''' 
Create a mini calculator where each mathematical operation is implemented as a separate function 
and a main function controls the program.
'''
# --- Operation Functions ---

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# --- Main Controller Function ---

def main():
    while True:
        print("\n--- Mini Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select between 1 and 5.")


# Program execution start point
main()

'''  
Modular Structure: The program follows modular programming principles by defining distinct functions for each mathematical
 operation: add(), subtract(), multiply(), and divide().

Zero Division Handling: The divide() function includes an explicit condition check (b == 0) to prevent 
runtime crashes caused by division by zero.

Control Flow (main function): The main() function acts as the central controller, using a while True loop 
to display a continuous interactive menu until the user selects option 5 to exit.

Input Validation: User choices are validated using simple if-elif-else conditions to ensure only 
supported operations (1 to 4) trigger calculations, while invalid entries display a warning prompt.
'''
