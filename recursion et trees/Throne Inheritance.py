"""Ma solution est essentiellement un exemple simple de ce que j'ai apprit dans le cours. J'utilise BFS pour ajouter des nodes et marquer les death
Mais c'est lent. D'autres personnes se cassent moins la tête pour aller plus vite. Plutôt qu'un tree, ils utilisent souvent des dictionnaires
pour simuler un tree

Essentiellement, je traverse le tree à chaque fois là ou un dictionnaire va utiliser une hashtable pour aller directement vers la node en O(1)
Donc mon code pour birth, death et Inheritance est O(N) là ou il faut que seul Inheritance soit O(N)
"""


class ThroneInheritance:
    result=[]
    def __init__(self, kingName: str):
        self.name= kingName
        self.children= []
        self.alive=True
   

    def birth(self, parentName: str, childName: str) -> None:
        node=self
        stack=[]
        while True:
            if node.name==parentName:
                child=ThroneInheritance(childName)
                node.children.append(child)
                break
            for child in node.children:
                stack.append(child)
            node=stack.pop(0)
            
            
    def death(self, name: str) -> None:
        node=self
        stack=[]
        while True:
            if node.name==name:
                node.alive=False
                break
            for child in node.children:
                stack.append(child)
            node=stack.pop(0)
        return None

    
    def getInheritanceOrder(self):
        node=self
        ThroneInheritance.result=[]
        return self.getInheritanceOrder_helper(node)
    
    def getInheritanceOrder_helper(self, current) -> List[str]:
        if current.name not in self.result and current.alive==True: 
            self.result.append(current.name)
        for child in current.children:
            if child.name not in self.result:
                self.getInheritanceOrder_helper(child)

        return self.result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()





"""Voilà un exemple de solution largement plus rapide : 

class TreeNode:

    def __init__(self, name: str):
        self.name = name
        self.is_alive = True
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = TreeNode(kingName)
        self.nodes = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = TreeNode(childName)
        self.nodes[parentName].children.append(child)
        self.nodes[childName] = child

    def death(self, name: str) -> None:
        self.nodes[name].is_alive = False

    def getInheritanceOrder(self):
        This method derives the inheritance order from this
        object's inheritance tree.

        :return: Array of names in inheritance order
        :rtype: list[str]

        def recursive(head: TreeNode, inherit):
            if head.is_alive:
                inherit.append(head.name)
            for child in head.children:
                inherit = recursive(child, inherit)
            return inherit

        return recursive(self.root, [])


""