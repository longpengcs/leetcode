class Solution(object):
  def longestPalindrome(self, s):
    """
    the best algorithm is manacher,it has o(n) time complex,and
    easy to undestand compare with suffix array.
    s = 'abcd' change to list ==> [0,1,'a',1,'b',1,'c',1,'d',1,2]. 
    """
    sl = [0]
    for m in s:sl.append(1);sl.append(m)
    sl.append(1);sl.append(2)
    #change end
    idx = 1;maxs = 1
    length = len(sl)
    p = range(length-1)
    for m in xrange(1,length-1):
      if m < maxs:
        p[m] = min(maxs-m,p[2*idx-m])
      else:p[m]=1
      while sl[m-p[m]] == sl[m+p[m]]:p[m] += 1
      if m + p[m] > maxs:
          maxs = m + p[m]
          idx = m
    longest = max(p[:-1])
    index = p.index(longest)
    result = []
    for m in sl[index-longest+1:index+longest-1]:
        if m != 1:result.append(m)
    return ''.join(result)
