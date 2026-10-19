# Part 1 Writing and Using Functions
def greet_user(name=""):
    """Greets the user. If no name is provided, uses a default greetinf."""
    if name:
        print (f"Hello, {name}! Welcome!")
    else:
        print ("Hello! Welcome!")
def add_two_numbers(a,b):
    """Returns the sum of two numbers."""
    return a + b
def is_even(num):
    """Returns True if num is even, False otherwise."""
    return num % 2 == 0
# Demonstrating each function in the main part of the script
if __name__ == "__name__":
    print("--- Testing greet_user() ---")
    greet_user("Alice")
    greet_user() # Called without a name
    print("\n-- Testing add_two_nembers()")
    sum_result = add_two_numbers(15, 27)
    print (f"The sum of 15 and 27 is: {sum_result}")
    print ("\n--- Testing is_even() ---")
    even_check = 4
    odd_check = 7
    print(f"{even_check} is even: {is_even(even_check)}")
    print(f"{odd_check} is even: {is_even(odd_check)}")
# Part 1 (Calculating)
def add(a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a/b
def calculate (a, b, op):
    """Takes two numbers and an operator symbol, then calls the respective function."""
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subbtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    else:
        raise ValueError(f"Invalid operation symbol: {op}'")
    if __name__ == "__main__":
        print("--- Refactored Calculator ---")
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            operator = input("Enter operation (+, -, *, /):")
            result = calculate(num1, num2, operator)
            print(f"Result: {num1} {operator} {num2} = {result}")
        except VallueError as ve:
                print(f"Input Error: {ve}")
        except ZeroDivisionError as zde:
                print(f"Math Error: {zde}")

