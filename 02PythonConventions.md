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
def save_message(text: str) -> None:
    """ This function saves several messages into the database . """
    pass
```

2.5 - For manual assingment of parameters, use spaces: <br>
```python
def send_message(title, body, raise_error = True) -> None:
    pass
```


## 3 - Breaking lines:

3.1 - Break 2 lines for classes, top level functions, logic sections, group of related functios <br>
```python
"""
Python code
"""


def log() -> None:
    pass


class Program:

    def start(self) -> None:
        pass


    def finish(self) -> None:
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


def find_longest_word(text: str) -> None:
    """
    :param text: str - text with all words
    """
    pass
```

5.5 - Use inline comments sparingly <br>
5.6 - Use at least two spaces away from statement <br>
5.7 - Do not state the obvious <br>
```python
def send_email(email: dict) -> bool:
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


    def validate_access(is_admin: bool) -> None:
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
    

    def __init__(self, value: int) -> None:
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

    def __init__(self, password, login) -> None:
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

7.5 - Do not change a list that is being iterated whithin its own iteration<br>
7.6 - In the following example, we lose C because we remove the 'B' which is the index 1<br>
7.7 - When it tries to print the next item after removing 'B', it has already looped through the index 1<br>
```python
items: list[str] = ['A', 'B', 'C', 'D', 'E']

for item in items:
    if item == 'B':
        items.remove('B')
    else:
        print(item)

# Output
# A
# D
# E
```

7.8 - User the function 'isinstance()' to verify types of variables<br>
7.9 - The function 'isinstance()' can be used to check instances of classes as well<br>
```python
name: str = 'John'
age: int = 38

print(isintance(name), str)  # Output is True
print(isintance(age), int)  # Output is True
```
```python
class Animal:
    pass


class Cat(Animal):
    pass


print(isintance(Cat(), Animal))  # Output is True
```

7.10 - Add index to a list of strings
```python
letters: str = 'ABCDEF'

for i, letter in enumarate(letters, start=1):
    print(f'{i}: {letter}')
```

## 8 - Writing classes and functions:

8.1 - Never make classes too big <br>
8.2 - Always try to break classes down to avoid density <br>
8.3 - For example, ff the class Person becomes to big, the address could become the class Address somewhere else <br>
8.4 - Classes should be behavior focused (cluster of funtions) or data focused (structured information) <br>
```python
class Calculator:

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b


    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b


    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b


    @staticmethod
    def divide(a: float, ba: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```
```python
class Person:

    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = name
        self.age = age
        self.address = address


    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age}, address={self.address})"


    def update_address(self, new_address: str) -> None:
        self.address = new_address
```
```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    
    def __str__(self) -> str:
        return f"Book(title={self.title}, author={self.author}"
```

8.5 - Always use dependency injection
8.6 - a class shouldn't be responsible for creating new objects
```python
class EmailService:

    def send_email(self, recipient: str, subject: str, message: str) -> None:
        print(f"Sending email to {recipient}: {subject}\n{message}")


class NotificationService:

    def __init__(self, email_service: EmailService) -> None:
        self.email_service = email_service


    def notify(self, user: str, message: str) -> None:
        subject = f"Notification for {user}"
        self.email_service.send_email(user, subject, message)
```

8.7 - Functions should peform only one task
8.8 - Always try to keep functions short and straight forward
```python
class File:

    def read_file(file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()


    def process_data(data: str) -> str:
        return data.upper()


    def write_file(file_path: str, data: str) -> None:
        with open(file_path, 'w') as file:
            file.write(data)
```

8.9 - If too many paramaters are being passed to the function, it might be trying to do more than one task<br>
8.10 - One way to solve this problem is to use defaul values<br>
8.11 - Another way to solve the problem in a better way this time, is to use a class<br>
```python
# Good
class CardInfo:

    @property
    def number(self) -> str:
        ...


    @property
    def expiration_month(self) -> int:
        ...


    @property
    def expiration_year(self) -> int:
        ...


def validate_card(card: CardInfo) -> bool:
    ...

# Bad
def validate_card(number: str, expiration_month: int, expiration_year: int) -> bool:
    ...
```

## 9 - Python curiosities:

9.1 - Python considers ints narrower than floats. So, using a float in an expression ensures the result will be a float too. However, when doing division, the result will always be a float, even if only integers are used. <br>
```python
# The int is widened to a float here, and a float type is returned.
>>> 3 + 4.0
7.0
>>> 3 * 4.0
12.0
>>> 3 - 2.0
1.0
# Division always returns a float.
>>> 6 / 2
3.0
>>> 7 / 4
1.75
# Calculating remainders.
>>> 7 % 4
3
>>> 2 % 4
2
>>> 12.75 % 3
0.75
```

9.2 - If an int result is needed, you can use // to truncate the result.<br>
```python
>>> 6 // 2
3
>>> 7 // 4
1
```

9.3 - To convert a float to an integer, you can use int(). Also, to convert an integer to a float, you can use float().<br>
```python
>>> int(6 / 2)
3
>>> float(1 + 2)
3.0
```

9.4 - The "==" is used to compare the values of the variables<br>
9.5 - The "is" is used to compare the identities (memory addresses) of the variables<br>
9.6 - Pytho can save on resources when there are two variables with the same value<br>
```python
name_a = 'Smith'
name_b = 'Smith'

print(id(name_b))  # Same ids
print(id(name_b))

print(name_a == name_b)  # Output True 
print(name_a is name_b)  # Output True
```
```python
name_a = 'Smith'
name_b = 'Smith'.lower()

print(id(name_b))  # Different ids
print(id(name_b))

print(name_a == name_b)  # Output True 
print(name_a is name_b)  # Output False
```

