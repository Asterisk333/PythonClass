# Dictionaries

Ein Python-Wörterbuch ist eine Sammlung von Schlüssel-Wert-Paaren, bei denen jeder Schlüssel mit einem Wert verknüpft
ist.

Ein Wert in einem Schlüssel-Wert-Paar kann eine Zahl, eine Zeichenkette, eine Liste, ein Tupel oder sogar ein anderes
Wörterbuch sein. Sie können einen Wert jedes in Python gültigen Typs als Wert in einem Schlüssel-Wert-Paar verwenden.

Ein Schlüssel im Schlüssel-Wert-Paar muss unveränderlich sein. Mit anderen Worten, der Schlüssel kann nicht geändert
werden, z. B. eine Zahl, eine Zeichenkette, ein Tupel usw.

Python verwendet geschweifte Klammern {}, um ein Wörterbuch zu definieren. Innerhalb der geschweiften Klammern können
Sie null, ein oder viele Schlüssel-Wert-Paare platzieren.

### Das folgende Beispiel definiert ein leeres Wörterbuch:

```
empty_dict = {}
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
```

Um auf einen Wert nach Schlüssel aus einem Wörterbuch zuzugreifen, können Sie die Notation in eckigen Klammern oder die
Methode get() verwenden.

```
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
print(person['first_name'])
print(person['last_name'])
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
ssn = person.get('ssn')
print(ssn)
```

Wenn der Schlüssel nicht existiert, gibt die Methode get() den Wert None zurück, anstatt einen KeyError auszulösen.
Beachten Sie, dass None bedeutet, dass kein Wert existiert.

Die Methode get() gibt auch einen Standardwert zurück, wenn der Schlüssel nicht existiert, indem sie den Standardwert an
ihr zweites Argument übergibt.

Das folgende Beispiel gibt die Zeichenkette '000-00-0000' zurück, wenn der Schlüssel ssn nicht im Personenwörterbuch
vorhanden ist:

```
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
ssn = person.get('ssn', '000-00-0000')
print(ssn)
```

Da ein Wörterbuch eine dynamische Struktur hat, können Sie ihm jederzeit neue Schlüssel-Wert-Paare hinzufügen.

Um ein neues Schlüssel-Wert-Paar zu einem Wörterbuch hinzuzufügen, geben Sie den Namen des Wörterbuchs gefolgt von dem
neuen Schlüssel in eckigen Klammern zusammen mit dem neuen Wert an.

### Das folgende Beispiel fügt dem Personen-Wörterbuch ein neues Schlüssel-Wert-Paar hinzu:

```
person['gender'] = 'Female'
```  

Um ein Schlüssel-Wert-Paar anhand eines Schlüssels zu entfernen, verwenden Sie die Anweisung del:

```
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
del person['active']
print(person)
```

Das Python-Wörterbuch bietet eine Methode namens items(), die ein Objekt zurückgibt, das eine Liste von
Schlüssel-Wert-Paaren als Tupel in einer Liste enthält.

```
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
for key, value in person.items():
    print(f"{key}: {value}")
 ```

Manchmal möchte man einfach eine Schleife durch alle Schlüssel in einem Wörterbuch ziehen. In diesem Fall können Sie
eine for-Schleife mit der Methode keys() verwenden.

Die Methode keys() gibt ein Objekt zurück, das eine Liste der Schlüssel des Wörterbuchs enthält.

Zum Beispiel:

```
person = {  
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
for key in person.keys():
    print(key)
 ```

Die Methode values() gibt eine Liste von Werten ohne Schlüssel zurück.

Um eine Schleife durch alle Werte in einem Wörterbuch zu ziehen, verwenden Sie eine for-Schleife mit der Methode
values():

```
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
for value in person.values():
 print(value)
 ```