"""sunday is a very easy algorithm,same as brute force,it match every character
   in pattern and target,when it find two different character,it find a character
   from right to left which same as the match target's next character.
   abcdefg  ==>   abcdefg
   cde      ==>     cde
   a != c  and we find a 'd' in 'cde' so we make 'd' match 'd'.
"""

def sunday(pattern,s):
  lenp = len(pattern)
  nexts = [lenp+1 for m in xrange(128)]
  for m,n in enumerate(pattern):
    nexts[ord(n)] = lenp - m
  length = len(s) - len(pattern)
  while m <= length:
    real = 1;k=m
    for n in pattern:
      if n == s[k]:k+=1
      else:real=0;break
    if real:return m
    else:m += nexts[ord(s[m + lenp])]
  return -1
if __name__ == '__main__':
  s = '2345ababab12345'
  pattern = '12345'
  print sunday(pattern,s) 
