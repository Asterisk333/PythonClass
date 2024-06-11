import json

with open('book.json', 'r', encoding='utf-8') as file:
    book_info = json.load(file)

book_info['Anzahl der Seiten'] = 576

with open('book.json', 'w', encoding='utf-8') as file:
    json.dump(book_info, file, ensure_ascii=False, indent=4)

