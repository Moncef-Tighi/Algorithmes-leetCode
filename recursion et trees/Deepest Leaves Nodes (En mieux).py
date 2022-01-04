class TreeNode:
    def __init__(self, val=0, left=None, right=None, depth=0):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        #On transforme le TreeNode en une liste comme ça Python fait tout le boulot d'ittérer dessus.
        q = [root]
        level = []
        while q:        
            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            #On va même pas chercher à connaître les Vals, on va juste chercher les leaves. On arrête la loop complètement si level = 0 
            if len(level) == 0:
                break
            #On réinititalise Level
            q = level
            level = []
        sum = 0
        for node in q:
            sum += node.val
        return sum



Voilà comment ça fonctionne : 
La loop : 
for node in q:
    if node.left:
        level.append(node.left)
            if node.right:
        level.append(node.right)
En elle même ne dit pas grand chose. Là ou c'est intéressant c'est ça : 
q = level
level = []

Enfaite, la loop ne sélectionne pas TOUT, elle s'électionne toute les nodes sauf les nodes du niveau actuelle. Parce qu'elle prend le chemin
Donc d'abord elle ne s'électionne pas le root
ensuite elle sélectionne pas le niveau 2 et ainsi de suite. À la fin il reste plus que les nodes les plus profondes
Et dans la dernière ittération on va même supprimer les dernières leaves sauf qu'on va s'arrêter avant d'override q avec le contenu de Level'
et on va donc compter la somme des nodes du dernier niveau.