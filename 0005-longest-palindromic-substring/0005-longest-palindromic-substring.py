class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        maxlen = 0
        maxstr = ""
        for i in range(l*2-1):
            index = i // 2
            tmplen = 0
            tmpstr = ""
            if i % 2 == 0:
                for j in range(min(index, l-1-index) + 1):
                    if s[index-j] == s[index+j]:
                        tmplen = 1 + 2 * j
                        tmpstr = s[index-j:index+j+1]
                    else:
                        break
            else:
                for j in range(min(index, l-2-index) + 1):
                    if s[index-j] == s[index+j+1]:
                        tmplen = 2 * (j+1)
                        tmpstr = s[index-j:index+j+2]
                    else:
                        break

            if tmplen > maxlen:
                maxlen = tmplen
                maxstr = tmpstr
        return maxstr