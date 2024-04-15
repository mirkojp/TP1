# Implemente una clase “factura” que tenga un importe correspondiente al total
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
# condición.

from abc import ABC, abstractmethod


class Bill(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def get_tax(self):
        pass


class ResponsibleCondition(Bill):
    def get_tax(self):
        return f"IVA Responsible - Amount ${self.amount}"


class NonEnrolledCondition(Bill):
    def get_tax(self):
        return f"IVA NonEnrolled - Amount ${self.amount}"


class ExemptCondition(Bill):
    def get_tax(self):
        return f"IVA Exempt - Amount ${self.amount}"


class ConditionFactory:
    @staticmethod
    def create_condition(condition_type, amount):
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
        factura = ConditionFactory.create_condition("Responsible", 1000)
        print(factura.get_tax())

        factura = ConditionFactory.create_condition("Exempt", 1500)
        print(factura.get_tax())

        factura = ConditionFactory.create_condition("Enrolled", 2000)
        print(factura.get_tax())
    except ValueError as e:
        print("Error:", e)
