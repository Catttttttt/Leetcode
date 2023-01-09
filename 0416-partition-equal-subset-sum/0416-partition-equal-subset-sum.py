class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s & 1 != 0:
            return False
        target = s // 2
        dp = [[0] * (target + 1) for j in range(len(nums))]
        for i in range(len(nums)):
            for j in range(target + 1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - nums[i]] + nums[i] if nums[i] <= j else 0)
                if dp[i][j] == target:
                    return True
        return False