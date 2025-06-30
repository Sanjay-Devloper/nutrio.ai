# # generate_calendar_from_result_txt.py
# from collections import defaultdict

# # Define meals and days
# meal_categories = [
#     "Early Morning", "Breakfast", "Mid-Morning", "Lunch",
#     "Evening Snack", "Pre-Dinner", "Dinner"
# ]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # Prepare dictionary structure
# calendar = {meal: {day: "" for day in days} for meal in meal_categories}

# # Read cleaned result.txt
# with open("result.txt", "r") as file:
#     lines = file.readlines()

# current_day = None
# for line in lines:
#     line = line.strip()
#     if line in days:
#         current_day = line
#     elif ':' in line and current_day:
#         try:
#             meal, food = line.split(":", 1)
#             meal = meal.strip()
#             food = food.strip()
#             if meal in meal_categories:
#                 calendar[meal][current_day] = food
#         except Exception:
#             pass

# # Generate HTML table string
# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Weekly Diet Calendar</title>
#     <style>
#     body {
#         font-family: Arial, sans-serif;
#         background-color: #111;
#         color: white;
#         padding: 20px;
#     }
#     h2 {
#         text-align: center;
#         color: white;
#     }
#     table {
#         border-collapse: collapse;
#         width: 100%;
#         table-layout: fixed;
#         background-color: #000;
#     }
#     th, td {
#         border: 1px solid #444;
#         padding: 12px;
#         color: white;
#     }
#     th {
#         background-color: #16a34a;
#         text-align: center;
#     }
#     td {
#         background-color: #111;
#         height: 90px;
#         overflow-wrap: break-word;
#         text-align: center;
#         vertical-align: middle;
#     }
#     </style>
# </head>
# <body>
#     <h2>Weekly Diet Calendar</h2>
#     <table>
#         <tr>
#             <th>Meal / Day</th>"""

# # Add table headers
# for day in days:
#     html += f"<th>{day}</th>"
# html += "</tr>"

# # Add rows
# for meal in meal_categories:
#     html += f"<tr><th>{meal}</th>"
#     for day in days:
#         food = calendar[meal][day]
#         html += f"<td>{food}</td>"
#     html += "</tr>"

# html += """
#     </table>
# </body>
# </html>
# """

# # Save HTML output
# with open("static/diet_calendar.html", "w") as f:
#     f.write(html)

# print("✅ Styled diet calendar saved as 'static/diet_calendar.html'")

# generate_calendar_from_result_txt.py
from collections import defaultdict

# Define meals and days
meal_categories = [
    "Early Morning", "Breakfast", "Mid-Morning", "Lunch",
    "Evening Snack", "Pre-Dinner", "Dinner"
]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Prepare dictionary structure
calendar = {meal: {day: "" for day in days} for meal in meal_categories}

# Read cleaned result.txt
with open("result.txt", "r") as file:
    lines = file.readlines()

current_day = None
for line in lines:
    line = line.strip()
    if line in days:
        current_day = line
    elif ':' in line and current_day:
        try:
            meal, food = line.split(":", 1)
            meal = meal.strip()
            food = food.strip()
            if meal in meal_categories:
                calendar[meal][current_day] = food
        except Exception:
            pass

# Generate HTML table with sidebar
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Weekly Diet Calendar</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #111;
      color: white;
      margin: 0;
      overflow-x: hidden;
    }
    .sidebar a {
  display: block;
  padding: 10px;
  margin: 5px 0;
  background-color: #222;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

.sidebar a:hover {
  background-color: #444;
}

    .sidebar {
      position: fixed;
      top: 0;
      left: -250px;
      width: 250px;
      height: 100%;
      background-color: #1e1e1e;
      padding: 20px;
      transition: left 0.3s ease;
      z-index: 1000;
    }
    .sidebar.active {
      left: 0;
    }
    .sidebar h3 {
      color: #4CAF50;
      margin-bottom: 20px;
    }
    .sidebar a {
      display: block;
      margin-bottom: 12px;
      color: white;
      padding: 10px;
      background: #222;
      text-decoration: none;
      border-radius: 5px;
    }
    .sidebar a:hover {
      background-color: #444;
    }
    .menu-button {
      position: fixed;
      top: 20px;
      left: 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      font-size: 20px;
      padding: 10px 15px;
      border-radius: 6px;
      cursor: pointer;
      z-index: 1001;
    }
    .content {
      margin-left: 80px;
      padding: 20px;
    }
    h2 {
      text-align: center;
      margin-bottom: 20px;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      table-layout: fixed;
    }
    th, td {
      border: 1px solid #444;
      padding: 12px;
      text-align: center;
      word-wrap: break-word;
    }
    th {
      background-color: #16a34a;
    }
    td {
      background-color: #111;
    }
    body {
  font-family: Arial, sans-serif;
  background-color: #111;
  color: white;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.container {
  margin-left: 60px; /* leave space for the menu button */
  padding: 20px;
  padding-right: 0;
}

h2 {
  text-align: center;
  color: white;
  margin: 20px 0;
}

table {
  border-collapse: collapse;
  width: 100%;
  table-layout: fixed;
  background-color: #000;
  margin: 0;
}

th, td {
  border: 1px solid #444;
  padding: 12px;
  color: white;
  text-align: center;
  vertical-align: middle;
}

th {
  background-color: #16a34a;
}

  </style>
</head>
<body>

  <button class="menu-button" onclick="toggleSidebar()">☰</button>
  <div id="sidebar" class="sidebar">
  <h3>Menu</h3>

  <!-- Grocery List (New Tab) -->
  <a href="grocery_list.html" target="_blank">🛒 Grocery List</a>

  <!-- Profile (Placeholder) -->
  <a href="body-facts.html" target="_blank">👤 Profile</a>

  <!-- Home Page -->
  <a href="index.html">🏠 Home</a>
</div>


  <div class="content">
    <h2>Weekly Diet Calendar</h2>
    <table>
      <tr>
        <th>Meal / Day</th>"""

# Add column headers
for day in days:
    html += f"<th>{day}</th>"
html += "</tr>"

# Add table rows
for meal in meal_categories:
    html += f"<tr><th>{meal}</th>"
    for day in days:
        html += f"<td>{calendar[meal][day]}</td>"
    html += "</tr>"

# Finish HTML
html += """
    </table>
  </div>

  <script>
    function toggleSidebar() {
      document.getElementById("sidebar").classList.toggle("active");
    }
  </script>

</body>
</html>
"""

# Save to file
with open("static/diet_calendar.html", "w") as f:
    f.write(html)

print("✅ diet_calendar.html generated with sidebar menu")