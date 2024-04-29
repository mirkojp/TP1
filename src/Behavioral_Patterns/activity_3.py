from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from string import ascii_uppercase
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self, id: str) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, id: str) -> None:
        print(f"\nSubject: Notifying observers for ID {id}...")
        for observer in self._observers:
            observer.update(id)


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, id: str) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    _id = "NJHR"

    def update(self, id: str) -> None:
        if id == self._id:
            print(f"ConcreteObserverA: Reacted to the event for ID {id}")


class ConcreteObserverB(Observer):
    _id = "MIMU"

    def update(self, id: str) -> None:
        if id == self._id:
            print(f"ConcreteObserverB: Reacted to the event for ID {id}")


class ConcreteObserverC(Observer):
    _id = "EGHD"

    def update(self, id: str) -> None:
        if id == self._id:
            print(f"ConcreteObserverC: Reacted to the event for ID {id}")


class ConcreteObserverD(Observer):
    _id = "ANWE"

    def update(self, id: str) -> None:
        if id == self._id:
            print(f"ConcreteObserverD: Reacted to the event for ID {id}")


if __name__ == "__main__":
    # The client code.
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    # Emitir 8 ID asegurándose de que al menos cuatro de ellos coincidan con los ID para los que tengamos clases implementadas.
    ids = ["NJHR", "MIMU", "EGHD", "ANWE", "HVFS", "TWAS", "XOJB", "AJTJ"]
    for id in ids:
        subject.notify(id)
