# generate_grocery_html.py
from collections import defaultdict

# Read categorized grocery.txt
with open("static/grocery.txt", "r") as file:
    lines = file.readlines()

items = []
current_category = ""

for line in lines:
    line = line.strip()
    if not line or line.startswith("Weekly Grocery List"):
        continue
    if line.startswith("#"):
        current_category = line[1:].strip()
    elif "-" in line:
        name, count = line.rsplit("-", 1)
        items.append((current_category, name.strip(), count.strip()))

# Group items by category
grouped = defaultdict(list)
for cat, name, count in items:
    grouped[cat].append((name, count))

# Build HTML
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Grocery List</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #111;
      color: white;
      margin: 0;
      padding: 20px;
    }

    h2 {
      text-align: center;
      color: #4CAF50;
      margin-bottom: 30px;
    }

    .categories-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
    }

    .category-card {
      background-color: #1a1a1a;
      padding: 20px;
      border-radius: 12px;
      border: 1px solid #333;
    }

    .category-card h3 {
      margin-top: 0;
      margin-bottom: 15px;
      color: #4CAF50;
      font-size: 1.2rem;
      border-bottom: 1px solid #333;
      padding-bottom: 5px;
    }

    .ingredients-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      gap: 10px;
    }

    .ingredient {
      background-color: #222;
      padding: 10px;
      border-radius: 8px;
      text-align: center;
      font-size: 0.9rem;
      transition: 0.2s;
      cursor: pointer;
    }

    .ingredient:hover {
      background-color: #333;
    }

    .ingredient.checked {
      background-color: #4CAF50;
      color: white;
    }

    .ingredient .count {
      display: block;
      margin-top: 5px;
      font-size: 0.75rem;
      color: #bbb;
    }
  </style>
</head>
<body>
  <h2>Weekly Grocery List</h2>
  <div class="categories-grid">
"""

# Add each category and its ingredients
for category, ingredient_list in grouped.items():
    html += f'<div class="category-card"><h3>{category}</h3><div class="ingredients-grid">'
    for name, count in ingredient_list:
        html += f"""
        <div class="ingredient" onclick="this.classList.toggle('checked')">
          {name}<span class="count">{count}</span>
        </div>
        """
    html += "</div></div>"

html += """
  </div>
</body>
</html>
"""

# Save to grocery_list.html
with open("static/grocery_list.html", "w") as f:
    f.write(html)

print("✅ grocery_list.html created with compact layout and side-by-side categories.")