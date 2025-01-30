'''
Este programa convierte números enteros de un archivo de texto a bases binarias y hexadecimales.
Los resultados se imprimen en pantalla y se guardan en un archivo de salida.

Requerimientos:
- Debe ejecutarse desde la línea de comandos con un archivo de entrada como argumento.
- Debe manejar errores en la lectura del archivo.
- Debe calcular conversiones sin usar funciones o bibliotecas estándar para conversiones numéricas.
- Debe ser compatible con PEP8 y pasar `pylint` sin errores críticos.
'''

import sys
import time

def read_numbers_from_file(file_name):
    '''
    Lee un archivo de texto y extrae los números enteros contenidos en él.
    Retorna una lista de números y maneja errores de lectura.
    Función parecida al problema 1.
    '''
    numbers = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Convierte el número en entero y elimina espacios innecesarios.
                    num = int(line.strip())
                    numbers.append(num)
                except ValueError:
                    print(f'Advertencia: "{line.strip()}" no es un número válido y será ignorado.')
    except FileNotFoundError:
        print(f'Error: El archivo "{file_name}" no fue encontrado.')
        sys.exit(1)

    if not numbers:
        print('Error: No se encontraron números válidos en el archivo.')
        sys.exit(1)

    return numbers

def convert_to_binary(number):
    ''' Convierte un número entero a binario manualmente. '''
    if number == 0:
        return '0'
    binary = ''
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2
    return binary

def convert_to_hexadecimal(number):
    ''' Convierte un número entero a hexadecimal manualmente. '''
    if number == 0:
        return '0'
    hex_digits = '0123456789ABCDEF'
    hexadecimal = ''
    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number //= 16
    return hexadecimal

def main():
    '''
    Principal. Lee el archivo de entrada, 
    convierte los números a binario y hexadecimal, y guarda los resultados.
    '''
    if len(sys.argv) != 2:  # Confirma que el usuario ingrese un argumento válido.
        print('Uso correcto: python convert_numbers.py fileWithData.txt')
        sys.exit(1)

    file_name = sys.argv[1]

    # Iniciar medición de tiempo
    start_time = time.time()

    # Leer números del archivo
    numbers = read_numbers_from_file(file_name)

    # Generar conversiones
    conversion_results = []
    for num in numbers:
        binary_value = convert_to_binary(num)
        hex_value = convert_to_hexadecimal(num)
        conversion_results.append(
            f'Número: {num}, Binario: {binary_value}, '
            f'Hexadecimal: {hex_value}'
        )

    # Detener medición de tiempo
    elapsed_time = time.time() - start_time

    # Generar salida
    time_text = f'\nTiempo de ejecución: {elapsed_time:.4f} segundos\n'
    output_text = '\n'.join(conversion_results) + time_text
    # Imprimir resultados en terminal
    print(output_text)

    # Guardar resultados en un archivo
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output_text)

    print('Los resultados han sido guardados en "ConvertionResults.txt".')

# Ejecutar el programa
if __name__ == '__main__':
    main()
