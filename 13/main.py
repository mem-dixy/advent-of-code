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


test = value_type(4)


a = [1, 2, 3]
b = [4, 5]

c = zip(a, b, strict=False)
d = list(c)
print(d)
for item in d:
    print(item)

print(Type.NUMBER.value)
print(Type.ARRAY.value)
index = 1
result = []

def compare(left, right):
    while True:
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
                match compare(left, [right]):
                    case True:
                        return True
                    case False:
                        return False
            case (Type.ARRAY.value, Type.NUMBER.value):
                match compare([left], right):
                    case True:
                        return True
                    case False:
                        return False
            case _:
                test = False
                print("FAIL")
        return "BOO"


array = array[0:1]
for item in array:
    (one, two) = item
    print(one, two)
    (one, two) = (value_type(one), value_type(two))

    test = None
    match (one, two):
        case (Type.NUMBER.value as left, Type.NUMBER.value as right):
            test = True if left < right else test
            test = False if left > right else test
        case (Type.ARRAY.value as left, Type.ARRAY.value as right):
            test = True if left < right else test
            test = False if left > right else test
        case Type.ARRAY.value:
            print("ARRAY")
        case _:
            test = False
            print("FAIL")

    if True:
        result.append(index)
    index += 1


final = sum(result)
print(final)
