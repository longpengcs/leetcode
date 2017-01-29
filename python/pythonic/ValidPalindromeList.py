class Solution(object):
    def isPalindrome(self, s):
        """
        list compherence
        """
        a = [m.lower() for m in s if m.isalnum()]
        return a==a[::-1]
