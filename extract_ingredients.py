
import os
import re
import google.generativeai as genai

genai.configure(api_key="AIzaSyAIdfceGfSTBmi5vqSds0BXefHijo6Wk-0")  # Replace with actual key
model = genai.GenerativeModel('gemini-1.5-flash')

INPUT_FILE = os.path.join("static", "grocery.txt")
OUTPUT_FILE = os.path.join("static", "ingredients.txt")

def is_meal(item):
    return (
        len(item.split()) > 1
        and not item.lower() in COMMON_INGREDIENTS
        and not item.strip().isdigit()
    )

COMMON_INGREDIENTS = {
    'salt', 'pepper', 'cheese', 'butter', 'milk', 'cream', 'egg', 'onion', 'garlic',
    'flax', 'grains', 'vegetables', 'banana', 'mango', 'paneer', 'yogurt', 'dal',
    'rice', 'potato', 'cottage cheese', 'fruit', 'salad', 'chutney', 'paratha',
    'peanut butter', 'protein shake', 'popcorn', 'makhana'
}

def extract_ingredients_with_gemini(meal_name):
    prompt = f"""
Meal: "{meal_name}"

Please give only the list of main ingredients used to cook this meal.

Output ONLY a bullet list of ingredients, like:
- ingredient1
- ingredient2
- ingredient3

Don't return the meal name or any explanations.
Avoid wrapping in markdown. Only ingredient names.
"""
    try:
        response = model.generate_content(prompt)
        ingredients_raw = response.text.strip()

        # Clean each line
        ingredients = []
        for line in ingredients_raw.split("\n"):
            line = line.strip("-• ").strip()
            if len(line.split()) <= 6 and not line.lower().startswith("please"):
                ingredients.append(line.lower())

        return ingredients
    except Exception as e:
        print(f"❌ Error processing {meal_name}: {e}")
        return []

def clean_line(line):
    # Remove trailing dash and numbers (e.g. "Apple - 1" → "Apple")
    return re.sub(r"[-–—]\s*\d+$", "", line).strip()

def main():
    final_ingredients = set()

    with open(INPUT_FILE, "r") as f:
        items = [clean_line(line.strip()) for line in f if line.strip()]

    for item in items:
        if not item or "please provide" in item.lower() or len(item) <= 1:
            continue

        if is_meal(item):
            print(f"🍽️ Processing meal: {item}")
            ingredients = extract_ingredients_with_gemini(item)
            final_ingredients.update(ingredients)
        else:
            final_ingredients.add(item.lower())

    # Write cleaned ingredients
    with open(OUTPUT_FILE, "w") as out:
        for ing in sorted(final_ingredients):
            out.write(ing + "\n")

    print("✅ ingredients.txt generated successfully.")

if __name__ == "__main__":
    main()
