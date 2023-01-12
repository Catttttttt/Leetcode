class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return helper(n - 1) + helper(n - 2)
        return helper(n)