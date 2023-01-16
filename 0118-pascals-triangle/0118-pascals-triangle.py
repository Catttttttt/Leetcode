class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pt = [[1 for _ in range(j+1)] for j in range(numRows)]
        for i in range(numRows):
            for j in range(i):
                if j != 0 and j != numRows-1:
                    pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
        return pt