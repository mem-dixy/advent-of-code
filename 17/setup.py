LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)



def file_read(FILE):
    with open(FILE) as file:
        read = file.read()
        strip = read.strip()
        split = strip.split(LINE_FEED)
    return split


def open_file(FILE):
    with open(FILE) as file:
        read = file.readline()
        strip = read.strip()
    return strip



def load(file):
    return open_file(file)
