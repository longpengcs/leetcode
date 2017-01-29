class Solution(object):
  def isPalindrome(self, s):
    """
    filter ==> get the character which is alpha or number.
    map ==> chance alpha to lowercase.
    """
    a = map(lambda x:x.lower(),filter(lambda x:x.isalnum(),s))
    return a==a[::-1]
