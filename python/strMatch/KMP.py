#!/usr/env/bin python
def kmp(pattern,s):
  k = 0;m = 1;length = len(pattern)
  nexts = [0] * length
#-----------------------------------------------
#construct the next array.
#m ==> the substring who ending by mth chr.
#k ==> last substring has k length same pre and suffix.
  for m in xrange(1,length):
    while k > 0 and pattern[m] != pattern[k]:k = nexts[k-1]
    if(pattern[m] == pattern[k]):k += 1
    nexts[m] = k
#constructing over.
  print nexts
  k = 0;m = 0
#match begin
  while m < len(s):
    if s[m] == pattern[k]:
      k += 1
    else:
#if not match in position k, k jump to next(k-1)
      k = nexts[k-1] if k else 0
    m += 1
    if k == length:return m-length 

if __name__ == '__main__':
  s = '12345ababab12345'
  pattern = 'abab'
  print kmp(pattern,s)
    
