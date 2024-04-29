from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: int) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: int) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        else:
            return "Number not consumed."


class PrimeHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        if self.is_prime(request):
            return f"PrimeHandler: Consumed prime number {request}"
        else:
            return super().handle(request)

    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True


class EvenHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        if self.is_even(request):
            return f"EvenHandler: Consumed even number {request}"
        else:
            return super().handle(request)

    def is_even(self, num: int) -> bool:
        return num % 2 == 0


def client_code(handler: Handler) -> None:
    for num in range(1, 101):
        print(handler.handle(num))


if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    prime_handler.set_next(even_handler)

    print("Chain: PrimeHandler > EvenHandler\n")
    client_code(prime_handler)
