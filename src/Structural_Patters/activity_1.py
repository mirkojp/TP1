import subprocess
from abc import ABC, abstractmethod


class PingSubject(ABC):

    @abstractmethod
    def execute(self, ip_address):
        pass
    
    def executefree(self, ip_address):
        result = subprocess.run(["ping", "-c","1","-n", "10", ip_address], stdout=subprocess.PIPE)
        print(result.stdout.decode("latin-1"))


class RealPing(PingSubject):

    def execute(self, ip_address):
        if ip_address.startswith("192."):
            result = subprocess.run(["ping", "-c", "1","-n","10", ip_address], stdout=subprocess.PIPE)
            print(result.stdout.decode("latin-1"))
        else:
            print("La ip debe comenzar con 192.")


class PingProxy(PingSubject):

    def __init__(self, real_ping=RealPing()):
        self.real_ping = real_ping

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.real_ping.executefree("www.google.com")
        else:
            self.real_ping.execute(ip_address)


def Client(subject: PingSubject, ip_address: str):
    try:
        if isinstance(subject, PingSubject):
            subject.execute(ip_address)
        else:
            print("El objeto no es una instancia de PingSubject.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")


if __name__ == "__main__":
    print("Probando con dirección IP que comienza con '192.'")
    real_ping = RealPing()
    proxy = PingProxy(real_ping)
    Client(proxy, "192.168.0.1")

    print("\nProbando con dirección IP que no comienza con '192.'")
    Client(proxy, "10.0.0.1")

    print("\nProbando con dirección IP especial '192.168.0.254'")
    Client(proxy, "192.168.0.254")
