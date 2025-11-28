
# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Command-line mode
    if len(sys.argv) == 3:
        numerator = sys.argv[1]
        denominator = sys.argv[2]
        result = safe_divide(numerator, denominator)
        print(result)
        return

    # Interactive mode
    print("Welcome to the Robust Division Calculator!")
    print("Type 'exit' to quit.")

    while True:
        numerator = input("Enter numerator: ").strip()
        if numerator.lower() == "exit":
            print("Goodbye!")
            break

        denominator = input("Enter denominator: ").strip()
        if denominator.lower() == "exit":
            print("Goodbye!")
            break

        
        result = safe_divide(numerator, denominator)

       
        print(result)

if __name__ == "__main__":
    main()
