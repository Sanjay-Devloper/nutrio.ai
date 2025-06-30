# clean_diet.py
import re

input_file = "diet_plan.txt"
output_file = "result.txt"

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

meal_categories = [
    "Early Morning", "Breakfast", "Mid-Morning", "Lunch",
    "Evening Snack", "Pre-Dinner", "Dinner"
]

current_day = None
output_lines = []

with open(input_file, "r") as infile:
    lines = infile.readlines()

    for line in lines:
        line = line.strip()

        if not line or "Important Note" in line:
            continue

        # Match a day header (with or without punctuation)
        day_match = re.match(r"[*\-]*\s*(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)[:\s\-]*", line, re.IGNORECASE)
        if day_match:
            current_day = day_match.group(1).capitalize()
            output_lines.append(f"\n{current_day}")
            continue

        # Match meal entries
        meal_match = re.match(r"[-*]*\s*(Early Morning|Breakfast|Mid-Morning|Lunch|Evening Snack|Pre-Dinner|Dinner):\s*(.+)", line)
        if meal_match and current_day:
            meal_type = meal_match.group(1)
            meal_item = meal_match.group(2)
            output_lines.append(f"{meal_type}: {meal_item}")

with open(output_file, "w") as outfile:
    outfile.write("\n".join(output_lines).strip())

print("✅ Cleaned diet plan saved to result.txt")
