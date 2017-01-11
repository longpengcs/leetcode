# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def recoverTree(self, root):
      """
      using Morris Traversal to inorder travel BST and check the wrong point,
      first wrong point it's value bigger than next one,when we find first point,
      the second wrong point's value less than previous one.
      like: 1 2 3 4 5 6 7 8 9 ==> 1 (7) > 3 4 5 6 > (2) 8 9
      """
      node = TreeNode(None)
      last = node;this = node#last ==> previous node,this ==> current node
      now = root;n1=node;n2=node#n1 the big wrong point,n2 the small wrong point
      #morris inorder traversal,O(1) space,O(n)time,if you don't know,please google.
      while now:
        check = 0#when we travel back we need check if it is a wrong point.
        if not now.left:
           last = this;this=now;check=1
           now = now.right
        else:
          pre = now.left
          while pre.right and pre.right != now:pre = pre.right
          if not pre.right:
             pre.right=now
             now = now.left
          else:
             pre.right = None
             last = this;this=now;check=1
             now = now.right
        if check:
           # the first big one,it is the real big one.
           if not n1.val and last.val > this.val:n1=last
           # if we have not find big one,we could not find small one.
           if n1.val and last.val > this.val:n2=this
      n1.val,n2.val=n2.val,n1.val
