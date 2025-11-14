task = input("Enter the task: ")
time_bound = input("Is the task time-bound? (yes/no): ").lower()
priority = input("Enter the priority level (high/medium/low): ").lower()

# Match-case based on priority
match priority:
    case "high":
        priority_message = "This task is very important."
    case "medium":
        priority_message = "This task has a moderate priority."
    case "low":
        priority_message = "This task can be done later."
    case _:
        priority_message = "Priority not recognized."

# If statement to handle time sensitivity
if time_bound == "yes":
    time_message = "You must complete this task immediately!"
else:
    time_message = "This task is not urgent."

# Final customized reminder
print(f"Reminder: {task}")
print(f"Priority: {priority_message}")
print(f"Urgency: {time_message}")