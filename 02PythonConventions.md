# 🐍📚 Python Conventions 📚🐍

## 1 - General rules of PEP8:

```python
# 1 - Beautiful is better than ugly.
# 2 - Explicit is better than implicit.
# 3 - Simple is better than complex.
# 4 - Complex is better than complicated.
# 5 - Flat is better than nested.
# 6 - Sparse is better than danse.
# 7 - Readability counts.
# 8 - Special cases are not special enough to break the rules - (Although # practicality beats purity).
# 9 - Erros should never pass silently - (Unless explicitly silenced).
# 10 - In the face of ambiguity, refuse the temptation to guess.
# 11 - There should be one and preferably only one obvious way to do it - # (Although that way may not be obvious at first unless you are Dutch).
# 12 - Now is better than never - (Although never is better than *right* now).
# 13 - If the implementation is hard to explain, it's a bad idea
# 14 - If the implementation is easy to explain, it might be a good idea.
# 15 - Namespaces are one honking great idea, let's do more of those!
```

## 2 - Using Spaces and lenghts:

2.1 - The tab width should be 4 spaces <br>
2.2 - The Maximum line lenght is 79 chars <br>
2.3 - For long blocks of text such as comments, the maximum lenght is 72 chars <br>
2.4 - There should be no unnecessary white spaces <br>

```python
def save_message(text):
    """ This function saves several messages into the database . """

    pass
```

2.5 - For manual assingment of parameters, use spaces: <br>

```python
def send_message(title, body, raise_error = True):
    pass
```


## 3 - Breaking lines:

3.1 - Break 2 lines for classes, top level functions, logic sections, group of related functios <br>

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

## 4 - Importing libraries:

4.1 - Seperate import lines <br>
4.2 - Same line for same module <br>

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

## 5 - Writing comments:

5.1 - Comments should always be up to date with the projects <br>
5.2 - They should always be complete sentences <br>
5.3 - They should never contradict what the code does <br>
5.4 - They should always contain capitalized begnning (The identifiers case should not be altered in comments) <br>

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

5.5 - Use inline comments sparingly <br>
5.6 - Use at least two spaces away from statement <br>
5.7 - Do not state the obvious <br>

```python
def send_email(email):
    """
    :param email: dict - information about the email
    :param return: bool - result of whether the email is valid
    """

    return validate(email)  # Using this method may affect performance
```

## 6 - Naming conventions:

- 6.1 - Names to avoid: "I", "l", "o" - because in some fonts it's indistinguishable from numbers like "1" and "0" <br>
- 6.2 - Modules and packages are all lowercase, but if it improves readability, use underscore <br>

```python
import pandas as pd

from website.email_validations import validate_spam_email
```

- 6.3 - Class names and Exception names are "CamelCase" (Words with the fist letters capitalized) <br>
- 6.4 Funtions and variables should be all lowercase with underscores <br>

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
- 6.5 - Always use self and cls as first arguments for instance and class methods <br>
- 6.6 - If an argument or variable name clashes with reserved keywords, use a synonym or single trailing underscore <br>


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
- 6.7 - Private and protected names should have underscores <br>

```python
class Login:

    def __init__(self, password, login):
        _password = password
        _login = login
```

- 6.8 - Constants are all capital letters with words seperated by underscores <br>

```python
PROGRAM_VERSION = '1.0.2'
PORT_NUMBER = 8080
PI = 3.141
```

## 7 - General conventions:

- 7.1 - Use variables directly in if statements whenever possible <br>

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

- 7.2 - Return the result right away <br>

```python
# Good 
def add(x, y):
    return x + y

# Bad
def add(x, y):
    result = x = y
    return result
```

- 7.3 - It's important to distinguish which files only contains classes and functions from the executable ones <br>
- 7.4 - This distinguishment can be acomplished with an if statement <br>

```python
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI(title='User API', description='API to manipulate users')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

```python
class User:

    def login(self):
        pass


    def logout(self):
        pass
```

## 8 - Writing classes and functions:

8.1 - Never make classes too big <br>
8.2 - Always try to break classes down to avoid density <br>
8.3 - For example, ff the class Person becomes to big, the address could become the class Address somewhere else <br>
8.4 - Classes should be behavior focused (cluster of funtions) or data focused (structured information) <br>

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


    @staticmethod
    def subtract(a, b):
        return a - b


    @staticmethod
    def multiply(a, b):
        return a * b


    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

```python
class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"


    def update_address(self, new_address):
        self.address = new_address
```

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    
    def __str__(self):
        return f"Book(title={self.title}, author={self.author}"
```
