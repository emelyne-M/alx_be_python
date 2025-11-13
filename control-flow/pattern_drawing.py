
    # pattern_drawing.py

# Prompt user for pattern size (exact ALX prompt)
size = int(input("Enter the size of the pattern:"))

# Initialize row counter
i = 0

# Outer while loop for each row
while i < size:
    # Inner for loop for each column
    for j in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to next line after row
    i += 1  # Increment row counter
