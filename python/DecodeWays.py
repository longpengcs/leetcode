class Solution(object):
    def numDecodings(self, s):
        """
        very easy way by DP.
        """
        if not s or s[0] == '0':return 0
        s1,s2 = 1,1
        for m in xrange(1,len(s)):
            if s[m] == '0':s2 = 0
            if s[m-1] == '1' or (s[m-1] == '2' and s[m] <= '6'):
                s2 += s1
                s1 = s2 - s1
            else:
                s1 = s2
            if s2 == 0:return 0
        return s2
