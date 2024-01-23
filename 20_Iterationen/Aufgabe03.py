def main():
    checkslut = None
    numberlist = []

    def validate_input(input):
        return input.__contains__("-")

    def convert_to_list(convertable):
        convertable = convertable.split("-")
        for number in convertable:
            numberlist.append(number)
        return numberlist

    while checkslut != 1:
        numbers = str(input("Der Zahlenbereich lautet: "))
        checkSlut = validate_input(numbers)

    convert_to_list(numbers)

    for i in range(int(numberlist[0]), int(numberlist[1])+1):
        print("Das Quadrat von", str(i), "ist", str(i ** 2))


if __name__ == '__main__':
    main()