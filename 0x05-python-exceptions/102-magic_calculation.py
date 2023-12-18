#!/usr/bin/python3
def magic_calculation(a, b):
    try:
        for x in range(1, 3):
            if x > a:
                raise Exception("Too far")
            result += (a**b) / x
    except Exception as e:
        print(f"Exception: {e}")
    result += a + b
    return result
