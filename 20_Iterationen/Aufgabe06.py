def main():
    checkslut, numbers = None, None
    numberlist = []

    def validate_input(input):  # input has to be x-y
        if input.__contains__("-"):
            try:
                int(input.split("-")[0]) & int(input.split("-")[1])
            except:
                return False
            else:
                if int(input.split("-")[0]) <= int(input.split("-")[1]):  # validate the user input x is smaller than y
                    return 1

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
