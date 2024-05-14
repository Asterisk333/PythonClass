# Schreiben Sie ein Python-Skript, das den Inhalt einer Textdatei namens "input.txt" liest und in eine neue Datei
# namens "output.txt" schreibt, wobei alle Zeilen umgekehrt werden. Zum Beispiel sollte die Zeile "Hallo Welt!" in
# der Datei "output.txt" als "!tleW ollaH" geschrieben werden.


def reverse_lines(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
            open(output_file_path, 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()

        for line in lines:
            output_file.write(line[::-1])


input_file_path = 'input.txt'
output_file_path = 'output.txt'

reverse_lines(input_file_path, output_file_path)
