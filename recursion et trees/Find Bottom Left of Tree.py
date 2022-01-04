# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack=[root]
        holder=[]
        while stack:
            for node in stack:
                if node.left:
                    holder.append(node.left)
                if node.right:
                    holder.append(node.right)
            if len(holder)==0:
                return stack[0].val
            stack=holder
            holder=[]


"""Même chose, en plus court :

def findLeftMostNode(self, root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val

"Doing BFS right-to-left means we can simply return the last node's value
 and don't have to keep track of the first node in the current row or even care about rows at all.

  Inspired by @fallcreek's solution (not published) which uses two nested loops to go row by row
   but already had the right-to-left idea making it easier. I just took that further.

note : 
        queue += filter(None, (node.right, node.left))
is the same as :

            if node.right:
                queue += [node.right]
            if node.left:
                queue += [node.left]

"""