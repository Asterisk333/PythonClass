# Es sei ein Text-File vorgegeben. Das File könnt Ihr selber erstellen. Implementiert ein Python Programm, dass in der
# Lage ist Duplikate-Zeilen zu zählen und auszugeben. Ihr könnt in einem ersten Schritt zwei Zeilen mit == auf
# Gleichheit überprüfen. In einem zweiten Schritt solltet Ihr die Leerzeichen entfernen und nur die Wörter überprüfen.
# Dazu könnt Ihr die Methode split verwenden

def count_dupes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_count = {}
    for line in lines:
        words = line.split()
        line = ' '.join(words)

    for line in lines:
        if line in line_count:
            line_count[line] += 1
        else:
            line_count[line] = 1

    for line, count in line_count.items():
        if count > 1:
            print(f"Die Zeile '{line}' erscheint {count} Mal im File.")


# Pfad zur Textdatei
file_path = './line.txt'
count_dupes(file_path)

