class TreeNode:
    def __init__(self, val=0, left=None, right=None, visited=False):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sequence(self, root, result):
        if root:
            if root.left==None and root.right==None:
                result.append(root.val)
                return result
            elif root.left and root.right: 
                return Solution.sequence(self, root.left, result) and Solution.sequence(self, root.right, result)
            elif root.right==None:
                return Solution.sequence(self, root.left, result)
            elif root.left==None:
                return Solution.sequence(self, root.right, result)
        return result
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        x=  self.sequence(root1,[])
        y=  self.sequence(root2,[])
        if x==y:
            return True
        else:
            return False