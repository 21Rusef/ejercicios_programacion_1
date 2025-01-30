'''
Este programa cuenta la frecuencia de cada palabra en un archivo de texto dado.
Los resultados se imprimen en pantalla y se guardan en un archivo de salida.

Requerimientos:
- Debe ejecutarse desde la línea de comandos con un archivo de entrada como argumento.
- Debe manejar errores en la lectura del archivo.
- Debe calcular la frecuencia de palabras sin el uso de bibliotecas externas.
- Debe ser compatible con PEP8 y pasar `pylint` sin errores críticos.
'''

import sys
import time

def read_words_from_file(file_name):
    '''
    Lee un archivo de texto y extrae las palabras contenidas en él.
    Retorna una lista de palabras en minúsculas y maneja errores de lectura.
    '''
    words = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = ''.join(
                    char.lower() if char.isalnum() or char.isspace() else ' '
                    for char in line
                )
                words.extend(cleaned_line.split())
    except FileNotFoundError:
        print(f'Error: El archivo "{file_name}" no fue encontrado.')
        sys.exit(1)

    if not words:
        print('Error: No se encontraron palabras válidas en el archivo.')
        sys.exit(1)

    return words

def count_word_frequencies(words):
    '''
    Calcula la frecuencia de cada palabra en la lista dada.
    Retorna un diccionario con las palabras y su conteo.
    '''
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    # Función principal para correr el programa.

    if len(sys.argv) != 2:
        print('Uso correcto: python word_count.py fileWithData.txt')
        sys.exit(1)

    file_name = sys.argv[1]

    # Iniciar medición de tiempo
    start_time = time.time()

    # Leer palabras del archivo
    words = read_words_from_file(file_name)

    # Calcular frecuencias de palabras
    word_counts = count_word_frequencies(words)

    # Detener medición de tiempo
    elapsed_time = time.time() - start_time

    # Generar salida
    output_lines = [
        'Resultados de Conteo de Palabras:\n'
    ]
    for word, count in sorted(word_counts.items()):
        output_lines.append(f'Palabra: "{word}" - Frecuencia: {count}')

    output_lines.append(f'\nTiempo de ejecución: {elapsed_time:.4f} segundos\n')

    # Imprimir resultados en pantalla
    print('\n'.join(output_lines))

    # Guardar resultados en un archivo
    with open('WordCountResults.txt', 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(output_lines))

    print('Los resultados han sido guardados en "WordCountResults.txt".')

# Ejecutar el programa
if __name__ == '__main__':
    main()