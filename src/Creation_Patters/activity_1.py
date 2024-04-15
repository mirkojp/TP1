# Provea una clase que dado un número entero cualquiera retorne el factorial del
# mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
# instancia de clase.

class SingletonMeta(type):
    """
    Metaclass for implementing the Singleton pattern.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override the __call__ method to ensure only one instance is created.
        """
        if cls not in cls._instances:
            # If the instance doesn't exist, create it and store it
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Factorial_calculator(metaclass=SingletonMeta):
    """
    Class implementing a Factorial calculator using the Singleton pattern.
    """

    def factorial(self, number):
        """
        Calculates the factorial of a non-negative integer.
        """
        if number < 0:
            raise ValueError("Factorial only applies to non-negative numbers")
        elif number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)


if __name__ == "__main__":
    try:
        # Create an instance of the Factorial_calculator class
        Si_1 = Factorial_calculator()

        # Calculate factorial (intentionally passing a negative number to trigger an exception)
        Value = Si_1.factorial(-5)
        print(Value)

        # Create another instance of the Factorial_calculator class
        Si_2 = Factorial_calculator()

        # Check if both instances are the same (Singleton pattern)
        if Si_1 == Si_2:
            print(True)
    except Exception as e:
        # Handle any exceptions raised during execution
        print("Error:", e)
