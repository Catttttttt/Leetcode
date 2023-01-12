class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        maxlen = 1
        l = 0
        hashtable = {}
        for r in range(len(s)):
            if s[r] in hashtable:
                l = max(l, hashtable[s[r]]+1)
                
            maxlen = max(maxlen, r+1-l)              
            hashtable[s[r]] = r
        return maxlen
        
        
        ''' dumb
        if s == "":
            return 0
        length = len(s)
        maxlen = 1
        for l in range(length):
            hashtable = {s[l]:l}
            for r in range(l+1, length):
                if s[r] in hashtable:
                    maxlen = max(maxlen, r-l)
                    break
                elif r == length - 1:
                    maxlen = max(maxlen, r-l+1)
                    break
                else:
                    hashtable[s[r]] = r
        return maxlen
        '''