import xml.etree.ElementTree as ET


def filter_books(file, filter_age):
    tree = ET.parse(file)
    root = tree.getroot()
    titles = []

    for book in root.findall('book'):
        author_age = int(book.find('age').text)
        if author_age > filter_age:
            titles.append(book.find('title').text)

    return titles


# call
filename = 'books.xml'
filter_age = 50
books = filter_books(filename, filter_age)
print(books)
