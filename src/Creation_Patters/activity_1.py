class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Factorial_calculator(metaclass=SingletonMeta):
    """
    This Class implements the metaclass SingletonMeta, so you can define
    differentes variables yet both are linked with the same instance of the class
    """

    def factorial(self,number):
        if number < 0:
            raise ValueError("Factorial only applies to non-negative numbers")
        elif number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)

if __name__ == "__main__":
    try:
        Si_1= Factorial_calculator()
        Value = Si_1.factorial(-5)
        print(Value)
        Si_2= Factorial_calculator()
        if Si_1 == Si_2:
            print(True)
    except Exception as e:
        print("Error:", e)
