class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    if j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] += 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1-1][l2-1]
