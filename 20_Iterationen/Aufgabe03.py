def main():
    checkslut, numbers = None, None
    output = 0
    numberlist = []

    def validate_input(input):  # input has to be x-y
        return input.__contains__("-")

    def convert_to_list(convertable):  # split and append to nuberlist
        convertable = convertable.split("-")
        for number in convertable:
            numberlist.append(number)
        return numberlist

    def print_output(input):
        print("Das ergebnis lautet: ", str(input))

    while checkslut != 1:
        numbers = str(input("Der Zahlenbereich lautet: "))
        checkslut = validate_input(numbers)

    convert_to_list(numbers)

    for i in range(int(numberlist[0]), int(numberlist[1]) + 1):
        output += i ** 2

    print_output(output)


if __name__ == '__main__':
    main()
