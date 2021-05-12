def matrix_find(matrix, value):
    for row in matrix:
        for element in row:
            if element == value:
                return True
    return False
            

matrix = [[3, 4, 4, 6],
          [6, 8, 11, 12],
          [6, 8, 11, 15],
          [9, 11, 12, 17]]

print(matrix_find(matrix, 7))
# False

print(matrix_find(matrix, 17))
# True