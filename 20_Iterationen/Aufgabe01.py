def main():
    number, result, checkslut = None, None, None
    fakultaet, counter = 1, 1

    def validate_number_input(input):
        try:
            float(input)
            return 1
        except ValueError:
            return 0

    def convert_to_integer(convertable):
        return int(float(convertable))

    def print_sum(input):
        print("Das ergebnis lautet: ", str(input))

    while checkslut != 1:
        number = input("Bitte geben Sie eine Natuerliche Zahl an: ")
        checkslut = validate_number_input(number)

    number = convert_to_integer(number)

    while counter <= number:
        fakultaet = fakultaet * counter
        print(str(counter) + "! : " + str(fakultaet))
        counter += 1

    print_sum(fakultaet)


if __name__ == '__main__':
    main()
