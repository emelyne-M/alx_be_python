# Prompt user for a single task
task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

# Process task using match-case
match priority:
    case "high":
        base = f"Reminder: '{task}' is a high priority task."
    case "medium":
        base = f"Reminder: '{task}' is a medium priority task."
    case "low":
        base = f"Reminder: '{task}' is a low priority task."
    case _:
        base = f"Reminder: '{task}' has an unspecified priority."

# Add time-bound info
if time_bound == "yes":
    if priority == "low":
        extra = " It is time-bound but not urgent."
    else:
        extra = " It is time-bound and requires immediate action."
else:
    extra = " It is not time-bound."

# FINAL OUTPUT 
print(f"{base}{extra}")
