class BankAccount:
    # Bank Account protected by a pin

    def __init__(self, pin):
        # Initial account balance is 0 and pin is 'pin'
        self.balance = 0
        self.pin = pin

    def _check_pin(self, pin):
        # Private method to check if the provided pin is correct
        return pin == self.pin

    def deposit(self, pin, amount):
        # Increment account balance by amount and return new balance
        if not self._check_pin(pin):
            return "Falsche PIN. Zugriff verweigert."
        self.balance += amount
        return f"Neuer Kontostand: {self.balance} CHF"

    def withdraw(self, pin, amount):
        # Decrement account balance by amount and return amount withdrawn
        if not self._check_pin(pin):
            return "Falsche PIN. Zugriff verweigert."
        if amount > self.balance:
            return "Nicht genügend Guthaben."
        self.balance -= amount
        return f"Betrag abgehoben: {amount} CHF"

    def get_balance(self, pin):
        # Return account balance
        if not self._check_pin(pin):
            return "Falsche PIN. Zugriff verweigert."
        return f"Kontostand: {self.balance} CHF"

    def change_pin(self, oldpin, newpin):
        # Change pin from oldpin to newpin
        if not self._check_pin(oldpin):
            return "Falsche PIN. Zugriff verweigert."
        self.pin = newpin
        return "PIN erfolgreich geändert."


class SavingsAccount(BankAccount):
    # Savings Account that earns interest

    def __init__(self, pin, zinssatz):
        super().__init__(pin)
        self.zinssatz = zinssatz  # Zinssatz als Dezimalzahl, z.B. 0.05 für 5 %

    def zinsen_hinzufuegen(self):
        # Erhöht das Guthaben um den Zinsbetrag
        zinsbetrag = self.balance * self.zinssatz
        self.balance += zinsbetrag
        return f"Zinsen hinzugefügt. Neuer Kontostand: {self.balance} CHF"


class FeeSavingsAccount(SavingsAccount):
    # FeeSavingsAccount that charges a fee for withdrawals

    def __init__(self, pin, zinssatz, gebuehr):
        super().__init__(pin, zinssatz)
        self.gebuehr = gebuehr  # Gebühr für Abhebungen

    def withdraw(self, pin, amount):
        # Decrement account balance by amount and fee and return amount withdrawn
        if not self._check_pin(pin):
            return "Falsche PIN. Zugriff verweigert."
        if amount + self.gebuehr > self.balance:
            return "Nicht genügend Guthaben für Abhebung und Gebühren."
        self.balance -= (amount + self.gebuehr)
        return f"Betrag abgehoben: {amount} CHF. Gebühr: {self.gebuehr} CHF. Verbleibender Kontostand: {self.balance} CHF"


print("Bankaccount:")
# Beispiel zur Verwendung der Klasse
konto = BankAccount(pin='1234')
print(konto.deposit('1234', 100))  # Einzahlung von 100 CHF
print(konto.get_balance('1234'))  # Abfrage des Kontostands
print(konto.withdraw('1234', 50))  # Abhebung von 50 CHF
print(konto.get_balance('1234'))  # Abfrage des Kontostands
print(konto.change_pin('1234', '4321'))  # Änderung der PIN
print(konto.get_balance('4321'))  # Abfrage des Kontostands
print("------------------------------------------")

print("Sparaccount:")
# Beispiel zur Verwendung der Klassen
spar_konto = SavingsAccount(pin='1234', zinssatz=0.05)
print(spar_konto.deposit('1234', 1000))  # Einzahlung von 1000 CHF
print(spar_konto.zinsen_hinzufuegen())  # Zinsen hinzufügen
print("------------------------------------------")

print("gebueren Sparaccount:")
gebuehren_konto = FeeSavingsAccount(pin='1234', zinssatz=0.05, gebuehr=5)
print(gebuehren_konto.deposit('1234', 1000))  # Einzahlung von 1000 CHF
print(gebuehren_konto.withdraw('1234', 100))  # Abhebung von 100 CHF mit Gebühr
