
# Chapter 4: lists

## Multiple Assignment / tuple unpacking

``` py
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
```
is equivalent to
``` py
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
```


## `import random`
```py
.choice()  ## pick from list
.randint()  ## int in the closed range
.shuffle()  ## mix up list in place
```

## Sorting
* On a list with mixed data types, python's `.sort()` sorts in ASCIIbetical order
```py
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```

* You can pass `key = str.lower` to sort in regular alphabetical order

## Mutability
* strings are immutable
    * build a new one
* lists are mutable
    * assigning one from another makes it point to the same reference of the list (since they're pointing to the same pointer (integer) value, just like below.
* integers are immutable
    * meaning variables assigned to them keep a reference to that literal integer value
    ```py
    >>> spam = 42
    >>> cheese = spam
    >>> spam = 100
    >>> spam
    100
    >>> cheese
    42
    ```

## Tuple
* same as lists, but (1) they are IMMUTABLE and (2) they use parentheses not brackets
* single value tuple `(7,)` (must include comma)
    ```py
    >>> type(('hello',))
    <class 'tuple'>
    >>> type(('hello'))
    <class 'str'>
    ```

## Identity
* `id()` returns unique id for each value
* think of it like a memory address (pointer)]
    * appending to a list (or other in-place modification) doesn't change its id
    * reassigning an int variable to a different number does change its id

## passing references
* Lists and dictionaries pass by reference into functions


## copy and deepcopy
```py
import copy

listb = copy.copy(lista)
listc = copy.deepcopy(lista)
```
* copy copys the list, so that changes to original don't affect it
* however, changes to lists within the outer list will be replicated, since the outer list just stores a reference to the inner lists, and that same reference is copied
* deepcopy solves this by recursively going down the lists within lists and copying everything

## `del` vs `remove`
* del: **keyword**
    * can use slices and the whole list as well
    * raises `IndexError` if not in range
```py
my_list = ['a', 'b', 'c', 'd']
del my_list[2]
my_list = ['a', 'b', 'd']
``` 

* remove: **function**
    * removes first occurence of a value
    * raises `ValueError` if not found
```py
list1 = [0, 2, 3, 2]
list1.remove(2)
list1 = [0, 3, 2,]
```

* pop: **method**
    * `my_list.pop(2)` removes the 3rd element from the list, and returns it
    * raises `IndexError` if not in range
