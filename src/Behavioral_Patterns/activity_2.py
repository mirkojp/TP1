from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class StringIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """

    def __init__(self, collection: str, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self) -> str:
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        if self._position < 0 or self._position >= len(self._collection):
            raise StopIteration()

        current_char = self._collection[self._position]

        if self._reverse:
            self._position -= 1
        else:
            self._position += 1

        return current_char


class StringCollection(Iterable):
    """
    Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """

    def __init__(self, collection: str) -> None:
        self._collection = collection

    def __iter__(self) -> StringIterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """
        return StringIterator(self._collection)

    def get_reverse_iterator(self) -> StringIterator:
        return StringIterator(self._collection, reverse=True)


if __name__ == "__main__":
    # The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.
    collection = StringCollection("Example")

    print("Straight traversal:")
    print("".join(collection))
    print("")

    print("Reverse traversal:")
    print("".join(collection.get_reverse_iterator()))
