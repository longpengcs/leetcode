import itertools
class Solution(object):
  def groupAnagrams(self, strs):
    """
    using groupby
    """
    return [ (_,[ m for m in it])  for _,it  in itertools.groupby(strs,lambda x:''.join(sorted(x)))]

if __name__ == '__main__':
  s = Solution()
  print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
