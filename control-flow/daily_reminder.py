
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to set the base message according to priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority"

# Use if to modify reminder if time-bound
if time_bound == "yes":
    # urgent message for time-bound tasks
    print(f"Reminder: {base_message} that requires immediate attention today!")
else:
    # non-urgent note (matches the example output format)
    if priority in ("high", "medium", "low"):
        print(f"Note: {base_message}. Consider completing it when you have free time.")
    else:
        print(f"Reminder: {base_message}.")