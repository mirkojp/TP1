# Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
# dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
# de 10 mts. Genere una clase que represente a las láminas en forma genérica al
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
# patrón bridge en la solución).
class Laminator:
    """
    Abstract class representing a laminator.
    """

    def produce(self):
        """
        Abstract method to produce laminated sheets.
        """
        pass


class ShortLaminator(Laminator):
    """
    Concrete class representing a short laminator.
    """

    def produce(self):
        """
        Produces laminated sheets of 5-meter length.

        Returns:
            str: Description of the produced laminated sheets.
        """
        return "Produced 5 meter long"


class LongLaminator(Laminator):
    """
    Concrete class representing a long laminator.
    """

    def produce(self):
        """
        Produces laminated sheets of 10-meter length.

        Returns:
            str: Description of the produced laminated sheets.
        """
        return "Produced 10 meter long"


class Sheets:
    """
    Class representing a set of sheets to be laminated.
    """

    def __init__(self, thick, width, laminator):
        """
        Initializes a Sheets object.

        Args:
            thick (float): Thickness of the sheets.
            width (float): Width of the sheets.
            laminator (Laminator): Laminator object to use for lamination.
        """
        self.thick = thick
        self.width = width
        self.laminator = laminator

    def produce_sheets(self):
        """
        Produces laminated sheets.

        Returns:
            str: Description of the produced laminated sheets.
        """
        return f"Sheets: thick={self.thick} width={self.width} laminator={self.laminator.produce()}"


if __name__ == "__main__":
    # Create instances of ShortLaminator and LongLaminator
    shortlam = ShortLaminator()
    longlam = LongLaminator()

    # Create instances of Sheets with different laminators
    ss = Sheets(0.5, 1.5, shortlam)
    sl = Sheets(0.5, 1.5, longlam)

    # Print the descriptions of produced sheets
    print(ss.produce_sheets())
    print(sl.produce_sheets())
