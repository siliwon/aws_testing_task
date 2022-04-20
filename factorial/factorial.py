import sys


class Factorial:
    """Factorial is the product of all positive integers less than or equal to n"""

    def __init__(self, user_number):
        self.number = user_number
        
    def get_factorial(self):
        """The interface for calculating the factorial"""
        if isinstance(self.number, (int, str)):
            try:
                self.number = int(self.number)
                sys.setrecursionlimit(sys.getrecursionlimit() + self.number ** 2) # dynamically increasing the recursion limit; the **2 is due to avoiding math.abs()
                return self.integer_handler()
            except (TypeError, ValueError):
                return f"Sorry, the value you gave ({self.number}) is not an integer!"
        return f"Sorry, the value you gave ({self.number}) is not an integer!"

    def integer_handler(self):
        if self.number > 0:
            return self.factorial_calculator(self.number)
        elif self.number == 0:
            return self.zero_handler()
        else:
            return self.negative_handler()

    def zero_handler(self):
        return 1
    
    def negative_handler(self):
        return f"Sorry, the number you gave ({self.number}) is not positive!"
    
    def factorial_calculator(self, number):
        if number > 1:
            number *= self.factorial_calculator(number - 1)
        return number


if __name__ == "__main__":
    user_input = input("Enter your integer: ")
    factorial = Factorial(user_input)
    print(factorial.get_factorial())
