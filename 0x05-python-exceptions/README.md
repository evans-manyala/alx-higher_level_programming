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
# TASK 2. Print and count integers

    Write a function that prints the first x elements of a list and only integers.

    => Prototype: def safe_print_list_integers(my_list=[], x=0):
    => my_list can contain any type (integer, string, etc.)
    => All integers have to be printed on the same line followed by a new line - other => type of value in the list must be skipped (in silence).
    => x represents the number of elements to access in my_list
    => x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
    => Returns the real number of integers printed
    => You have to use try: / except:
        => You have to use "{:d}".format() to print an integer
        => You are not allowed to import any module
        => You are not allowed to use len()

# TASK 3.  Integers division with debug

    Write a function that divides 2 integers and prints the result.

    => Prototype: def safe_print_division(a, b):
    => You can assume that a and b are integers
    => The result of the division should print on the finally
    => section preceded by Inside result:
    => Returns the value of the division, otherwise: None
    => You have to use try: / except: / finally:
    => You have to use "{}".format() to print the result
    => You are not allowed to import any module

# TASK 4. Divide a list

    Write a function that divides element by element 2 lists.

    => Prototype: def list_division(my_list_1, my_list_2, list_length):
    => my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    => list_length can be bigger than the length of both lists
    => Returns a new list (length = list_length) with all divisions
    => If 2 elements can’t be divided, the division result should be equal to 0
        => If an element is not an integer or float:
            => print: wrong type
    => If the division can’t be done (/0):
        => print: division by 0
    => If my_list_1 or my_list_2 is too short
        => print: out of range
    => You have to use try: / except: / finally:
    => You are not allowed to import any module

# TASK 5. Raise exception

    Write a function that raises a type exception.

    => Prototype: def raise_exception():
    => You are not allowed to import any module