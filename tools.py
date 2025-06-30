import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = os.getenv("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")  # Make sure your .env file has this key

def generate_diet_plan(user_data):
    prompt = f"""
    Generate a 7-day vegetarian diet plan for the following user:
    Name: {user_data.get('name')}
    Age: {user_data.get('age')}
    Gender: {user_data.get('gender')}
    Weight: {user_data.get('weight')} kg
    Height: {user_data.get('height')} cm
    Goal: {user_data.get('goal')} (options: weight loss, weight gain, maintenance, muscle gain)
    Allergies: {user_data.get('allergies') or 'None'}

    The plan should include Morning Drink, Breakfast, Mid-Morning Snack, Lunch, Evening Snack, Dinner, and Post-Dinner for each day (Monday to Sunday).

    Format the response clearly for HTML display.
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful dietician."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"DeepSeek API error: {response.status_code}, {response.text}")
