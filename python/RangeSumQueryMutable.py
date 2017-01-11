class NumArray(object):
  def __init__(self, nums):
    """
    template of binary indexed array.
    """
    #initialize array
    self.nums = nums[:]
    self.cp = nums
    self.length = len(nums)
    for m,v in enumerate(self.nums):
      k = self.getk(m+1)+m
      if k < self.length:self.nums[k] += self.nums[m]

  def getk(self,v):
    return v&(-v)
    
  def update(self, i, val):
    """
    update ith number to val 
    """
    dt = val - self.cp[i]
    self.cp[i] = val
    while i < self.length:
      self.nums[i] += dt
      i += self.getk(i+1)#get the parent point

  def sumRange(self, i, j):
    """
     get sum(sums[i:j+1]
    """
    return self.getn(j) - self.getn(i-1)

  def getn(self,n):#get sums[:n+1]
    s = 0
    while n >= 0:
      s += self.nums[n]
      n -= self.getk(n+1)
    return s
if __name__ == '__main__':
    a = NumArray([7,2,7,2,0])
    a.update(4,6)
    a.update(0,2)
    a.update(0,9)
    a.sumRange(4,4)
    a.update(3,8)
    a.sumRange(0,4)
    a.update(4,1)
    a.sumRange(0,3)
    a.sumRange(0,4)
    a.update(0,4)
