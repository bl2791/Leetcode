# Solution 1
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        position = {}
        ncol = len(matrix[0])
        nrow = len(matrix)
        for i in range(nrow):
            for j in range(ncol):
                 if matrix[i][j] == 0:
                        if i not in list(position.keys()):
                            position[i] = []
                        position[i].append(j)
        for i in position:
            matrix[i] = [0] * ncol
            for j in position[i]:
                for i in range(nrow):
                    matrix[i][j] = 0
        return matrix

# Solution 2
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_row = []
        zero_col = []
        ncol = len(matrix[0])
        nrow = len(matrix)
        for i in range(nrow):
            for j in range(ncol):
                 if matrix[i][j] == 0:
                        if i not in zero_row:
                            zero_row.append(i)
                        if j not in zero_col:
                            zero_col.append(j)
        for i in range(nrow):
            for j in range(ncol):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0
        return matrix