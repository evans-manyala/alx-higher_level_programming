def add_integer(a, b=98):
    """Adds two integers and returns their sum.

    Args:
        a (int or float): The first integer to add.
        b (int or float, optional): The second integer to add. Defaults to 98.

    Returns:
        int: The sum of first_number and second_number.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if type(a) is not int  and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
