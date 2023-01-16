class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mlen = len(nums1) + len(nums2)
        merged = [0 for _ in range(mlen)]
        i = 0
        j = 0
        for k in range(mlen):
            if j == len(nums2):
                merged[k] = nums1[i]
                i += 1
            elif i == len(nums1) or nums2[j] < nums1[i]:
                merged[k] = nums2[j]
                j += 1
            else:
                merged[k] = nums1[i]
                i += 1
        if mlen % 2 == 0:
            return (merged[mlen // 2 - 1] + merged[mlen // 2]) / 2.0
        else:
            return merged[mlen // 2]
        