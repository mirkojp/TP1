# Implemente una clase “factura” que tenga un importe correspondiente al total
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
# condición.
from abc import ABC, abstractmethod


class Bill(ABC):
    """
    Abstract base class for generating invoices.
    """

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def get_tax(self):
        """
        Abstract method to be implemented by concrete invoice classes.
        """
        pass


class ResponsibleCondition(Bill):
    """
    Concrete class for generating invoices for clients with IVA Responsible condition.
    """

    def get_tax(self):
        return f"IVA Responsible - Amount ${self.amount}"


class NonEnrolledCondition(Bill):
    """
    Concrete class for generating invoices for clients with IVA No Inscripto condition.
    """

    def get_tax(self):
        return f"IVA Non Inscripto - Amount ${self.amount}"


class ExemptCondition(Bill):
    """
    Concrete class for generating invoices for clients with IVA Exento condition.
    """

    def get_tax(self):
        return f"IVA Exento - Amount ${self.amount}"


class ConditionFactory:
    """
    Factory class for creating invoice objects based on client tax condition.
    """

    @staticmethod
    def create_condition(condition_type, amount):
        """
        Creates an invoice object based on the specified condition type.
        """
        if condition_type == "Responsible":
            return ResponsibleCondition(amount)
        elif condition_type == "Enrolled":
            return NonEnrolledCondition(amount)
        elif condition_type == "Exempt":
            return ExemptCondition(amount)
        else:
            raise ValueError("Invalid condition type")


if __name__ == "__main__":
    try:
        # Generate invoices for different tax conditions
        factura = ConditionFactory.create_condition("Responsible", 1000)
        print(factura.get_tax())

        factura = ConditionFactory.create_condition("Exempt", 1500)
        print(factura.get_tax())

        factura = ConditionFactory.create_condition("Enrolled", 2000)
        print(factura.get_tax())
    except ValueError as e:
        print("Error:", e)
