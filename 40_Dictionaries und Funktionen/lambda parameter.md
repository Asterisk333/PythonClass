# Lambda Parameter

Mit Python-Lambda-Ausdrücken können Sie anonyme Funktionen definieren.

Anonyme Funktionen sind Funktionen ohne Namen. Die anonymen Funktionen sind nützlich, wenn Sie sie nur einmal verwenden
müssen.

Ein Lambda-Ausdruck enthält normalerweise ein oder mehrere Argumente, kann aber nur einen Ausdruck haben.

Im Folgenden wird die Syntax des Lambda-Ausdrucks dargestellt:

```
lambda parameters: 
    expression
```

```
lambda first_name,last_name: f"{first_name} {last_name}"
```

```
def times(n):
    return lambda x: x * n
double = times(2)
```

Da die Funktion times() eine Funktion zurückgibt, ist auch das double eine Funktion. Um sie aufzurufen, setzen Sie
Klammern wie folgt:

result = double(2)
print(result)
result = double(3)
print(result)