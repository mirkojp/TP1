import os


# Clase Director
class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_airplane(self):
        airplane = Airplane()

        # Construye el cuerpo del avión
        body = self.__builder.get_body()
        airplane.set_body(body)

        # Construye las turbinas del avión
        for _ in range(2):
            engine = self.__builder.get_engine()
            airplane.attach_engine(engine)

        # Construye las alas del avión
        for _ in range(2):
            wing = self.__builder.get_wing()
            airplane.attach_wing(wing)

        # Construye el tren de aterrizaje del avión
        landing_gear = self.__builder.get_landing_gear()
        airplane.set_landing_gear(landing_gear)

        return airplane


# Clase Avión
class Airplane:
    def __init__(self):
        self.__engines = []
        self.__wings = []
        self.__body = None
        self.__landing_gear = None

    def set_body(self, body):
        self.__body = body

    def attach_engine(self, engine):
        self.__engines.append(engine)

    def attach_wing(self, wing):
        self.__wings.append(wing)

    def set_landing_gear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Cuerpo: %s" % (self.__body.shape))
        print("Turbinas: %d" % (len(self.__engines)))
        print("Alas: %d" % (len(self.__wings)))
        print("Tren de aterrizaje: %s" % (self.__landing_gear.type))


# Clase Builder genérica
class Builder:
    def get_body(self):
        pass

    def get_engine(self):
        pass

    def get_wing(self):
        pass

    def get_landing_gear(self):
        pass


# Builder específico para aviones
class AirplaneBuilder(Builder):
    def get_body(self):
        body = Body()
        body.shape = "Avión"
        return body

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 10000  # Suponga una potencia específica para aviones
        return engine

    def get_wing(self):
        wing = Wing()
        wing.type = "Ala"
        return wing

    def get_landing_gear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Tren de aterrizaje"
        return landing_gear


# Clases para partes genéricas de aviones
class Body:
    shape = None


class Engine:
    horsepower = None


class Wing:
    type = None


class LandingGear:
    type = None


# Función principal
def main():
    airplane_builder = AirplaneBuilder()
    director = Director()
    director.set_builder(airplane_builder)
    airplane = director.get_airplane()
    airplane.specification()


# Punto de entrada principal
if __name__ == "__main__":
    os.system("clear")
    print("Ejemplo de un patrón Builder aplicado a la construcción de aviones\n")
    main()
