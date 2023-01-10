class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(l, r, s):
            if len(s) == 2 * n:
                res.append(s)
            if l < n:
                helper(l+1, r, s + "(")
            if r < l:
                helper(l, r+1, s + ")")
        res = []
        helper(0, 0, "")
        return res

        '''
        if n == 1:
            return ["()"]
        res = []
        openp = 0
        closep = 0
        tmp1 = ""
        tmp2 = ""
        for i in generateParenthesis(self, n - 1):
            
        for i in range(2 * n):
            tmp1 += "("
            openp += 1
            res.extend(generateParenthesis(self, n-1))

            tmp2 += ")"
            closep += 1
        '''