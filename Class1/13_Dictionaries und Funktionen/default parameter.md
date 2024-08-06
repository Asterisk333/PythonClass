# Default Parameter

Wenn Sie eine Funktion definieren, können Sie für jeden Parameter einen Standardwert angeben.

Um Standardwerte für Parameter anzugeben, verwenden Sie die folgende Syntax:

```
def function_name(param1, param2=value2, param3=value3, ...):
```

In dieser Syntax geben Sie mit dem Zuweisungsoperator (=) Standardwerte (value2, value3, ...) für jeden Parameter an.

Wenn Sie eine Funktion aufrufen und dem Parameter ein Argument übergeben, das einen Standardwert hat, verwendet die
Funktion dieses Argument anstelle des Standardwerts.

Wenn Sie das Argument jedoch nicht übergeben, verwendet die Funktion den Standardwert.

Um Standardparameter zu verwenden, müssen Sie die Parameter mit den Standardwerten hinter anderen Parametern platzieren.
Andernfalls erhalten Sie einen Syntaxfehler.

```
def greet(name, message='Hi'):
    return f"{message} {name}"
    
def greet(name='there', message='Hi'):
    return f"{message} {name}"
 ```