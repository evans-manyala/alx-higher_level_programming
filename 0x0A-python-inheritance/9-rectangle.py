#!/usr/bin/python3
"""Class Rectangle that inherits fron Base Geometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """A child class of the BaseGeometry class"""

    def __init__(self, width, height):
        """Initializning the private attributes"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
    def area(self):
        """Returns area of a rectangle"""
        return self.width * self.height

    def __str__(self):
        """Returns sring output to console"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
