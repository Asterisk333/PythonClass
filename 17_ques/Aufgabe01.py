class Stack:
    def __init__(self):
        self.liste = []

    def is_empty(self):
        return len(self.liste) == 0

    def push(self, daten):
        self.liste.append(daten)

    def pop(self):
        if not self.is_empty():
            return self.liste.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.liste[-1]
        return None

    def size(self):
        return len(self.liste)


# Beispiel zur Verwendung des Stacks
stapel = Stack()
stapel.push('Buch1')
stapel.push('Buch2')
stapel.push('Buch3')

print(stapel.is_empty())  # Gibt False zurück
print(stapel.pop())  # Gibt 'Buch3' zurück
print(stapel.pop())  # Gibt 'Buch2' zurück
print(stapel.peek())  # Gibt 'Buch1' zurück
print(stapel.pop())  # Gibt 'Buch1' zurück
print(stapel.is_empty())  # Gibt True zurück
