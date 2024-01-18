def main():
    hourlyRate, workingHours, weekDay, checkSlut, total = None, None, None, None, None
    weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

    def validate_number_input(input):
        try:
            float(input)
            return 1
        except ValueError:
            return 0

    def validate_text_input(input):
        for weekday in weekdays:
            if input == weekday:
                return 1

    def print_sum(input):
        print("Das ergebnis lautet: ", str(input))

    def clean_slut():
        return 0

    while checkSlut != 1:
        hourlyRate = input("Bitte geben Sie Ihren Stundenlohn an: ")
        checkSlut = validate_number_input(hourlyRate)

    checkSlut = clean_slut()

    while checkSlut != 1:
        workingHours = input("Bitte geben Sie Ihre Tagestunden an: ")
        checkSlut = validate_number_input(workingHours)

    checkSlut = clean_slut()

    while checkSlut != 1:
        weekDay = input("Bitte geben Sie den Arbeitstag an: ")
        checkSlut = validate_text_input(weekDay)

    if weekDay == weekdays[6]:  # Sonntag
        print_sum((float(hourlyRate) * 2) * float(workingHours))
    else:
        print_sum(float(hourlyRate) * float(workingHours))


if __name__ == '__main__':
    main()
