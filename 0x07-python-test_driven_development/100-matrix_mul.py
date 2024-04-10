#!/usr/bin/python3
"""matrix_mul module
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_b should contain only integers or floats")

    set_of_lens = set([])
    for row in m_a:
        set_of_lens.add(len(row))
    if len(set_of_lens) != 1:
        raise TypeError("each row of m_a must be of the same size")

    set_of_lens = set([])
    for row in m_b:
        set_of_lens.add(len(row))
    if len(set_of_lens) != 1:
        raise TypeError("each row of m_b must be of the same size")

    a_col = len(m_a[0])
    b_row = len(m_b)

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
