#!/usr/bin/python3
"""Class Rectangle that inherits fron Base Geometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle (BaseGeometry):
    """A child class of the BaseGeometry class"""

    def __init__(self, width, height):
        """Initializning the private attributes"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.width = width
        self.height = height
