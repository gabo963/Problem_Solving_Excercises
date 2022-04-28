# -*- coding: utf-8 -*-
"""
Algo Expert

River Sizes

"""

matrix =  [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1]
  ]

def riverSizes(matrix):
    # Write your code here.
    sizes = []

    for i in range( 0, len(matrix) ):
        for j in range( 0, len( matrix[0] ) ):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                sizes.append(neighbors( i, j, matrix ))
    return sizes
                        
def neighbors( i, j, matrix ):
    suma = 1
    possible = movements(i, j)
    
    for k, l in possible:
        if k >= 0 and k < len(matrix) and l >= 0 and l < len(matrix[0]):
            if matrix[k][l] == 1:
                matrix[k][l] = 0
                suma += neighbors( k,l, matrix )
    return suma

def movements( i, j ):
    possible = []
    
    for x in range(-1, 2):
        if x != 0:
            possible.append( [i+x,j])
            possible.append( [i,j+x])
        
    return possible

print(riverSizes(matrix))