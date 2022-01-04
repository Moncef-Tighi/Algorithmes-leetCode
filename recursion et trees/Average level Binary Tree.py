# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        median, stack, stack2=[], [], []
        stack.append(root)
        while stack:
            holder=[]
            for node in stack:
                holder.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            median.append(round(mean(holder),5))
            stack=stack2
            stack2=[]
        return median


"""PLUS RAPIDE :

Cette solution utilise deux varaible au lieu de 3 en utilisant for I in range len(queue) plutôt que Stack 2
Il gagne un peu de vitesse en évitant de devoir copier le stack, c'est exactement pareil sinon. (de 72ms à 52)

class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        result = []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(sum(level)/len(level))
        return result
"""