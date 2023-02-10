#!/usr/bin/python3

"""Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rowLength, colLength = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (colLength + 1) for rows in range(rowLength + 1)]
        
        for row in range(rowLength):
            prefixSum = 0
            for col in range(colLength):
                prefixSum += matrix[row][col]
                above = self.sumMat[row][col + 1]
                self.sumMat[row + 1][col + 1] = prefixSum + above                
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:        
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        
        return bottomRight - above - left + topLeft    
