# Extractor de Token para Acceso API Servicios Banco XXX
**Versión 1.2**  
© UADER-FCyT-IS2 2024 Todos los derechos reservados

## Descripción
Este proyecto proporciona una herramienta para extraer tokens y realizar pagos utilizando un archivo JSON. Está implementado en Python y utiliza un patrón de diseño Singleton para garantizar que solo una instancia de la clase `TokenExtractor` exista en todo momento.

## Características
- **Extracción de tokens**: Realiza pagos deductivos de 500 unidades desde las cuentas con saldo suficiente en el archivo JSON proporcionado.
- **Singleton Pattern**: Garantiza que solo una instancia de `TokenExtractor` está activa.
- **Comandos**: Proporciona varios comandos para interactuar con la aplicación.
- **Persistencia**: Guarda y carga los pagos realizados en un archivo `payments.json`.


## Ejecución Básica
- Para procesar un archivo JSON:
    ```bash
    python getJason-3.10v1.2.py ./sitedata-ri.json
    ```
- Para obtener el mensaje de ayuda:
    ```bash
    python getJason-3.10v1.2.py -h
    ```
- Para obtener la versión del programa:
    ```bash
    python getJason-3.10v1.2.py -v
    ```
- Para listar los pagos realizados:
    ```bash
    python getJason-3.10v1.2.py -lp
    ```

## Comandos
- `-h`: Muestra el mensaje de ayuda.
- `-v`: Muestra la versión del programa.
- `-lp`: Lista los pagos realizados.

## Excepciones
Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de terminar.

## Archivos
- **sitedata-ri.json**: Archivo JSON de entrada con las cuentas y sus balances.
- **payments.json**: Archivo JSON donde se almacenan los pagos realizados.

## Código

### Clase `TokenExtractor`

#### Descripción
Clase principal que maneja la extracción de tokens y la gestión de pagos. Implementa el patrón Singleton para asegurar que solo una instancia esté activa.

#### Métodos
- `__init__(self)`: Constructor privado para evitar la instanciación directa.
- `get_instance()`: Método estático para obtener la instancia única (Singleton).
- `print_help()`: Devuelve el mensaje de ayuda del programa.
- `print_version()`: Devuelve la versión del programa.
- `load_payments()`: Carga los pagos realizados desde un archivo JSON.
- `save_payments()`: Guarda los pagos realizados en un archivo JSON.
- `get_json(self, jsonfile)`: Extrae el token, realiza el pago y actualiza el archivo JSON.
- `create_iterator()`: Crea un iterador para la lista de pagos.
- `list_payments()`: Lista todos los pagos realizados en orden cronológico.

### Clase `PaymentIterator`

#### Descripción
Iterador para la lista de pagos realizados.

#### Métodos
- `__init__(self, payments)`: Constructor que inicializa el iterador con la lista de pagos.
- `__iter__(self)`: Devuelve el iterador.
- `__next__(self)`: Devuelve el siguiente pago en la lista.

### Clases `Command`

#### Descripción
Implementa el patrón Command para encapsular las acciones específicas.

- **GetJsonCommand**: Comando para ejecutar la extracción de tokens.
- **PrintHelpCommand**: Comando para imprimir la ayuda.
- **PrintVersionCommand**: Comando para imprimir la versión.
- **ListPaymentsCommand**: Comando para listar los pagos realizados.

### Clase `Invoker`

#### Descripción
Responsable de registrar y ejecutar comandos.

#### Métodos
- `__init__(self)`: Inicializa el invocador.
- `register(self, name, command)`: Registra un comando bajo un nombre específico.
- `execute(self, name)`: Ejecuta un comando bajo un nombre específico.

### Función `main()`

#### Descripción
Punto de entrada del script. Gestiona los argumentos de la línea de comandos y ejecuta los comandos correspondientes.