🍏 Nutrio – AI-Powered Diet Planner

Nutrio is a web-based diet planning app designed to help users create personalized meal plans, track nutrition, and generate grocery lists.
It’s built using HTML, CSS, JavaScript, and Supabase for authentication & database storage.

🚀 Features

User Authentication – Secure login/signup with Supabase.

Personalized Diet Plans – AI-generated based on user details (age, weight, height, and goals).

Weekly Meal Calendar – Dynamic grid layout showing meals from Monday to Sunday.

Grocery List Generator – Auto-creates a shopping list based on your diet plan.

Responsive UI – Works seamlessly on desktop and mobile devices.


🛠 Tech Stack

Frontend: HTML, CSS, JavaScript

Backend / Database: Supabase (PostgreSQL + Auth)

AI API: Google Gemini (or compatible API) for meal plan generation

Hosting: (Add where you plan to host it, e.g., Vercel, Netlify, GitHub Pages)


📂 Project Structure

Nutrio/
│── index.html           # Landing page
│── goal.html            # Collects user goals
│── diet-planner.html    # Displays weekly diet plan
│── startingpage.html    # Intro page before login
│── styles.css           # Styling
│── script.js            # Core JavaScript logic
│── result.txt           # Stores AI-generated plan
│── supabase.js          # Supabase configuration
│── README.md            # This file

⚙️ How It Works

1.⁠ ⁠Sign Up / Log In

User creates an account with email and password via Supabase Auth.



2.⁠ ⁠Enter Details & Goal

Age, weight, height, and diet goal (e.g., weight loss, muscle gain).



3.⁠ ⁠Generate Diet Plan

Uses AI API to create a personalized weekly meal plan.



4.⁠ ⁠View in Calendar

Meals displayed in a structured grid for easy tracking.



5.⁠ ⁠Get Grocery List

Click a button to generate an ingredient list for the week.



