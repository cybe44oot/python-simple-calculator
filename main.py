# main.py
def add_numbers(a, b):
    """Add two numbers together here"""
    return a + b

def subtract_numbers(a, b):
    """Subtract b from a"""
    return a - b

if __name__ == "__main__":
    # This will only run when executing the file directly
    print("Running the calculator app!")
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"5 - 2 = {subtract_numbers(5, 2)}")
