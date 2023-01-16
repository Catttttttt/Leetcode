class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
        ''' dumb
        pt = [[1 for _ in range(j+1)] for j in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i):
                if j != 0 and j != rowIndex:
                    pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
        return pt[rowIndex]
        '''