# Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
# dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
# de 10 mts. Genere una clase que represente a las láminas en forma genérica al
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
# patrón bridge en la solución).


class Laminator():
    def produce(self):
        pass

class ShortLaminator(Laminator):
    def produce(self):
        return "Produced 5 meter long"


class LongLaminator(Laminator):
    def produce(self):
        return "Produced 10 meter long"

class Sheets:
    def __init__(self,thick,width,laminator):
        self.thick = thick
        self.width = width
        self.laminator = laminator

    def produce_sheets(self):
        return f"Sheets: thick={self.thick} width={self.width} laminator={self.laminator.produce()}"

if __name__ == "__main__":
    
    shortlam =ShortLaminator()
    longlam = LongLaminator()

    ss = Sheets(0.5,1.5,shortlam)
    sl = Sheets(0.5, 1.5, longlam)

    print(ss.produce_sheets())
    print(sl.produce_sheets())
