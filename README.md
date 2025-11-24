**CALORIE COUNTER**

This is a simple command-line calorie tracking application built in Python. It allows users to set a daily calorie goal and log consumed food items from a predefined database of popular food items.

FEATURES

GOAL SETTING: Define your daily calorie target.

FOOD DATABASE: Includes estimated calorie counts for common dishes like Dal Makhani, Butter Chicken, Aloo Paratha, and more.

REAL-TIME TRACKING: Displays calories consumed and remaining calories after every log entry.

SIMPLE COMMAND LINE INTERFACE: Easy to run and use directly in your terminal.

PREREQUISITES

You only need a Python interpreter installed on your system.

Python 3.6 or higher (Tested and confirmed to run on standard Python environments).

HOW TO RUN THE PROGRAM

Save the Code: Save the provided Python code (the run_food_tracker function and the FOOD_DATABASE dictionary) into a file named calorie_counter.py.

Execute from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and run: python calorie_counter.py

HOW TO USE

The program runs in a continuous loop until you manually exit.

Set Your Goal: When the script starts, enter your target calorie intake for the day.

Enter your **daily calorie goal** (e.g., 2000): 2000

View Status: The program will display your current goal, consumed calories, and remaining balance.

Log Food: Enter the full name of the food item exactly as it appears in the Available Foods list. You can use lowercase or uppercase.

Example Log:

Log food (e.g., 'Butter Chicken' or 'done'): Aloo Paratha (1 Piece)

✅ Logged Aloo Paratha (1 Piece) (280 cal).

Finish Logging: Type done and press Enter to exit the logging loop and view your final daily summary.

FUTURE IMPROVEMENTS

Implement a feature to handle quantities (e.g., logging "2 Samosas").

Allow users to add new food items to the database dynamically.

Save the daily log to a file (CSV or JSON) for persistence across sessions.

Use an external API (like USDA or similar nutrition services) for a vast and accurate database of food items.
