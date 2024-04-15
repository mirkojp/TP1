# Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar
# para construir aviones en lugar de vehículos. Para simplificar suponga que un
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.

import os
# Class Director
class Director:
    __builder = None

    def set_builder(self, builder):
        """Set the builder for the director."""
        self.__builder = builder

    def get_airplane(self):
        """Construct an airplane using the set builder."""
        airplane = Airplane()

        # Build the airplane body
        body = self.__builder.get_body()
        airplane.set_body(body)

        # Build the airplane engines
        for _ in range(2):
            engine = self.__builder.get_engine()
            airplane.attach_engine(engine)

        # Build the airplane wings
        for _ in range(2):
            wing = self.__builder.get_wing()
            airplane.attach_wing(wing)

        # Build the airplane landing gear
        landing_gear = self.__builder.get_landing_gear()
        airplane.set_landing_gear(landing_gear)

        return airplane


# Class Airplane
class Airplane:
    def __init__(self):
        self.__engines = []
        self.__wings = []
        self.__body = None
        self.__landing_gear = None

    def set_body(self, body):
        """Set the body of the airplane."""
        self.__body = body

    def attach_engine(self, engine):
        """Attach an engine to the airplane."""
        self.__engines.append(engine)

    def attach_wing(self, wing):
        """Attach a wing to the airplane."""
        self.__wings.append(wing)

    def set_landing_gear(self, landing_gear):
        """Set the landing gear of the airplane."""
        self.__landing_gear = landing_gear

    def specification(self):
        """Print the specifications of the airplane."""
        print("Body: %s" % (self.__body.shape))
        print("Engines: %d" % (len(self.__engines)))
        print("Wings: %d" % (len(self.__wings)))
        print("Landing Gear: %s" % (self.__landing_gear.type))


# Generic Builder class
class Builder:
    def get_body(self):
        """Abstract method to get the body."""
        pass

    def get_engine(self):
        """Abstract method to get an engine."""
        pass

    def get_wing(self):
        """Abstract method to get a wing."""
        pass

    def get_landing_gear(self):
        """Abstract method to get the landing gear."""
        pass


# Specific Builder for airplanes
class AirplaneBuilder(Builder):
    def get_body(self):
        """Get the body for an airplane."""
        body = Body()
        body.shape = "Airplane"
        return body

    def get_engine(self):
        """Get an engine for an airplane."""
        engine = Engine()
        engine.horsepower = 10000  # Assume a specific horsepower for airplanes
        return engine

    def get_wing(self):
        """Get a wing for an airplane."""
        wing = Wing()
        wing.type = "Wing"
        return wing

    def get_landing_gear(self):
        """Get landing gear for an airplane."""
        landing_gear = LandingGear()
        landing_gear.type = "Landing Gear"
        return landing_gear


# Classes for generic airplane parts
class Body:
    shape = None


class Engine:
    horsepower = None


class Wing:
    type = None


class LandingGear:
    type = None


# Main function
def main():
    airplane_builder = AirplaneBuilder()
    director = Director()
    director.set_builder(airplane_builder)
    airplane = director.get_airplane()
    airplane.specification()


# Main entry point
if __name__ == "__main__":
    import os
    os.system("clear")
    print("Example of a Builder pattern applied to airplane construction\n")
    main()
