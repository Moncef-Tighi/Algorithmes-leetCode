"""C'est proche de la vitesse maximal sachant que selon ma luck mon classement change considérablement
On est obligé de traverser tout le tree donc on est sur du O(N) la différence de vitesse se fait juste sur le nombre de comparaison
Quoi que on peut opti en abortant quand on a trouvé X et Y, mais dans l'exercice X et Y était souvent au fond du tree""" 


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue=[]
        parentX,parentY,i, level=0,0,0,0
        queue.append(root)
        while queue:
            i+=1
            level=len(queue)
            while level>0:
                root=queue.pop(0)
                if root.left:
                    queue.append(root.left)
                    if root.left.val==x:
                        parentX=root.val
                        x = i
                    if root.left.val==y:
                        parentY=root.val
                        y = i            


                if root.right:
                    queue.append(root.right)
                    if root.right.val==x:
                        parentX=root.val
                        x = i
                    if root.right.val==y:
                        parentY=root.val
                        y = i
                level-=1
        if x==y and parentX!=parentY and (parentX!=0 and parentY!=0):
            return True
        else:
            return False

""" Approche similaire à la mienne mais qui utilise un dictionnaire et moins de conditions. Un peu plus compliqué mais largement moins de lignes
En gros elle stock ensemble le root, le niveau et le parent dans la queue. Elle a deux list, une queue qui fait la traversée
et Nodes qui garde le level et les parent à l'index équivalent à la value de la nod
Cette solution ne fonctionnerait pas si des valeurs se répétaient

class Solution(object):
    def isCousins(self, root, x, y):
        nodes = collections.defaultdict(list)
        queue = [(root,0,0)]
        while queue:
            node,level,parent = queue.pop(0)
            nodes[node.val] = [level,parent]

            if node.left:
                queue.append((node.left,level+1,node.val))
            if node.right:
                queue.append((node.right,level+1,node.val))

        if nodes[x][0]==nodes[y][0] and nodes[x][1] != nodes[y][1]:
            return True

        return False
"""
