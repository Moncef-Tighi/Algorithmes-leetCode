# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""La difficulté là c'était de penser à ne parcourir le tree que quand la valeur actuelle n'est pas déjà hors champ (low ou high)
et il faut bien que ça soit la valeur actuelle

aussi, faut pas que j'oublie qu'utiliser un appel avec return ça va tout arrêter alors que sans ça ça va exécuter le code en dessous aussi
"""

class Solution:
    result=0
    def DFS(self, root, low, high):
        if root:
            if root.val<=high and root.val>=low:
                self.result+=root.val
            if root.val>=low:
                self.DFS(root.left, low, high)
            if  root.val<=high:
                self.DFS(root.right, low, high)
        return self.result
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.DFS(root, low, high)





