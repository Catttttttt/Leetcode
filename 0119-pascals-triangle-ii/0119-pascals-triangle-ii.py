class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pt = [[1 for _ in range(j+1)] for j in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i):
                if j != 0 and j != rowIndex:
                    pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
        return pt[rowIndex]