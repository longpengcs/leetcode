class Solution(object):
    def shortestPalindrome(self, s):
        """
        this is a problem about how to get longest palindrome prefix.
        using kmp algorithm can solve this problem at O(n) time complex.
        """
        x = s
        s = s + '#' + s[::-1]
        nexts = [0 for _ in xrange(len(s))]
        k = 0
        for m in xrange(1,len(s)):
            #if s[k] == s[m],this position has a longest prefix k+1
            #else,k = nexts[k-1]
            while k > 0 and s[k] != s[m]:k = nexts[k-1]
            if s[k] == s[m]:k += 1
            nexts[m] = k
        m = max(nexts[len(s)/2:])
        return x[m:][::-1] + x

if __name__ == '__main__':
  s = Solution()
  c = 'qqqqqqqq'
  print  s.shortestPalindrome(c)
