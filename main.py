# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import google.generativeai as genai
# import os

# app = FastAPI()

# # CORS setup (you can restrict origins in production)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Set your Gemini API key here
# GOOGLE_API_KEY = "AIzaSyCj9ycvQefd2q1Ip81yAmHAVGBSAvtwL38"
# genai.configure(api_key=GOOGLE_API_KEY)

# class UserData(BaseModel):
#     name: str
#     age: int
#     gender: str
#     weight: float
#     height: float
#     email: str
#     goal: str
#     dietType: str
#     allergies: str = ""

# @app.post("/generate-diet")
# async def generate_diet(user: UserData):
#     prompt = f"""
# Generate a 7-day diet plan Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday(do not account today's day and give for all days irrespective) for the following user:
# Name: {user.name}
# Age: {user.age}
# Gender: {user.gender}
# Weight: {user.weight} kg
# Height: {user.height} cm
# Goal: {user.goal}
# Diet Type: {user.dietType}
# Allergies: {user.allergies or 'None'}


# Include meals for:
# - Early Morning
# - Breakfast
# - Mid-Morning
# - Lunch
# - Evening Snack
# - Pre-Dinner
# - Dinner

# Make it detailed, healthy, and goal-oriented.and display only the meal name for each category.
# """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-1.5-pro
#         response = model.generate_content(prompt)
#         return {"diet_plan": response.text}
#     except Exception as e:
#         return {"error": str(e)}
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import google.generativeai as genai

# app = FastAPI()

# # ✅ Allow cross-origin requests
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Change this to specific domains in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Define user input model
# class UserData(BaseModel):
#     name: str
#     age: int
#     weight: float
#     height: float
#     goal: str
#     allergies: str
#     gender: str
#     dietType: str

# # ✅ POST endpoint to generate diet plan
# @app.post("/generate-diet")
# async def generate_diet(user: UserData):
#     prompt = f"""
# Generate a 7-day diet plan Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday (do not account today's day and give for all days irrespective) for the following user:
# Name: {user.name}
# Age: {user.age}
# Gender: {user.gender}
# Weight: {user.weight} kg
# Height: {user.height} cm
# Goal: {user.goal}
# Diet Type: {user.dietType}
# Allergies: {user.allergies or 'None'}

# Include meals for:
# - Early Morning
# - Breakfast
# - Mid-Morning
# - Lunch
# - Evening Snack
# - Pre-Dinner
# - Dinner

# Make it detailed, healthy, and goal-oriented. Only display the meal name for each category.give the meal name as a single name for every meal.
# """

#     # ✅ Configure Google Gemini
#     genai.configure(api_key="AIzaSyCj9ycvQefd2q1Ip81yAmHAVGBSAvtwL38")
    
#     # ✅ Use correct model name (make sure this exists for your key)
#     model = genai.GenerativeModel("models/gemini-1.5-flash")  # or "models/gemini-pro" if supported
    
#     # ✅ Generate the diet plan
#     response = model.generate_content(prompt)

#     # ✅ Extract and save text
#     diet_text = response.text.strip()
#     with open("diet_plan.txt", "w") as f:
#         f.write(diet_text)

#     return {"diet": diet_text}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# import google.generativeai as genai
# import subprocess
# import shutil
# import os

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class UserData(BaseModel):
#     name: str
#     age: int
#     weight: float
#     height: float
#     goal: str
#     allergies: str
#     gender: str
#     dietType: str

# @app.post("/generate-diet")
# async def generate_diet(user: UserData):
#     prompt = f"""
# Generate a 7-day diet plan Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday (do not account today's day and give for all days irrespective) for an indian user (give indian meal) for the following user:
# Name: {user.name}
# Age: {user.age}
# Gender: {user.gender}
# Weight: {user.weight} kg
# Height: {user.height} cm
# Goal: {user.goal}
# Diet Type: {user.dietType}
# Allergies: {user.allergies or 'None'}

# Include meals for:
# - Early Morning
# - Breakfast
# - Mid-Morning
# - Lunch
# - Evening Snack
# - Pre-Dinner
# - Dinner

# Make it detailed, healthy, and goal-oriented. Only display the meal name for each category. Give the meal name as a single name for every meal.
# """

#     genai.configure(api_key="AIzaSyCj9ycvQefd2q1Ip81yAmHAVGBSAvtwL38")
#     model = genai.GenerativeModel("models/gemini-1.5-flash")
#     response = model.generate_content(prompt)

#     # Save diet plan to file
#     with open("diet_plan.txt", "w") as f:
#         f.write(response.text.strip())

#     # Run processing script
#     subprocess.run(["python3", "clean_diet.py"], check=True)
#     subprocess.run(["python3", "generate_calendar_from_result_txt.py"], check=True)


#     # Ensure static folder exists
#     os.makedirs("static", exist_ok=True)
#     shutil.move("result.txt", "static/result.txt")

#     return {"status": "success"}

# # Mount static folder for result.txt access
# app.mount("/static", StaticFiles(directory="static"), name="static")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
import google.generativeai as genai
import subprocess
import shutil
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User input schema
class UserData(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    goal: str
    allergies: str
    gender: str
    dietType: str

# Generate diet plan
@app.post("/generate-diet")
async def generate_diet(user: UserData):
    prompt = f"""
Generate a 7-day diet plan Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday (do not account today's day and give for all days irrespective) for an Indian user (give Indian meal) for the following user:
Name: {user.name}
Age: {user.age}
Gender: {user.gender}
Weight: {user.weight} kg
Height: {user.height} cm
Goal: {user.goal}
Diet Type: {user.dietType}
Allergies: {user.allergies or 'None'}

Include meals for:
- Early Morning
- Breakfast
- Mid-Morning
- Lunch
- Evening Snack
- Pre-Dinner
- Dinner

Make it detailed, healthy, and goal-oriented. Only display the meal name for each category. Give the meal name as a single name for every meal.
"""

    genai.configure(api_key="AIzaSyCj9ycvQefd2q1Ip81yAmHAVGBSAvtwL38")
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)

    with open("diet_plan.txt", "w") as f:
        f.write(response.text.strip())

    subprocess.run(["python3", "clean_diet.py"], check=True)
    subprocess.run(["python3", "generate_calendar_from_result_txt.py"], check=True)
    subprocess.run(["python3", "extract_grocery_list.py"], check=True)
    subprocess.run(["python3", "generate_grocery_html.py"], check=True)



    os.makedirs("static", exist_ok=True)
    shutil.move("result.txt", "static/result.txt")

    return {"status": "success"}

# Serve HTML pages dynamically (NOT static)
@app.get("/diet-calendar", response_class=HTMLResponse)
async def serve_diet_calendar():
    with open("diet_calendar.html", "r") as f:
        return f.read()

@app.get("/grocery-list", response_class=HTMLResponse)
async def serve_grocery_list():
    with open("grocery_list.html", "r") as f:
        return f.read()

# Serve plain result/grocery files if needed
@app.get("/data/result", response_class=FileResponse)
async def get_result():
    return FileResponse("static/result.txt")

@app.get("/data/grocery", response_class=FileResponse)
async def get_grocery():
    return FileResponse("static/grocery.txt")