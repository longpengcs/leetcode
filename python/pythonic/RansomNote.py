class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    """
    counter - counter,it just save element which
    value > 0.
    """
    return not collections.Counter(ransomNote) - collections.Counter(magazine)
