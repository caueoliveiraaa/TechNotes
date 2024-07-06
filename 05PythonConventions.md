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

- The tab width should be 4.
- The Maximum line lenght is 79.
- For long blocks of text such as comments, the maximum lenght is 72.
- No unnecessary white spaces.

```python


def save_message(text):
    """ This function saves several messages into the database . """
    pass

```

- For manual assingment of parameters, leave spaces:

```python


def send_message(title, body, raise_error = True):
    pass

```


## Breaking lines:

- Break 2 lines:
  - For classes.
  - Top level functions.
  - Logic sections.
  - Group of related functios.

```python


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
