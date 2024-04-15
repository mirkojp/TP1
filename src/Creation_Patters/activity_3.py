# Genere una clase donde se instancie una comida rápida “hamburguesa” que
# pueda ser entregada en mostrador, retirada por el cliente o enviada por
# delivery. A los efectos prácticos bastará que la clase imprima el método de
# entrega.

from abc import ABC, abstractmethod


class Hamburger:
    """
    Class representing a hamburger that can be delivered in different ways.
    """

    def __init__(self, tyype, delivery_strategy):
        self.tyype = tyype
        self.delivery_strategy = delivery_strategy

    def deliver(self):
        """
        Method to deliver the hamburger using the specified delivery strategy.
        """
        self.delivery_strategy.handit()


class DeliveryStrategy(ABC):
    """
    Abstract base class defining the interface for delivery strategies.
    """

    @abstractmethod
    def handit(self):
        """
        Abstract method to be implemented by concrete delivery strategies.
        """
        pass


class DeliveryStore(DeliveryStrategy):
    """
    Concrete delivery strategy for delivering to the store.
    """

    def handit(self):
        print("Delivered in store")


class DeliveryClient(DeliveryStrategy):
    """
    Concrete delivery strategy for delivering to the client.
    """

    def handit(self):
        print("Delivered by the client")


class DeliveryGuy(DeliveryStrategy):
    """
    Concrete delivery strategy for delivering by a delivery person.
    """

    def handit(self):
        print("Delivered by delivery man")


class DeliveryFactory:
    """
    Factory class for creating delivery strategy objects.
    """

    @staticmethod
    def create_delivery_strategy(strategy_type):
        """
        Creates a delivery strategy object based on the specified type.
        """
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
        # Create hamburger and deliver using different strategies
        hamburger = Hamburger(
            "Simple", DeliveryFactory.create_delivery_strategy("store")
        )
        hamburger.deliver()

        hamburger = Hamburger(
            "Simple", DeliveryFactory.create_delivery_strategy("client")
        )
        hamburger.deliver()

        hamburger = Hamburger("Simple", DeliveryFactory.create_delivery_strategy("guy"))
        hamburger.deliver()
    except ValueError as e:
        print("Error:", e)
