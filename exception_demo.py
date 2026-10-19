# Part 3
def safe_divide(a, b):
    """Returns a / b if is not zero. Raises a ValueError if zero."""
    if b == 0:
        raise ValueError ("Cannot divide by zero.")
    return a / b
if __name__ == "__main__":
    print ("--- Testing safe_divide with Try/Except & Finally ---")
    test_values = [(10, 2),(5, 0)]
    for numerator, dominator in test_values:
        try:
            result = safe_divide(numerator, dominator)
            print(f"Success: {numerator} / {dominator} = {result}")
        except ValueError as e:
                print(f"Caught Excemption: {e}")
        finally:
                print("Division opration completed. \n")
        print("--- Testing Generic Exception (Invalid String to Int Conversion) ---")
        try:
            user_input = "not_a_number"
            coverted_value = int(user_input)
        except Exception as e:
            print(f"Caught Excemption during conversion: {e}")



