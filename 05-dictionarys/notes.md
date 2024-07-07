# Chapter 4 Dictionaries

## intro
* `KeyError` when accessing invalid key
* Ordered dictionaries
    * they will print in the order you fill them essentially
    * added in python 3.7, so don't trust this to work

## keys, values, "in"
* Methods: keys, values, and items (key value tuples)
    * can do `for k, v in d.items()` as well
* `in d` and `in d.keys()` are equivalent. 
    * The in operator checks whether a value exists as a key in the dictionary


## the `get()` method
* `get(key_of_value_to_get, fallback_value)`
* so it doesn't throw key error when indexing to nonexistent value

## `setdefault()`
```py
if 'color' not in spam:
    spam['color'] = 'black'
```
equivalent to 
```py
spam.setdefault('color', 'black')
```
* Won't overwrite color, just will add it as 'black' if it's not in dict yet
* returns the value that the passed-in key ends with, whether changed or not

This counts the occurrences of each character in a message
```py
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
```

## Pretty Printing
* `pprint()` pretty prints
* `pformat()` stores a pretty string value
* equivalent lines: 
```py
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
```




