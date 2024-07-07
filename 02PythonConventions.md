# 🐍📚 Python Conventions 🐍📚

## General rules of PEP8:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than danse.
Readability counts.
Special cases are not special enough to break the rules - (Although practicality beats purity).
Erros should never pass silently - (Unless explicitly silenced).
In the face of ambiguity, refuse the temptation to guess.
There should be one and preferably only one obvious way to do it - (Although that way may not be obvious at first unless you are Dutch).
Now is better than never - (Although never is better than *right* now).
If the implementation is hard to explain, it's a bad idea
If the implementation is easy to explain, it might be a good idea.
Namespaces are one honking great idea, let's do more of those!
```

## Spaces and lenghts:

- The tab width should be 4 spaces
- The Maximum line lenght is 79 chars
- For long blocks of text such as comments, the maximum lenght is 72 chars
- There should be no unnecessary white spaces

```python
def save_message(text):
    """ This function saves several messages into the database . """

    pass
```

- For manual assingment of parameters, use spaces:

```python
def send_message(title, body, raise_error = True):
    pass
```


## Breaking lines:

- Break 2 lines for classes, top level functions, logic sections, group of related functios

```python
"""
Python code
"""


def log():
    pass


class Program:

    def start(self):
        pass


    def finish(self):
        pass

```

## Importing libraries:

- Seperate import lines
- Same line for same module

```python
"""
# Code as example for order of the imports
# Do not use * because it makes unclear which names are present
"""


import os
import sys
import math


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from datetime import datetime
from fastapi import FastAPI, Depends, HTTPExecption  


# Code

```

## Comments:

- Comments should always be up to date with the projects
- They should always be complete sentences
- They should never contradict what the code does
- They should always contain capitalized begnning (The identifiers case should not be altered in comments)

```python
"""
Docstring describing the program
"""


def find_longest_word(text):
    """
    :param text: str - text with all words
    """

    pass
```

- Use inline comments sparingly
- Use at least two spaces away from statement
- Do not state the obvious

```python
def send_email(email):
    """
    :param email: dict - information about the email
    :param return: bool - result of whether the email is valid
    """

    return validate(email)  # Using this method may affect performance
```

## Naming conventions:

- Names to avoid: "I", "l", "o" - because in some fonts it's indistinguishable from numbers like "1" and "0"
- Modules and packages are all lowercase, but if it improves readability, use underscore

```python
import pandas as pd

from website.email_validations import validate_spam_email
```

- Class names and Exception names are "CamelCase" (Words with the fist letters capitalized)
- Funtions and variables should be all lowercase with underscores

```python
from webscrapping import LoginValidation
from exceptions.erros import LoginError


class TelegramBot():

    # Rest of the class code


    def validate_access(is_admin):
        """
        :param is_admin: bool - user's access level
        """

        if not is_admin:
            raise LoginError("This user has no access.")


    # Rest of the class code

```
- Always use self and cls as first arguments for instance and class methods
- If an argument or variable name clashes with reserved keywords, use a synonym or single trailing underscore


```python
"""
The @classmethod decorator is used to define a method that is bound to
the class and not the instance of the class. The first parameter of a
class method is the class itself.
"""


class MyClass:
    class_variable = 0
    

    def __init__(self, value):
        self.initial_value = value
    

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
        return cls.class_variable


object_ = MyClass(10)

print(MyClass.increment_class_variable())  
print(MyClass.increment_class_variable())

```
- Private and protected names should have underscores

```python
class Login:

    def __init__(self, password, login):
        _password = password
        _login = login
```

- Constants are all capital letters with words seperated by underscores

```python
PROGRAM_VERSION = '1.0.2'
PORT_NUMBER = 8080
PI = 3.141
```

## General conventions:

- Use variables directly in if statements whenever possible

```python
# Good 
if is_admin:
    pass

# Bad
if is_admin == True:
    pass
```

```python
x = None

# Good 
if not x:
    pass

# Bad

if x is not None:
    pass
```

- Return the result right away

```python
# Good 
def add(x, y):
    return x + y

# Bad
def add(x, y):
    result = x = y
    return result
```
