'''
compute_statistics.py

Este programa calcula estadísticas descriptivas (media, mediana, moda,
desviación estándar y varianza) a partir de un archivo de texto que
contiene una lista de números. Los resultados se imprimen en pantalla 
y se guardan en un archivo de salida.

Requerimientos:
- Debe ejecutarse desde la línea de comandos con un archivo de entrada (ambos como argumentos).
- Debe manejar errores en la lectura del archivo.
- Debe calcular las estadísticas sin el uso de bibliotecas de terceros para cálculos.
- Debe ser compatible con PEP8 y pasar `pylint` sin errores críticos.
'''

import sys  # Librería para tomar los argumentos pasados al ejecutar el programa en terminal.
import time


def read_numbers_from_file(file_name):
    '''
    Lee un archivo de texto y extrae los números contenidos en él.
    Retorna una lista de números y maneja errores de lectura.
    '''
    numbers = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    num = float(line.strip())  # Numero en float y elimina espacios innecesarios.
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


def calculate_mean(data):
    ''' Calcula la media aritmética '''
    return sum(data) / len(data)


def calculate_median(data):
    ''' Calcula la mediana '''
    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    mid = num_elements // 2
    if num_elements % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def calculate_mode(data):
    ''' Calcula la moda '''
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    mode_values = [num for num, count in frequency.items() if count == max_count]
    return mode_values if len(mode_values) > 1 else mode_values[0]


def calculate_variance(data, mean_value):
    ''' Calcula la varianza '''
    return sum((x - mean_value) ** 2 for x in data) / len(data)


def calculate_standard_deviation(variance_value):
    ''' Calcula la desviación estándar '''
    return variance_value ** 0.5


def main():
    '''
    Función principal para ejecutar el programa.
    Lee el archivo de entrada, calcula estadísticas y guarda los resultados.
    '''
    if len(sys.argv) != 2:  # Ambos argumentos para el programa.
        print('Uso correcto: python compute_statistics.py fileWithData.txt')
        sys.exit(1)

    file_name = sys.argv[1]

    # Iniciar medición de tiempo
    start_time = time.time()

    # Leer números del archivo
    numbers = read_numbers_from_file(file_name)

    # Calcular estadísticas
    mean_value = calculate_mean(numbers)
    median_value = calculate_median(numbers)
    mode_value = calculate_mode(numbers)
    variance_value = calculate_variance(numbers, mean_value)
    std_dev_value = calculate_standard_deviation(variance_value)

    # Detener medición de tiempo
    elapsed_time = time.time() - start_time

    # Generar salida
    output_text = (
        'Resultados de Estadísticas Descriptivas:\n'
        f'Media: {mean_value}\n'
        f'Mediana: {median_value}\n'
        f'Moda: {mode_value}\n'
        f'Varianza: {variance_value}\n'
        f'Desviación Estándar: {std_dev_value}\n'
        f'Tiempo de ejecución: {elapsed_time:.4f} segundos\n'
    )

    # Imprimir resultados en terminal
    print(output_text)

    # Guardar resultados en un archivo
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output_text)

    print('Los resultados han sido guardados en "StatisticsResults.txt".')

# Ejecutar el programa
if __name__ == '__main__':
    main()
