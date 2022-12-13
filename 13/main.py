import io
import enum
import typing
import types

from input import array

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
    return True

for item in array:
    if compare(*item):
        result.append(index)
    index += 1

print(result)
final = sum(result)
print(final)
