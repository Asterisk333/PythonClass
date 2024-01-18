def main():
    checkSlut = None
    validOperators = ["addieren", "subtrahieren", "multiplizieren"]

    def clean_slut():
        return 0

    def validate_number_input(input):
        try:
            float(input)
            return 1
        except ValueError:
            return 0

    def validate_text_input(input):
        for validOperator in validOperators:
            if input == validOperator:
                return not int(input.isdigit())  # return turned true or false as we check for string and not int ++ left in cuz imo its cool

    def print_sum(input):
        print("Das ergebnis lautet: ", str(input))

    while checkSlut != 1:
        num1 = input("Bitte geben sie die erste Nummer ein: ")
        checkSlut = validate_number_input(num1)

    checkSlut = clean_slut()

    while checkSlut != 1:
        num2 = input("Bitte geben sie die zweite Nummer ein: ")
        checkSlut = validate_number_input(num2)

    checkSlut = clean_slut()

    while checkSlut != 1:
        operator = input("Bitte geben sie den gwuenschten Operator ein: ")
        checkSlut = validate_text_input(operator)

    if operator == validOperators[0]:  # addieren
        calculated = float(num1) + float(num2)
        print_sum(calculated)
    elif operator == validOperators[1]:  # subtrahieren
        calculated = float(num1) - float(num2)
        print_sum(calculated)
    elif operator == validOperators[2]:  # multiplizieren
        calculated = float(num1) * float(num2)
        print_sum(calculated)


if __name__ == "__main__":
    main()
