import re
from collections import defaultdict
import os

# ✅ Simple mock dictionary of meal to ingredient mappings
meal_to_ingredients = {
    "Protein Shake": ["Protein powder", "Milk", "Banana"],
    "Egg Burji": ["Eggs", "Onion", "Tomato", "Spices"],
    "Oatmeal": ["Oats", "Milk", "Fruit"],
    "Chapati": ["Wheat flour", "Water", "Salt"],
    "Chicken Curry": ["Chicken", "Onion", "Tomato", "Spices", "Oil"],
    "Fish Fry": ["Fish", "Spices", "Oil"],
    "Brown Rice": ["Brown rice"],
    "Greek Yogurt": ["Milk"],
    "Paneer Tikka": ["Paneer", "Yogurt", "Spices"],
    "Fruit Salad": ["Apple", "Banana", "Papaya"],
    "Dal": ["Lentils", "Onion", "Tomato", "Spices"],
    "Vegetable Stir-fry": ["Carrot", "Beans", "Capsicum", "Oil"],
    "Chutney": ["Coconut", "Green Chilli", "Salt", "Oil"],
    # Add more meals as needed
}

# ✅ Read diet plan
with open("result.txt", "r") as file:
    diet = file.read()

# ✅ Extract all meals from the diet plan
meals = re.findall(r"<td>(.*?)</td>", diet)

ingredient_counts = defaultdict(int)

# ✅ Extract ingredients from each meal name
for meal in meals:
    ingredients = meal_to_ingredients.get(meal.strip(), [])
    for ing in ingredients:
        ingredient_counts[ing] += 1

# ✅ Save to grocery.txt
with open("grocery.txt", "w") as file:
    for item, count in sorted(ingredient_counts.items()):
        file.write(f"{item}: {count}\n")

print("✅ Grocery list extracted to grocery.txt")
