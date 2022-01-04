#Problème? LEEEEEEEEEEEEEEEEEEEEEEEENNNNNNNNNNNNNNNNNTTTTTTTTTTT

class TreeNode:
    def __init__(self, val=0, left=None, right=None, depth=0):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack=[]
        visited=[]
        stack.append(root)
        result=0
        maxDepth=0
        Depth=0
        while stack:
            visited.append(root)
            if root.left==None and root.right==None and Depth==maxDepth:
                result+=root.val
            if root.left and root.left not in visited:
                stack.append(root)
                Depth+=1
                root=root.left
            elif root.right and root.right not in visited:
                stack.append(root)
                Depth+=1
                root=root.right
            else:
                root=stack.pop()
                Depth-=1
            if Depth>maxDepth:
                maxDepth=Depth
                result=0
        return result            