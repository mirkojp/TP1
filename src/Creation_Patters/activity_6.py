# Extienda el ejemplo del taller para prototipos de forma que genere 20
# anidamientos y que la carga simulada de procesamiento dure 2 segundos.
import copy
import time


class SelfReferencingEntity:
    """Class representing an entity that can reference itself."""

    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        """Set the parent reference for the entity."""
        self.parent = parent


class SomeComponent:
    """Class representing some component."""

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        """
        Initialize SomeComponent.

        Args:
            some_int (int): Some integer value.
            some_list_of_objects (list): List of objects.
            some_circular_ref (SelfReferencingEntity): Reference to a SelfReferencingEntity object.
        """
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """Create a shallow copy of the component."""
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the component."""
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


def create_nested_component(depth):
    """
    Create a nested component with the specified depth.

    Args:
        depth (int): Depth of nesting.

    Returns:
        SomeComponent: Nested SomeComponent object.
    """
    if depth <= 0:
        return SomeComponent(0, [], None)

    inner_component = create_nested_component(depth - 1)
    some_list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    inner_component.some_list_of_objects = some_list_of_objects
    inner_component.some_circular_ref = circular_ref
    circular_ref.set_parent(inner_component)
    return inner_component


def main():
    """Main function to create a nested component and measure processing time."""
    start_time = time.time()

    root_component = create_nested_component(20)

    processing_time = time.time() - start_time
    print(f"Processing time: {processing_time:.2f} seconds")


if __name__ == "__main__":
    main()
