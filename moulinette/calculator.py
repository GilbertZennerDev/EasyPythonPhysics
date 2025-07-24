class calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplicate(self, a, b):
        return a * b

    def divide(self, a, b):
        # error handling
        if b == 0:
            raise ValueError("Division by Zero not allowed")
        return a / b

#running code
if __name__ == "__main__":
    my_calculator = calculator()
    print(f"2 + 3 = {my_calculator.addition(2, 3)}")
    print(f"10 - 4 = {my_calculator.subtraction(10, 4)}")
    print(f"5 * 6 = {my_calculator.multiplicate(5, 6)}")
    try:
        print(f"10 / 2 = {my_calculator.divide(10, 2)}")
        print(f"10 / 0 = {my_calculator.divide(10, 0)}") # This creates en error
    except ValueError as e:
        print(f"Error: {e}")
