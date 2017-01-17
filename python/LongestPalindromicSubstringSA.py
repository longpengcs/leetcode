#!/usr/bin/env python
class Solution(object):
  """
  this solution is using the suffix array,it is difficult to
  understand and i spend a week to think about it.
  """
  def longestPalindrome(self, s):
    class node():
      """
      a class about suffix(nu),it has three attribute.
      x ==> first keywords rank
      y ==> second keywords rank
      nu ==> suffix number
      """
      def __init__(self,x,y,nu):
        self.x = x
        self.y = y
        self.nu = nu
 
    def getLP(s):
      """
      get the longest Palindrome,it has three part.
      1. get the suffix array and rank array
      2. calculate height array
      3. find the LP
      """
      #reverse s and add it to s(in the middle add a 0,0 < str)
      st = list(s) + [0] + list(reversed(s))
      length = len(st)
      r = list(st) + [-1] * length#when m + k > length r[m+k] = -1
      sa = [node(0,0,0) for m in xrange(length)]#every node represent a suffix
      k = 1
      while k <= length:
        for m in xrange(length):
          sa[m].x = r[m]
          sa[m].y = r[m+k]
          sa[m].nu = m
        sa.sort(key=lambda x:(x.x,x.y))#sort according to x,y
        rank = 0;r[sa[0].nu]=0
        for m in xrange(1,length):
            #if two suffix has same first and second keywords rank,it has same rank
            rank = rank if sa[m].x == sa[m-1].x and sa[m].y == sa[m-1].y else rank + 1
            r[sa[m].nu] = rank
        k *= 2
      #calculate sa
      for m in xrange(length):sa[r[m]]=m
      rank = r[:length]
      #end to calculate rank and sa
      #---------------------------------------------------------------------------
      #begin to calculate height
      height = range(length);k=0
      for m in xrange(0,length):
        if k:k -= 1
        if not rank[m]:continue
        n = sa[rank[m]-1];t = max(n,m)
        while t+k < length and st[n+k] == st[m+k]:k+=1
        height[rank[m]] = k
      #---------------------------------------------------------------------------
      #begin to calculate longest Palindrome
      p = 0;maxs = 0;ls = len(s)
      for m in xrange(1,length):
      #i have no ideal about this,sorry.
        if sa[m] + sa[m-1] == length-height[m] and ((sa[m] < ls) != (sa[m-1] < ls)):
           if height[m] > maxs:
             p = m;maxs = height[m]
      return ''.join(st[sa[p]:sa[p]+maxs])
    return getLP(s)

if __name__ == '__main__':
  a = Solution()
  print a.longestPalindrome('abcdCXdcba')
