"""rk method:
   if hash(s[i:i+length]) == hash(pattern) ==> maybe s[i:i+length] == pattern
   if hash(~) != hash(~) ==> s[~] != pattern
   second:hash(s[m:m+length]) = (d^length-1)*s[m] + ....+ s[m+length-1] = Sm
   Sm+1 = S[m+length] + d*(Sm - s[m]*d^(length-1))
"""
def rk(pattern,s):
  p = 2891336453
  length = len(pattern);s1 = 0;s2 = 0;h = 1
  for m in xrange(length-1):
    h = h*10 % p
  for m in xrange(length):
    s1 = (int(pattern[m])+s1*10) % p
    s2 = (int(s[m]) + s2*10) % p
  for m in xrange(length,len(s)):
    if s1 == s2 and s[m-length:m] == pattern:return m - length
    s2 = (int(s[m]) + 10*(s2 - int(s[m-length])*h)) % p
if __name__ == '__main__':
   s = '234512345'
   pattern = '123'
   print rk(pattern,s)
