import re

def parse_diet_plan(raw_text):
    days = re.split(r"\*\*Day (\d+):\*\*", raw_text)
    structured = {}

    for i in range(1, len(days), 2):
        day_number = days[i]
        content = days[i + 1]
        meals = re.findall(r"\*\*(.*?)\*\* \| (.+)", content)
        structured[f"Day {day_number}"] = {meal: desc.strip() for meal, desc in meals}

    return structured
