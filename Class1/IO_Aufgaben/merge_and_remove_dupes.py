# Implementiert ein Python-Programm, das mehrere Text-Files in einem einzelnen Text-File zusammenführt und dabei
# Duplikate Zeilen entfernt. Als Ergebnis soll ein neues Text-File entstehen, dass keine Duplikate Zeilen enthält (
# siehe auch Aufgabe 1).

import os


def merge_and_remove_duplicates(file_paths, output_file_path):
    unique_lines = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = ' '.join(line.split())
                if cleaned_line not in unique_lines:
                    unique_lines.append(cleaned_line)

    with open(output_file_path, 'w') as output_file:
        for line in unique_lines:
            output_file.write(line + '\n')


file_paths = ['./line.txt', './line2.txt']
output_file_path = 'merged_file.txt'

merge_and_remove_duplicates(file_paths, output_file_path)



