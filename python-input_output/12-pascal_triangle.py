#!/usr/bin/python3
"""Generate Pascal's triangle as a list of lists."""


def pascal_triangle(n):
    """Return Pascal’s triangle of size n as a list of lists."""
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
