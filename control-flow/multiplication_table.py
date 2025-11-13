number= int(input("Enter a number to see its multiplication table:."))

for x in range(1, 11):  # starts at 1, ends at 10
    print(f"{number} * {x} = {number * x}")