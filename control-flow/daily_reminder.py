# Prompt user for a single task
task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

# Process task using match-case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task."
    case "low":
        message = f"Note: '{task}' is a low priority task."
    case _:
        message = f"Note: '{task}' has an unspecified priority."

# Add time sensitivity information (always)
if time_bound == "yes":
    message += " It is time-bound and requires immediate action."
else:
    message += " It is not time-bound."

# Print the final reminder
print(message)
