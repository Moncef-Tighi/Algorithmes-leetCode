# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEven(self, number):
        if number % 2==0:
            return True
        else:
            return False

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack, holder, grandparent=[], [], []
        stack.append(root)
        result=0
        while stack:
            for node in stack:
                if self.isEven(node.val)==True:
                    if node.left:
                        grandparent.append(node.left.left)
                        grandparent.append(node.left.right)
                    if node.right:
                        grandparent.append(node.right.left)
                        grandparent.append(node.right.right)
                if node.left:
                    holder.append(node.left)
                if node.right:
                    holder.append(node.right)
                if node in grandparent:
                    result+= node.val
            stack=holder
            holder=[]
        return result

"""30 fois Plus rapide :

C'est plus rapide parce que ça n'utilise pas d'appel d'autre fonctions et parce que ça calcule le total directement en cherchant
les petits enfants sans attendre que les petits enfants apparaissent dans la loop.

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        ans = 0
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val
        return ans
"""