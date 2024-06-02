import json
import sys


def print_help():
    help_message = """
    Extractor de token para acceso API Servicios Banco XXX (versión 1.0)

    Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.

    Uso:
        {path ejecutable}/getJason-3.6v1.0.py {path archivo JSON}/{nombre archivo JSON}.json {jsonkey}

    Ejemplo:
        ./getJason-3.6v1.0.py ./sitedata.json access_token

    El token podrá recuperarse mediante el standard output de ejecución en el formato:

       {1.0}XXXX-XXXX-XXXX-XXXX

    Para obtener este mensaje de ayuda, ejecute:
       ./getJason-3.6v1.0.py -h

    Excepciones:
    Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
    terminar.
    """
    print(help_message)


def main():
    if len(sys.argv) != 3:
        if len(sys.argv) == 2 and sys.argv[1] == "-h":
            print_help()
        else:
            print("Error: Número incorrecto de argumentos.")
            print("Use -h para obtener ayuda.")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    try:
        with open(jsonfile, "r") as myfile:
            data = myfile.read()

        obj = json.loads(data)

        if jsonkey in obj:
            print(f"{{1.0}}{obj[jsonkey]}")
        else:
            print(f"Error: La clave '{jsonkey}' no se encuentra en el archivo JSON.")
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


if __name__ == "__main__":
    main()
