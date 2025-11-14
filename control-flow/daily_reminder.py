task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_msg = "a high priority task"
    case "medium":
        priority_msg = "a medium priority task"
    case "low":
        priority_msg = "a low priority task"
    case _:
        priority_msg = "a task with unknown priority"

if time_bound == "yes":
    final_msg = f"'{task}' is {priority_msg} that requires immediate attention today!"
else:
    final_msg = f"'{task}' is {priority_msg}. Consider completing it when you have free time."

print("\nReminder:", final_msg)