

import io
import enum
import typing
import types

from input import array

FILE = "input.txt"
FILE = "sample.txt"


data = None
with open(FILE) as file:
    data = file.read()


print(data)
