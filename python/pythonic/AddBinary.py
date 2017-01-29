class Solution(object):
  def addBinary(self, a, b):
    """
    bin ==> turn number to a binary number (number ==> string)
    int(x,base=y) ==> turn string x to number(base = y)
    """
    return bin(int(a,base=2) + int(b,base=2))[2:]
