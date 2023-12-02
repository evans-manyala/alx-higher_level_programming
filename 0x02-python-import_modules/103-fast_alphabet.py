#!/usr/bin/python3
import codecs
print(bytes(map(lambda i: i + 65, range(26))).decode("ascii"), end="")
