# . Implemente una clase que permita a un número cualquiera imprimir su valor,
# luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a
# las clases con las diferentes operaciones. Use un patrón decorator para
# implementar.


class Number:
    """
    Class representing a number.
    """

    def __init__(self, value):
        """
        Initializes a Number object with a given value.

        Args:
            value (int): The value of the number.
        """
        self.value = value

    def print_value(self):
        """
        Prints the value of the number.
        """
        print("Value:", self.value)


class OperationDecorator(Number):
    """
    Abstract base class for operation decorators.
    """

    def __init__(self, number):
        """
        Initializes an OperationDecorator object with a number.

        Args:
            number (Number): The number to be operated on.
        """
        self.number = number

    def print_value(self):
        """
        Prints the value of the number.
        """
        self.number.print_value()


class AddTwo(OperationDecorator):
    """
    Class representing an operation to add 2 to a number.
    """

    def print_value(self):
        """
        Prints the value of the number after adding 2.
        """
        super().print_value()
        self.number.value += 2
        print("After adding 2:", self.number.value)


class MultiplyByTwo(OperationDecorator):
    """
    Class representing an operation to multiply a number by 2.
    """

    def print_value(self):
        """
        Prints the value of the number after multiplying by 2.
        """
        super().print_value()
        self.number.value *= 2
        print("After multiplying by 2:", self.number.value)


class DivideByThree(OperationDecorator):
    """
    Class representing an operation to divide a number by 3.
    """

    def print_value(self):
        """
        Prints the value of the number after dividing by 3.
        """
        super().print_value()
        self.number.value /= 3
        print("After dividing by 3:", self.number.value)


# Usage
number = Number(5)
number.print_value()

# Adding operations sequentially
number = AddTwo(number)
number = MultiplyByTwo(number)
number = DivideByThree(number)
number.print_value()
