
# import time
# import google.generativeai as genai

# # ✅ Configure Gemini API
# genai.configure(api_key="AIzaSyCj9ycvQefd2q1Ip81yAmHAVGBSAvtwL38")

# # ✅ Read meal names from result.txt
# with open("result.txt", "r") as f:
#     lines = f.readlines()

# meals = []
# for line in lines:
#     line = line.strip()
#     if line and not line.startswith("Day"):
#         parts = line.split(":")
#         if len(parts) > 1:
#             meals.append(parts[1].strip())

# # ✅ Prepare to store all ingredients
# all_ingredients = {}

# model = genai.GenerativeModel("models/gemini-1.5-flash")

# for meal in meals:
#     try:
#         prompt = f"""
# List all the ingredients needed to prepare this Indian meal:

# Meal: {meal}

# Only return the ingredient names in a comma-separated list. Do not include any extra words or steps.
# """
#         response = model.generate_content(prompt)
#         text = response.text.strip()
#         ingredients = [i.strip().title() for i in text.replace("\n", ",").split(",") if i.strip()]
#         all_ingredients[meal] = ingredients
#         time.sleep(5)  # prevent hitting rate limit
#     except Exception as e:
#         all_ingredients[meal] = [f"Error fetching ingredients: {str(e)}"]

# # ✅ Save all ingredients to static/all_ingredients.txt
# with open("static/all_ingredients.txt", "w") as f:
#     for meal, ingredients in all_ingredients.items():
#         f.write(f"{meal}:\n")
#         for ing in ingredients:
#             f.write(f"- {ing}\n")
#         f.write("\n")
