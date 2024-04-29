import os


class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:
            self.history.pop(0)
        return memento

    def undo(self, steps=1):
        if steps <= len(self.history):
            memento = self.history[-steps]
            self.file = memento.file
            self.content = memento.content
            print(f"Undo {steps} steps")
        else:
            print("No hay suficientes estados en el historial")


class FileWriterCaretaker:
    def __init__(self):
        self.history = []

    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer, steps=1):
        writer.undo(steps)


if __name__ == "__main__":
    os.system("cls")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("se invoca al <undo> para deshacer 2 pasos")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> para deshacer 3 pasos")
    caretaker.undo(writer, 3)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> para deshacer 1 paso")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print(
        "se invoca al <undo> para deshacer 4 pasos (intentará deshacer más de lo que tiene)"
    )
    caretaker.undo(writer, 4)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
