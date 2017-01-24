class Solution(object):
  def groupAnagrams(self, strs):
    """
    we can using the sorted string to be a key,
    and put words has same key into same list.
    O(m*log m)*n;
    m ==> max word length.
    n ==> word number.
    """
    result = {}
    for n in strs:
      t = ''.join(sorted(n))
      if t in result:result[t].append(n)
      else:result[t] = [n]
    return result.values()
