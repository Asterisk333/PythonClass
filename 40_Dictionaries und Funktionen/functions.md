# Was ist eine Funktion?

Eine Funktion ist ein benannter Codeblock, der eine Aufgabe ausführt oder einen Wert zurückgibt.

# Wozu braucht man Funktionen in Python?

Manchmal muss man eine Aufgabe in einem Programm mehrfach ausführen. Und Sie wollen den Code für dieselbe Aufgabe nicht
an verschiedenen Stellen kopieren.

Dazu verpacken Sie den Code in eine Funktion und verwenden diese Funktion, um die Aufgabe auszuführen, wann immer Sie
sie brauchen.

Wenn Sie zum Beispiel einen Wert auf dem Bildschirm ausgeben wollen, müssen Sie die Funktion print() aufrufen. Hinter
den Kulissen führt Python den Code in der Funktion print() aus, um einen Wert auf dem Bildschirm anzuzeigen.

In der Praxis verwenden Sie Funktionen, um ein umfangreiches Programm in kleinere und besser handhabbare Teile
aufzuteilen. Die Funktionen machen Ihr Programm einfacher zu entwickeln, zu lesen, zu testen und zu warten.

Die Funktion print() ist eine von vielen eingebauten Funktionen in Python. Das bedeutet, dass diese Funktionen überall
im Programm verfügbar sind.

In diesem Lernprogramm lernen Sie, wie Sie benutzerdefinierte Python-Funktionen definieren können.

```
def greet():
# Display a greeting to users 
    print('Hi')
 ```

Eine Funktionsdefinition beginnt mit dem Schlüsselwort def und dem Namen der Funktion (greet).

Wenn die Funktion einige Informationen benötigt, um ihre Aufgabe zu erfüllen, müssen Sie diese innerhalb der Klammern ()
angeben. Die Funktion greet in diesem Beispiel benötigt keine Informationen, daher sind die Klammern leer.

Die Funktionsdefinition endet immer mit einem Doppelpunkt (lächelnd.

Alle eingerückten Zeilen, die auf die Funktionsdefinition folgen, bilden den Körper der Funktion.

Die von dreifachen Anführungszeichen umgebene Textzeichenfolge wird als docstring bezeichnet. Er beschreibt, was die
Funktion tut. Python verwendet den docstring, um automatisch eine Dokumentation für die Funktion zu erstellen.

Die Zeile print('Hallo') ist die einzige Zeile mit tatsächlichem Code im Funktionsrumpf. Die Funktion greet() erledigt
eine Aufgabe: print('Hallo').

Wenn Sie eine Funktion verwenden möchten, müssen Sie sie aufrufen. Ein Funktionsaufruf weist Python an, den Code
innerhalb der Funktion auszuführen.

Um eine Funktion aufzurufen, schreiben Sie den Namen der Funktion, gefolgt von den Informationen, die die Funktion
benötigt, in Klammern.

Das folgende Beispiel ruft die Funktion greet() auf. Da die Funktion greet() keine Informationen benötigt, müssen Sie
leere Klammern wie diese angeben:

```
greet()
```

Angenommen, Sie möchten die Benutzer mit ihrem Namen begrüßen. Dazu müssen Sie einen Namen in Klammern der
Funktionsdefinition wie folgt angeben:

```
def greet(name):
    print(f"Hi {name}")
```

Manchmal werden die Begriffe Parameter und Argumente synonym verwendet. Es ist wichtig, zwischen den Parametern und
Argumenten einer Funktion zu unterscheiden.

Ein Parameter ist eine Information, die eine Funktion benötigt. Und Sie geben den Parameter in der Funktionsdefinition
an. Zum Beispiel hat die Funktion greet() einen Parameter namens name.

Ein Argument ist ein Teil der Daten, die Sie an die Funktion übergeben. Zum Beispiel ist die Zeichenkette 'John' oder
die Variable jane das Argument der Funktion.

Eine Funktion kann eine Aufgabe erfüllen, wie die Funktion greet(). Oder sie kann einen Wert zurückgeben. Der Wert, den
eine Funktion zurückgibt, wird als Rückgabewert bezeichnet.

Um einen Wert aus einer Funktion zurückzugeben, verwenden Sie die return-Anweisung innerhalb des Funktionskörpers.

```
def greet(name):
    return f"Hi {name}"
```

Eine Funktion kann null, einen oder mehrere Parameter haben.

Das folgende Beispiel definiert eine Funktion namens sum(), die die Summe von zwei Zahlen berechnet:

```
def sum(a, b):
    return a + b

total = sum(10,20)
print(total)
```