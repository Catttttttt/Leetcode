class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        l = len(nums)
        res = 0
        psa = [0 for _ in range(l)]
        for i in range(l):
            psa[i] = nums[i] + psa[i-1]
            psa[i] %= k
        sums = {}
        for i in range(l):
            if psa[i] == 0:
                res += 1
            if psa[i] not in sums:
                sums[psa[i]] = 1
            else:
                res += sums[psa[i]]
                sums[psa[i]] += 1
        return res  ''' 
        res = 0
        prefix = 0
        count = [1] + [0] * k
        for a in nums:
            prefix = (prefix + a) % k
            res += count[prefix]
            count[prefix] += 1
        return res
            
        '''BF
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) % k == 0:
                    res += 1
        return res    
        '''