#!/usr/bin/python3
"""
Module that contains the function matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices (m_a and m_b).

    Validates inputs according to specified requirements.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(
                    "m_a should contain only integers or floats"
                )

    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(
                    "m_b should contain only integers or floats"
                )

    m_a_row_len = len(m_a[0])
    if not all(len(row) == m_a_row_len for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    m_b_row_len = len(m_b[0])
    if not all(len(row) == m_b_row_len for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if m_a_row_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem_sum = 0
            for k in range(len(m_b)):
                elem_sum += m_a[i][k] * m_b[k][j]
            row.append(elem_sum)
        result.append(row)

    return result
