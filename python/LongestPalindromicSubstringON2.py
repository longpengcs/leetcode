class Solution(object):
  def longestPalindrome(self, s):
    """
    check if a substring is a palindrome from middle to both ends,
    and record the longest.
    time complex O(N^2)
    """
    string = '';length = len(s)
    for m in xrange(length):#this substing middle in point m.
      n = 1
      #class 'aba',it has a real middle
      while m-n >= 0 and m+n < length and s[m-n] == s[m+n]:n+=1
      if 2*n - 1 > len(string):string = s[m-n+1:m+n]
      n=0
      #class 'aa',it has no real middle
      while m-n >= 0 and m+n+1 < length and s[m-n]==s[m+n+1]:n+=1
      if 2*n > len(string):string = s[m-n+1:m+n+1]
    return string
