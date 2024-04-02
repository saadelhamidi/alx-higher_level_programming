#!/usr/bin/python3
""" a class to define a size of square """


class Square():
    """ a class to define and calculate area of the square
    Args:
        square1 (class): a class which define a square with size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end='')
                print()
