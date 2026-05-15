#!/usr/bin/python3


def pascal_triangle(n):
    
    pascal = []

    for indexor in range(n):
        row = [1] * (indexor + 1)

        for j in range(1, indexor):
            row[j] = pascal[indexor-1][j-1] + pascal[indexor-1][j]

        pascal.append(row)
    return pascal
