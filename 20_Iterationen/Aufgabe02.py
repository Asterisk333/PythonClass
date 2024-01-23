def main():
    word, checkSlut, length = None, None, None
    drow= ""
    letterlist = []

    def validate_text_input(input):
        try:
            float(input) #if convertable its A nbr we just want str
            return 0
        except ValueError:
            return 1

    def convert_to_list(convertable):
        for letter in convertable:
            letterlist.append(letter)
        return letterlist

    def print_sum(input):
        print("Die invertierte Zeichenkette lautet: ", str(input))

    while checkSlut != 1:
        word = input("Bitte geben Sie eine Zeichenkette ein: ")
        checkSlut = validate_text_input(word)

    length = len(word)
    convert_to_list(word)

    while length > 0:
        drow = drow + (letterlist[length - 1])
        length -= 1

    print_sum(drow)


if __name__ == '__main__':
    main()
