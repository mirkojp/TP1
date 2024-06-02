# Extractor de token para acceso API Servicios Banco XXX
# Versión 1.1
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados

# import json
# import sys

import json
import sys
import os

class TokenExtractor():
    _instance = None

    def __init__(self):
        """Constructor privado para evitar instanciación directa"""
        if TokenExtractor._instance is not None:
            raise Exception("Esta clase es un Singleton. Use get_instance() para obtener la instancia.")
        else:
            TokenExtractor._instance = self
            self.payments = self.load_payments()
            self.next_account_index = 0

    @staticmethod
    def get_instance():
        """Método estático para obtener la instancia única (Singleton)"""
        if TokenExtractor._instance is None:
            TokenExtractor()
        return TokenExtractor._instance

    @staticmethod
    def print_help():
        """Devuelve el mensaje de ayuda del programa"""
        help_message = """
        Extractor de token para acceso API Servicios Banco XXX (versión 1.2)

        Este programa toma un token y realiza pagos 

        Uso:
            {path ejecutable}/getJason-3.10v1.2.py {path archivo JSON}/{nombre archivo JSON}.json

        Ejemplo:
            ./getJason-3.10v1.2.py ./sitedata-ri.json

        Para obtener este mensaje de ayuda, ejecute:
           ./getJason-3.10v1.2.py -h

        Para obtener la version, ejecute:
           ./getJason-3.10v1.2.py -v

        Para listar los pagos realizados, ejecute:
           ./getJason-3.10v1.2.py -lp

        Excepciones:
        Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
        terminar.
        """
        return help_message

    @staticmethod
    def print_version():
        """Devuelve la versión del programa"""
        version_message = """versión 1.2"""
        return version_message

    def load_payments(self):
        """Carga los pagos realizados desde un archivo JSON"""
        if os.path.exists("payments.json"):
            with open("payments.json", "r") as file:
                return json.load(file)
        return []

    def save_payments(self):
        """Guarda los pagos realizados en un archivo JSON"""
        with open("payments.json", "w") as file:
            json.dump(self.payments, file, indent=4)

    def get_json(self, jsonfile):
        """Extrae el token según su monto, le resta 500, los carga en la lista de pagos, devuelve string """
        try:
            with open(jsonfile, "r") as myfile:
                data = myfile.read()

            obj = json.loads(data)
            accounts = list(obj.keys())

            while True:
                account = accounts[self.next_account_index]
                balance = obj[account]

                if balance >= 500:
                    obj[account] -= 500
                    self.payments.append(
                        {
                            "order": len(self.payments) + 1,
                            "account": account,
                            "amount": 500,
                            "remaining_balance": obj[account],
                        }
                    )
                    with open(jsonfile, "w") as file:
                        json.dump(obj, file, indent=4)

                    self.save_payments()

                    self.next_account_index = (self.next_account_index + 1) % len(
                        accounts
                    )
                    return f"Numero pedido: {len(self.payments)}, Cuenta: {account}, Monto: 500, Balance: {obj[account]}"

                self.next_account_index = (self.next_account_index + 1) % len(accounts)

                if self.next_account_index == 0:
                    return "No hay cuentas con saldo suficiente para realizar el pago."

        except FileNotFoundError:
            return f"Error: El archivo '{jsonfile}' no existe."
        except json.JSONDecodeError:
            return f"Error: El archivo '{jsonfile}' no contiene un JSON válido."
        except Exception as e:
            return f"Error inesperado: {e}"

    def create_iterator(self):
        """Crea un iterador para la lista de pagos"""
        return PaymentIterator(self.payments)

    def list_payments(self):
        """Lista todos los pagos realizados en orden cronológico"""
        iterator = self.create_iterator()
        payments_list = []
        for payment in iterator:
            payments_list.append(
                f"Pedido: {payment['order']}, Cuenta: {payment['account']}, Monto: {payment['amount']}, Balance restante: {payment['remaining_balance']}"
            )
        return (
            "\n".join(payments_list) if payments_list else "No se han realizado pagos."
        )


class PaymentIterator:
    def __init__(self, payments):
        self._payments = payments
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._payments):
            result = self._payments[self._index]
            self._index += 1
            return result
        raise StopIteration

class Command:
    """
    The Command interface declara un método para ejecutar un comando.
    """

    def execute(self):
        pass

class GetJsonCommand(Command):
    """
    Implementa la interfaz Command y encapsula la lógica específica de GetJson.
    """

    def __init__(self, receiver, jsonfile):
        self.receiver = receiver
        self.jsonfile = jsonfile

    def execute(self):
        return self.receiver.get_json(self.jsonfile)

class PrintHelpCommand(Command):
    """
    Implementa la interfaz Command y encapsula la lógica específica de PrintHelp.
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.print_help()

class PrintVersionCommand(Command):
    """
    Implementa la interfaz Command y encapsula la lógica específica de PrintVersion.
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.print_version()

class ListPaymentsCommand(Command):
    """
    Implementa la interfaz Command y encapsula la lógica específica de ListPayments.
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.list_payments()

class Invoker:
    """
    La clase Invoker es responsable de registrar y ejecutar comandos.
    """
    def __init__(self):
        self._commands = {}

    def register(self, name, command):
        """
        Registra un comando bajo un nombre especifico
        """
        self._commands[name] = command

    def execute(self, name):
        """
        Ejecuta un comando bajo un nombre especifico
        """
        if name in self._commands:
            return self._commands[name].execute()
        return "Command not found"

def main():
    if len(sys.argv) != 2:
        print("Error: Faltan ingresar argumentos")
        print("Use python ruta\\getJason-3.10v1.3.py -h para obtener ayuda.")
        sys.exit(1)

    Token_extractor = TokenExtractor().get_instance()
    command_or_file = sys.argv[1]

    # Creates command and invoker
    getjson_command = GetJsonCommand(Token_extractor, command_or_file)
    print_help_command = PrintHelpCommand(Token_extractor)
    print_version_command = PrintVersionCommand(Token_extractor)
    list_payments_command = ListPaymentsCommand(Token_extractor)

    invoker = Invoker()
    invoker.register("get_json", getjson_command)
    invoker.register("-h", print_help_command)
    invoker.register("-v", print_version_command)
    invoker.register("-lp", list_payments_command)

    # Executes, print result
    if command_or_file == "-h":
        result = invoker.execute("-h")
    elif command_or_file == "-v":
        result = invoker.execute("-v")
    elif command_or_file == "-lp":
        result = invoker.execute("-lp")
    else:
        result = invoker.execute("get_json")
    print(result)

if __name__ == "__main__":
    main()
