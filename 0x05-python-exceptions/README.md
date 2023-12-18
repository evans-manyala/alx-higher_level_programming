# 0x05. Python - Exceptions

# Resources

    Read or watch:

    Errors and Exceptions
    Learn to Program 11 Static & Exception Handling (starting at minute 7)
    Learning Objectives
    At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General

    1. Why Python programming is awesome
    2. What’s the difference between errors and exceptions.
    3. What are exceptions and how to use them
    4. When do we need to use exceptions
    5. How to correctly handle an exception
    5. What’s the purpose of catching exceptions
    6. How to raise a builtin exception
    7. When do we need to implement a clean-up action after an exception

# TASK 0. Safe list printing

    Write a function that prints x elements of a list:

    => Prototype: def safe_print_list(my_list=[], x=0):
    => my_list can contain any type (integer, string, etc.)
    => All elements must be printed on the same line followed by a new line.
    => x represents the number of elements to print
    => x can be bigger than the length of my_list
    => Returns the real number of elements printed
    => You have to use try: / except:
    => You are not allowed to import any module
    => You are not allowed to use len()

# TASK 1. Safe printing of an integers list

    Write a function that prints an integer with "{:d}".format().

    => Prototype: def safe_print_integer(value):
    => value can be any type (integer, string, etc.)
    => The integer should be printed followed by a new line
    => Returns True if value has been correctly printed (it means the value is an integer)
    => Otherwise, returns False
    => You have to use try: / except:
    => You have to use "{:d}".format() to print as integer
    => You are not allowed to import any module
    => You are not allowed to use type()
