

import io
import enum
import typing
import types

from input import demo as array

def value_type(value):
    return str(type(value))

class Type(enum.Enum):
    NUMBER = value_type(0)
    ARRAY = value_type([0])


index = 1
result = []

def compare(left, right):
    match (value_type(left), value_type(right)):
        case (Type.NUMBER.value, Type.NUMBER.value):
            if left < right:
                return True
            if left > right:
                return False
        case (Type.ARRAY.value, Type.ARRAY.value):
            for zipper in zip(left, right, strict=False):
                match compare(*zipper):
                    case True:
                        return True
                    case False:
                        return False
            if len(left) < len(right):
                return True
            if len(left) > len(right):
                return False
        case (Type.NUMBER.value, Type.ARRAY.value):
            match compare([left], right):
                case True:
                    return True
                case False:
                    return False
        case (Type.ARRAY.value, Type.NUMBER.value):
            match compare(left, [right]):
                case True:
                    return True
                case False:
                    return False
        case _:
            print("FAIL")
            return False
    return None


size = len(array) - 1
for turn in range(size):
    for index in range(0, size - turn, 1):
        left = array[index + 0]
        right = array[index + 1]
        compare(left, right)



divider_top = [[2]]
divider_bottom = [[6]]

index = 1
index_top = 0
index_bottom = 0
for item in array:
    cat = str(item)
    dog = str(divider_bottom)
    fromo = str(divider_top)
    if str(item) == str(divider_top):
        index_top = index
    if str(item) == str(divider_bottom):
        index_bottom = index
    index += 1

index_code = index_top * index_bottom
print(F"{index_top} * {index_bottom} = {index_code}")
