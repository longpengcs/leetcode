class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    using hash list to record which characters has been read.
    if we find a character has been find,we record the length and 
    update the boundary.
    """
    if not s:return 0
    l,r,length = 0,0,len(s)
    hashs = {}#recording hash list
    m = 1
    while r < length:
      #if s[r] in hash,we calculate different length and update.
      if s[r]  in hashs and hashs[s[r]] > -1:
      # r - l if the length of substring which has no same character.
        if m < r - l:m = r - l
      # record the jump position
        ll = hashs[s[r]] + 1
      # when we jump to some characters, we need to set it to -1 or del it.
        for n in xrange(l,hashs[s[r]]+1):
            hashs[s[n]] = -1
        l = ll#get left boundary
      hashs[s[r]] = r
      r += 1
    if m < length - l:m = length - l
    return m
