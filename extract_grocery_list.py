import re
from collections import defaultdict

# Step 1: Load lines
with open("result.txt") as f:
    lines = f.readlines()

ingredient_counts = defaultdict(int)

# Master list of known grocery ingredients
all_ingredients = [
    # Single and compound ingredients
    "banana", "apple", "grapes", "orange", "melon", "papaya", "berries", "pear",
    "milk", "curd", "yogurt", "cheese", "paneer", "greek yogurt", "cottage cheese", "butter",
    "chicken", "egg", "tofu", "mutton", "fish", "lentils", "dal", "chickpeas", "peanut", "keema",
    "protein shake", "whey", "omelette",
    "rice", "roti", "bread", "whole wheat bread", "paratha", "chapati", "upma", "idli", "dosa", "poha", "chilla", "oats",
    "spinach", "carrot", "cabbage", "broccoli", "beans", "green beans", "cucumber", "vegetables", "tomato", "onion", "celery", "capsicum",
    "almonds", "walnuts", "cashews", "seeds", "peanut butter", "sunflower seed", "chia",
    "olive oil", "salt", "pepper", "honey", "lemon", "ginger", "garlic", "red chili powder"
]

# Lowercase for safe matching
ingredient_keywords = set(all_ingredients)

# Clean and match
for line in lines:
    if ':' not in line or line.strip() in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        continue

    _, meal = line.split(":", 1)
    meal = meal.lower()

    # Remove punctuation
    meal = re.sub(r"[^\w\s]", "", meal)

    # Check for presence of any known ingredient (even compound phrases)
    for ingredient in ingredient_keywords:
        if ingredient in meal:
            ingredient_counts[ingredient.title()] += 1

# Categories
categories = {
    "Fruits": ["Banana", "Apple", "Grapes", "Orange", "Melon", "Papaya", "Berries", "Pear"],
    "Dairy": ["Milk", "Curd", "Yogurt", "Cheese", "Paneer", "Greek Yogurt", "Cottage Cheese", "Butter"],
    "Protein": ["Chicken", "Egg", "Tofu", "Mutton", "Fish", "Lentils", "Dal", "Chickpeas", "Peanut", "Protein Shake", "Whey", "Omelette", "Keema"],
    "Grains": ["Rice", "Roti", "Bread", "Whole Wheat Bread", "Paratha", "Chapati", "Upma", "Idli", "Dosa", "Poha", "Chilla", "Oats"],
    "Vegetables": ["Spinach", "Carrot", "Cabbage", "Broccoli", "Beans", "Cucumber", "Tomato", "Onion", "Green Beans", "Celery", "Capsicum"],
    "Nuts & Seeds": ["Almonds", "Walnuts", "Cashews", "Seeds", "Peanut Butter", "Sunflower Seed", "Chia"],
    "Others": ["Olive Oil", "Salt", "Pepper", "Honey", "Lemon", "Ginger", "Garlic", "Red Chili Powder"]
}

# Categorize
categorized = defaultdict(list)

for item, count in ingredient_counts.items():
    placed = False
    for cat, keywords in categories.items():
        if item in keywords:
            categorized[cat].append((item, count))
            placed = True
            break
    if not placed:
        categorized["Others"].append((item, count))

# Output grocery.txt
with open("static/grocery.txt", "w") as f:
    f.write("Weekly Grocery List (Categorized)\n==============================\n")
    for cat in categories.keys():
        if categorized[cat]:
            f.write(f"# {cat}\n")
            for item, count in sorted(categorized[cat]):
                f.write(f"{item} - {count}\n")
            f.write("\n")
