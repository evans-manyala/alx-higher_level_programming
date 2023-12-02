#!/usr/bin/python3
import codecs
print(codecs.encode(bytearray(map(lambda i: i + 65, range(26))),
                    "ascii").decode("ascii"), end="")
