class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    """
    we can count every character's number,and if 
    all character's number in ransomNote <= magazine.
    it can be costructed.
    there has a more pythonic method,using the Counter's
    feature.
    """
    a = collections.Counter(ransomNote)
    b = collections.Counter(magazine)
    return all([a[m] <= b[m] for m in a])
