# Genere una clase donde se instancie una comida rápida “hamburguesa” que
# pueda ser entregada en mostrador, retirada por el cliente o enviada por
# delivery. A los efectos prácticos bastará que la clase imprima el método de
# entrega.

from abc import ABC, abstractmethod

class Hamburger:
    def __init__(self, tyype, delivery_strategy):
        self.tyype = tyype
        self.delivery_strategy = delivery_strategy

    def deliver(self):
        self.delivery_strategy.handit()

class DeliveryStrategy(ABC):
    @abstractmethod
    def handit(self):
        pass

class DeliveryStore(DeliveryStrategy):
    def handit(self):
        print("Delivered in store")

class DeliveryClient(DeliveryStrategy):
    def handit(self):
        print("Delivered by the client")

class DeliveryGuy(DeliveryStrategy):
    def handit(self):
        print("Delivered by delivery man")

class DeliveryFactory:
    @staticmethod
    def create_delivery_strategy(strategy_type):
        if strategy_type == "store":
            return DeliveryStore()
        elif strategy_type == "client":
            return DeliveryClient()
        elif strategy_type == "guy":
            return DeliveryGuy()
        else:
            raise ValueError("Invalid delivery strategy")

if __name__ == "__main__":
    try:
        hamburger = Hamburger("Simple", DeliveryFactory.create_delivery_strategy("store"))
        hamburger.deliver()

        hamburger = Hamburger("Simple", DeliveryFactory.create_delivery_strategy("client"))
        hamburger.deliver()

        hamburger = Hamburger("Simple", DeliveryFactory.create_delivery_strategy("guy"))
        hamburger.deliver()
    except ValueError as e:
        print("Error:", e)