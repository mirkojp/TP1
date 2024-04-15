# . Implemente una clase que permita a un número cualquiera imprimir su valor,
# luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a
# las clases con las diferentes operaciones. Use un patrón decorator para
# implementar.


class Number:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Value:", self.value)


class OperationDecorator(Number):
    def __init__(self, number):
        self.number = number

    def print_value(self):
        self.number.print_value()


class AddTwo(OperationDecorator):
    def print_value(self):
        super().print_value()
        self.number.value += 2
        print("After adding 2:", self.number.value)


class MultiplyByTwo(OperationDecorator):
    def print_value(self):
        super().print_value()
        self.number.value *= 2
        print("After multiplying by 2:", self.number.value)


class DivideByThree(OperationDecorator):
    def print_value(self):
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
