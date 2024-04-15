# Represente la lista de piezas componentes de un ensamblado con sus
# relaciones jerárquicas. Empiece con un producto principal formado por tres
# sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
# que representen esa configuración y la muestren. Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón
# composite).


class Component:
    def display(self, indent=0):
        pass


class Piece(Component):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print("  " * indent + f"• {self.name}")


class Assembly(Component):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def display(self, indent=0):
        print("  " * indent + f"Assembly: {self.name}")
        for component in self.components:
            component.display(indent + 1)


# Creating the main product
main_product = Assembly("Main Product")

# Sub-assemblies
subset1 = Assembly("Subset 1")
subset2 = Assembly("Subset 2")
subset3 = Assembly("Subset 3")

# Individual pieces
for i in range(1, 5):
    subset1.add_component(Piece(f"Piece {i} of Subset 1"))
    subset2.add_component(Piece(f"Piece {i} of Subset 2"))
    subset3.add_component(Piece(f"Piece {i} of Subset 3"))

# Adding subsets to the main product
main_product.add_component(subset1)
main_product.add_component(subset2)
main_product.add_component(subset3)

# Displaying the structure of the main product
main_product.display()

# Adding an additional optional subset
optional_subset = Assembly("Optional Subset")
for i in range(1, 5):
    optional_subset.add_component(Piece(f"Piece {i} of Optional Subset"))
main_product.add_component(optional_subset)

# Displaying the structure of the main product with the optional subset
print("\nAfter adding the optional subset:")
main_product.display()
