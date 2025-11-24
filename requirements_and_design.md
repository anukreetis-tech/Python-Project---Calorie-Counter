1. Functional Requirements (FR)

Given below are the Module and their Requirement Description

Goal Management: The system must prompt the user to set a specific daily calorie intake goal upon startup.

Data Module: The system must store a fixed dictionary (FOOD_DATABASE) of food names and their estimated calorie values.

Logging:The system must accept user input for a consumed food item.

Logging(2): The system must perform a case-insensitive match between user input and the food database keys.

Tracking: The system must calculate and update the total calories consumed for the current session.

Tracking: The system must display the current consumed and remaining calories after every successful log entry.

I/O: The system must use clear, formatted text for all prompts and status updates.

2. Non-Functional Requirements 

Given below are the Categories and their Requirement Description

Usability: The application must be runnable directly from the command line with standard Python and feature intuitive, simple commands ('done') for navigation.

Performance: Food lookup and calorie calculation must be instantaneous (sub-second response time) due to the in-memory data model.

Reliability: The system must handle non-numeric input for the calorie goal and unknown food names gracefully, printing an error message instead of crashing.

Maintainability: The calorie data must be stored in a separate, easily editable section (the Python dictionary) away from the core tracking logic.

3. Design Diagram Descriptions

3.1. System Architecture

Type: Monolithic, Single-Tier (suitable for CLI).

Components:

Data Layer: The hard-coded Python dictionary (FOOD_DATABASE).

Logic Layer: The main function that orchestrates I/O, search, and calculation.

Presentation Layer: The console output (print/input).

3.2. Workflow Diagram (Process Flow)

The application operates on a simple control loop:

Setup: Prompt user for daily_goal --> Validate input.

Loop: Continuously display status --> Get food input.

Decision Point: If input is 'done', print summary and exit.

Logging: Look up food --> If found, update calories_consumed --> Loop. If not found, show error --> Loop.

3.3. Sequence Diagram (Logging Food)

Given below are Participant and Action

User:- Provides input: food_name

run_food_tracker:- Receives input and initiates data lookup.

run_food_tracker:- Lookup(name) in FOOD_DATABASE

FOOD_DATABASE:- Return calories--> run_food_tracker

run_food_tracker:- Updates internal calories_consumed variable.

run_food_tracker:- Print status --> User (Console)
