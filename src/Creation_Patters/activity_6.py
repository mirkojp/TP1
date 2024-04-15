import copy
import time


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


def create_nested_component(depth):
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
    start_time = time.time()

    root_component = create_nested_component(20)

    processing_time = time.time() - start_time
    print(f"Processing time: {processing_time:.2f} seconds")


if __name__ == "__main__":
    main()
