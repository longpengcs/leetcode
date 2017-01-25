"""rk method:
   if hash(s[i:i+length]) == hash(pattern) ==> maybe s[i:i+length] == pattern
   if hash(~) != hash(~) ==> s[~] != pattern
   first:give a very easy way to achieve it,but it has O(MN) complexity.
"""
def rk(pattern,s):
    length = len(pattern)
    hashp = hash(pattern)
    for m in xrange(len(s) - length):
      sm = s[m:m+length]
      if hash(sm) == hashp:
        if sm == pattern:return m
    return -1

if __name__ == '__main__':
   s = '12345ababab12345'
   pattern = 'ababv'
   print rk(pattern,s)
