#!/usr/bin/python3
for x in range(1, 89):
    if x < 10 or x // 10 < x % 10:
        print('{:02d}'.format(x), end=", ")
print(89)
