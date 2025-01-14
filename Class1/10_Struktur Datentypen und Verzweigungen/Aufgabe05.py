bewertung = 25


def note(bewertung):
    if bewertung < 25:
        print('F')
    elif 25 <= bewertung < 45:
        print('E')
    elif 45 <= bewertung < 50:
        print('D')
    elif 50 <= bewertung < 60:
        print('C')
    elif 60 <= bewertung < 80:
        print('B')
    else:
        print('A')


note(bewertung)
