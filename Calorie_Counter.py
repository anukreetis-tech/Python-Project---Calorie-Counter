FOOD_DATABASE = {
    # Main Courses (Curries/Gravies) - Approx. per 1.5 cup serving
    "butter chicken (murgh makhani)": 400,
    "dal makhani (1 cup)": 350,
    "shahi paneer (1.5 cup)": 420,
    "palak paneer (1.5 cup)": 300,
    "kadai paneer (1.5 cup)": 350,
    "rajma chawal (1 cup curry + 1 cup rice)": 450,
    "chana masala (1 cup)": 250,
    "malai kofta (2 koftas + gravy)": 500,
    "rogan josh (lamb curry, 1.5 cup)": 400,

    # Breads & Sides
    "plain naan (1 piece)": 260,
    "butter naan (1 piece)": 320,
    "tandoori roti (1 piece)": 120,
    "aloo paratha (1 piece)": 280,
    "plain rice (1 cup cooked)": 205,
    "jeera rice (1 cup cooked)": 220,

    # Snacks & Street Food
    "samosa (1 piece)": 250,
    "aloo tikki (1 patty)": 150,
    "chole bhature (1 bhatura + chole)": 550,
    
    # Desserts & Drinks
    "gulab jamun (1 piece)": 150,
    "jalebi (2 pieces)": 180,
    "sweet lassi (1 glass)": 220,
}

# --- Main Program ---
def run_food_tracker():
    print("🥗 North Indian Calorie Log Tracker")
    print("-----------------------------------")

    try:
        # 1. Set the Goal
        daily_goal = float(input("Enter your **daily calorie goal** (e.g., 2000): "))
        calories_consumed = 0
        
        while True:
            # 2. Display Status
            remaining = daily_goal - calories_consumed
            print("\n--- Daily Status ---")
            print(f"Goal: {daily_goal:.0f} cal | Consumed: {calories_consumed:.0f} cal | Remaining: {remaining:.0f} cal")
            print("--------------------")

            # 3. List Available Foods
            print("\n**Available North Indian Foods (Enter 'done' to quit):**")
            
            # Print a neatly formatted list of the food items
            for i, (food, cal) in enumerate(FOOD_DATABASE.items()):
                print(f"  {i+1}. {food.title():<30}: {cal} cal")
            print("--------------------------------------------------")

            # 4. Get User Input
            food_name = input("Log food (e.g., 'Butter Chicken' or 'done'): ").strip().lower()

            if food_name == 'done':
                break
            
            # 5. Look up and Log (Fuzzy matching for better user experience)
            matched_food = None
            
            # First, check for exact match
            if food_name in FOOD_DATABASE:
                matched_food = food_name
            else:
                # Check for partial matches (e.g., 'naan' matches 'plain naan')
                for key in FOOD_DATABASE:
                    if food_name in key:
                        matched_food = key
                        break
            
            if matched_food:
                calories = FOOD_DATABASE[matched_food]
                calories_consumed += calories
                print(f"✅ Logged {matched_food.title()} ({calories} cal).")
            else:
                print("❌ Food item not found in the database. Please try again or check spelling.")

    except ValueError:
        print("\n**ERROR:** Please ensure you enter a valid number for your calorie goal.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        
    finally:
        # Final summary when the user types 'done'
        print("\n====================================")
        print("Daily Summary:")
        print(f"Goal: {daily_goal:.0f} cal")
        print(f"Total Consumed: {calories_consumed:.0f} cal")
        final_remaining = daily_goal - calories_consumed
        print(f"Remaining: {final_remaining:.0f} cal")
        if final_remaining >= 0:
            print("Great job tracking your calories! 👍")
        else:
            # Calculate the amount over the goal
            over_by = abs(final_remaining)
            print(f"You were **{over_by:.0f} calories** over your goal. 🛑")
        print("====================================")

if __name__ == "__main__":
    run_food_tracker()
