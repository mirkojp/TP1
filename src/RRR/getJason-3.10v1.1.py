# Extractor de token para acceso API Servicios Banco XXX
# Versión 1.1
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados

import json
import sys


class TokenExtractor:
    _instance = None

    @staticmethod
    def get_instance():
        """Método estático para obtener la instancia única (Singleton)"""
        if TokenExtractor._instance is None:
            TokenExtractor()
        return TokenExtractor._instance

    def __init__(self):
        """Constructor privado para evitar instanciación directa"""
        if TokenExtractor._instance is not None:
            raise Exception(
                "Esta clase es un Singleton. Use get_instance() para obtener la instancia."
            )
        else:
            TokenExtractor._instance = self

    @staticmethod
    def print_help():
        """Imprime el mensaje de ayuda del programa"""
        help_message = """
        Extractor de token para acceso API Servicios Banco XXX (versión 1.1)

        Este programa permite extraer la clave de acceso API para utilizar los servicios del 
        Banco XXX.

        Uso:
            {path ejecutable}/getJason-3.6v1.1.py {path archivo JSON}/{nombre archivo JSON}.json {jsonkey}

        Ejemplo:
            ./getJason-3.6v1.1.py ./sitedata.json access_token

        El token podrá recuperarse mediante el standard output de ejecución en el formato:

           {1.0}XXXX-XXXX-XXXX-XXXX

        Para obtener este mensaje de ayuda, ejecute:
           ./getJason-3.6v1.1.py -h

        Para obtener la version, ejecute:
           ./getJason-3.6v1.1.py -v

        Excepciones:
        Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
        terminar.
        """
        print(help_message)

    @staticmethod
    def print_version():
        """Imprime version del programa"""
        version_message = """versión 1.1
        """
        print(version_message)
        
    def extract_token(self, jsonfile, jsonkey):
        """Extrae y muestra el token del archivo JSON proporcionado"""
        try:
            with open(jsonfile, "r") as myfile:
                data = myfile.read()

            obj = json.loads(data)

            if jsonkey in obj:
                print(f"{{1.0}}{obj[jsonkey]}")
            else:
                print(
                    f"Error: La clave '{jsonkey}' no se encuentra en el archivo JSON."
                )
                sys.exit(1)
        except FileNotFoundError:
            print(f"Error: El archivo '{jsonfile}' no existe.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{jsonfile}' no contiene un JSON válido.")
            sys.exit(1)
        except Exception as e:
            print(f"Error inesperado: {e}")
            sys.exit(1)
    

def main():
    """Función principal que maneja la ejecución del programa desde la línea de comandos"""
    if len(sys.argv) not in [2, 3]:
        print("Error: Número incorrecto de argumentos.")
        print("Use -h para obtener ayuda.")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "-h":
        TokenExtractor.get_instance().print_help()
        sys.exit(0)
    elif arg == "-v":
        TokenExtractor.get_instance().print_version()
        sys.exit(0)
    elif len(sys.argv) == 3:
        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]
        TokenExtractor.get_instance().extract_token(jsonfile, jsonkey)
    else:
        print("Error: Argumentos incorrectos.")
        print("Use -h para obtener ayuda.")
        sys.exit(1)


if __name__ == "__main__":
    main()
