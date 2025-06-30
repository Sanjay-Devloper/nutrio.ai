async function saveDietPlanToSupabase(dietData, weekStartDate) {
  const supabaseUrl = 'https://YOUR_PROJECT_ID.supabase.co';
  const supabaseKey = 'YOUR_PUBLIC_ANON_KEY';
  const supabase = supabase.createClient(supabaseUrl, supabaseKey);

  const user = await supabase.auth.getUser();
  const userId = user.data.user.id;

  const { error } = await supabase
    .from('diet_plans')
    .insert([
      {
        user_id: userId,
        week_start: weekStartDate, // example: '2025-06-24'
        diet_data: dietData,       // JSON object
      }
    ]);

  if (error) {
    console.error('Failed to save diet plan:', error);
    alert('Error saving diet plan!');
  } else {
    console.log('Diet plan saved!');
    alert('Diet plan saved successfully!');
  }
}
