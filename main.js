document.addEventListener("DOMContentLoaded", async function () {
  function getUserField(field) {
    const userDataStr = localStorage.getItem("userData");
    if (!userDataStr) return '';
    try {
      const userData = JSON.parse(userDataStr);
      return userData[field] || '';
    } catch {
      return '';
    }
  }

  const user = {
    name: getUserField("fullname"),
    email: getUserField("email"),
    age: getUserField("age"),
    gender: getUserField("gender"),
    weight: getUserField("weight"),
    height: getUserField("height"),
    goal: localStorage.getItem("goal") || '',
    allergies: localStorage.getItem("allergies") || '',
  };

  const displayMappings = {
    displayName: user.name,
    displayEmail: user.email,
    displayAge: user.age,
    displayGender: user.gender,
    displayWeight: user.weight,
    displayHeight: user.height,
    displayGoal: user.goal,
    displayAllergies: user.allergies || "None",
  };

  for (const [id, value] of Object.entries(displayMappings)) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  try {
    // ✅ Corrected endpoint (hyphen)
    const response = await fetch("http://localhost:8000/generate-diet", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    const plan = data.diet_plan || "No diet plan returned.";

    let dietContainer = document.getElementById("dietPlanContainer");
    if (!dietContainer) {
      dietContainer = document.createElement("div");
      dietContainer.id = "dietPlanContainer";
      dietContainer.style.marginTop = "30px";
      dietContainer.style.padding = "15px";
      dietContainer.style.background = "#222";
      dietContainer.style.borderRadius = "10px";
      dietContainer.style.color = "#fff";
      document.body.appendChild(dietContainer);
    }

    dietContainer.innerHTML = `<h3>Your AI Diet Plan:</h3><p>${plan.replace(/\n/g, "<br>")}</p>`;

  } catch (error) {
    console.error("Failed to fetch diet plan:", error);
    alert("Failed to generate diet plan. Please try again later.");
  }
  
});
