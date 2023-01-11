class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        ans = []
        for i in range(n + 1):
            binstr = bin(i)
            count = 0
            for j in binstr:
                if j == '1':
                    count += 1
            ans.append(count)
        return ans