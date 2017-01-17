class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    zip('') ==> []
    zip('abc') ==> [('a',),('b',),(c,)]
    zip('ab','abc') [('a','a'),('b','b')]
    ''.join([])=''
    """
    prefix = []
    for m in zip(*strs):
      if len(set(m)) == 1:prefix.append(m[0])
      else:break
    return ''.join(prefix)
