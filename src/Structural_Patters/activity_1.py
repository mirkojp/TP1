# Provea una clase ping que luego de creada al ser invocada con un método
# “execute(string)” realice 10 intentos de ping a la dirección IP contenida en
# “string” (argumento pasado), la clase solo debe funcionar si la dirección IP
# provista comienza con “192.”. Provea un método executefree(string) que haga
# lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
# cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
# www.google.com usando el método executefree de ping y re-envie a execute
# de la clase ping en cualquier otro caso. (Modele la solución como un patrón
# proxy).import subprocess
from abc import ABC, abstractmethod
import subprocess

class PingSubject(ABC):
    """
    Abstract class defining the interface for executing ping operations.
    """

    @abstractmethod
    def execute(self, ip_address):
        """
        Executes a ping operation for the given IP address.

        Args:
            ip_address (str): The IP address to ping.
        """
        pass

    def executefree(self, ip_address):
        """
        Executes a ping operation with predefined parameters for the given IP address.

        Args:
            ip_address (str): The IP address to ping.
        """
        result = subprocess.run(
            ["ping", "-c", "1", "-n", "10", ip_address], stdout=subprocess.PIPE
        )
        print(result.stdout.decode("latin-1"))


class RealPing(PingSubject):
    """
    Concrete implementation of PingSubject for performing real ping operations.
    """

    def execute(self, ip_address):
        """
        Executes a ping operation for the given IP address.

        Args:
            ip_address (str): The IP address to ping.
        """
        if ip_address.startswith("192."):
            result = subprocess.run(
                ["ping", "-c", "1", "-n", "10", ip_address], stdout=subprocess.PIPE
            )
            print(result.stdout.decode("latin-1"))
        else:
            print("The IP address must start with '192.'")


class PingProxy(PingSubject):
    """
    Proxy class for controlling access to RealPing objects.
    """

    def __init__(self, real_ping=RealPing()):
        """
        Initializes the PingProxy with a RealPing object.

        Args:
            real_ping (PingSubject): The RealPing object to proxy.
        """
        self.real_ping = real_ping

    def execute(self, ip_address):
        """
        Executes a ping operation for the given IP address, possibly delegating to RealPing.

        Args:
            ip_address (str): The IP address to ping.
        """
        if ip_address == "192.168.0.254":
            self.real_ping.executefree("www.google.com")
        else:
            self.real_ping.execute(ip_address)


def Client(subject: PingSubject, ip_address: str):
    """
    Client function to test ping operations.

    Args:
        subject (PingSubject): The subject to perform the ping operation.
        ip_address (str): The IP address to ping.
    """
    try:
        if isinstance(subject, PingSubject):
            subject.execute(ip_address)
        else:
            print("The object is not an instance of PingSubject.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    print("Testing with IP address starting with '192.'")
    real_ping = RealPing()
    proxy = PingProxy(real_ping)
    Client(proxy, "192.168.0.1")

    print("\nTesting with IP address not starting with '192.'")
    Client(proxy, "10.0.0.1")

    print("\nTesting with special IP address '192.168.0.254'")
    Client(proxy, "192.168.0.254")
