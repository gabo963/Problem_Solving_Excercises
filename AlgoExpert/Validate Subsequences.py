# -*- coding: utf-8 -*-
"""
AlgoExpert

Validate Subsequence
"""

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 8]

def isValidSubsequence(array, sequence):
    # Write your code here.
    
    revisado = 0
    
    for val in array:
        if revisado == len(sequence):
            break
        if val == sequence[revisado]:
            revisado += 1
        
    return revisado == len(sequence)

print(isValidSubsequence(array, sequence))