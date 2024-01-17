def main():
    checkSlut = None
    validOperators = ["ddieren", "subtrahieren", "multiplizieren"]


    def clean_slut(checkSlut):
        checkSlut = 0
        return checkSlut

    def validate_number_input(input):
        return int(input.isdigit())

    def validate_text_input(input):
        for validOperator in validOperators:
            if input == validOperator:
                return not int(input.isdigit())

    def print_sum(input):
        print("Das erebnss lautet: ", str(input))

    while checkSlut != 1:
        num1 = input("Bitte geben sie die erste Nummer ein: ")
        checkSlut = validate_number_input(num1)

    checkSlut = clean_slut(checkSlut)

    while checkSlut != 1:
        num2 = input("Bitte geben sie die zweite Nummer ein: ")
        checkSlut = validate_number_input(num2)

    checkSlut = clean_slut(checkSlut)

    while checkSlut != 1:
        operator = input("Bitte geben sie den gwuenschten Operator ein: ")
        checkSlut = validate_text_input(operator)

    if operator == validOperators[0]:  # ddieren
        sum = float(num1) + float(num2)
        print_sum(sum)
    elif operator == validOperators[1]:  # subtrahieren
        sum = float(num1) - float(num2)
        print_sum(sum)
    elif operator == validOperators[2]:  # multiplizieren
        sum = float(num1) * float(num2)
        print_sum(sum)


if __name__ == "__main__":
    main()
