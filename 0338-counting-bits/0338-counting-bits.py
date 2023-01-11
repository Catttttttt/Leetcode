class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if i == 2 * offset:
                offset = i
            ans[i] = 1 + ans[i - offset]
        return ans
        ''' BF
        ans = []
        for i in range(n + 1):
            binstr = bin(i)
            count = 0
            for j in binstr:
                if j == '1':
                    count += 1
            ans.append(count)
        return ans
        '''