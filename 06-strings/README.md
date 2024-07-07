# 06 Strings


## Escape Characters

```
\'
\"
\t
\n
\\
```

## Raw strings
* ignore escape characters (print backslashes)
* tip: use raw strings for Windows paths since they use backslashes

```py
print(r"He said \"hi.\"") # literally prints as written
```

## String Interpolation
* Way to put strings inside other strings
* Don't have to call `str()` and use concatenation (`+`)
* similar to f-strings

```py
name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))

# 'My name is Al. I am 4000 years old.'
```

## Methods
* `.upper()` and `.lower()` return strings with all upper or lowercase letters
* startswith, endswith
* join, split
    * split by default uses whitespace (space, tab, newline)

```py
print(', '.join(['cats', 'rats', 'bats']))
# 'cats, rats, bats'

print('MyABCnameABCisABCSimon'.split('ABC'))
# ['My', 'name', 'is', 'Simon']
```

* partition
    * returns tuple!
    * only splits on the first occurrence
    * if no occurrences, whole string in tuple[0]
    ```py
    print('Hello, world!'.partition('o'))
    # ('Hell', 'o', ', world!')

    print('Hello, world!'.partition('XYZ'))
    # ('Hello, world!', '', '')
    ```
    * can use multiple assignment trick
    ```py
    >>> before, sep, after = 'Hello, world!'.partition(' ')
    >>> before
    'Hello,'
    >>> after
    'world!'
    ```



### `isX` methods

* `.isupper()` and `.islower()` return booleans if all chars in string are upper/lower case letters
* `.isalpha()` only letters, not blank
* `.isalnum()` string consists only of letters and numbers and is not blank
* `.isdecimal()` string consists only of numeric characters and is not blank
* `.isspace()` string consists only of spaces, tabs, and newlines and is not blank
* `.istitle()` string consists only of words that begin with an uppercase letter followed by only lowercase letters


* none change the string itself since strings are immutable



