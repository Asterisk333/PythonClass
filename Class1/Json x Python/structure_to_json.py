import json

book_data = {
    "titel": "Der Goldene Kompass",
    "autor": "Philip Pullman",
    "jahr": "1995",
    "iban": "DE19 6709 2300 0033 1448 57",
    "verfuegbarkeit": 1
}

book_json = json.dumps(book_data, ensure_ascii=False, indent=4)

with open('book.json', 'w', encoding='utf-8') as file:
    file.write(book_json)
