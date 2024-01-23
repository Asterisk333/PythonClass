def main():
    checkslut, numbers = None, None
    numberlist = []

    def validate_input(input):  # input has to be x-y
        return input.__contains__("-")

    def convert_to_list(convertable):  # split and append to nuberlist
        convertable = convertable.split("-")
        for number in convertable:
            numberlist.append(number)
        return numberlist

    while checkslut != 1:
        numbers = str(input("Der Zahlenbereich lautet: "))
        checkslut = validate_input(numbers)

    convert_to_list(numbers)

    for i in range(int(numberlist[0]), int(numberlist[1]) + 1):
        print(i, i ** 2)


if __name__ == '__main__':
    main()
