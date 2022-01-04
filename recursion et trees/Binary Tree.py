class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    roadused=[]
    visited=[]
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        node = self.root
        BinaryTree.roadused=[]
        BinaryTree.visited=[]
        result= BinaryTree.preorder_search(self,node, find_val)
        return result

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        node = self.root
        BinaryTree.roadused=[]
        BinaryTree.visited=[]
        result= BinaryTree.preorder_print(self,node)
        listToStr = '-'.join([str(elem) for elem in result]) 
        return listToStr

    def preorder_search(self, node, find_val):
        #D'abord, On regarde si on a déjà visité la value. Si ce n'est pas le cas on ajoute la node à la liste des visités.
        #Et si la node n'est pas une leaf, on va l'ajouter à la route pour qu'on puisse backtrack après.
        if node.value not in BinaryTree.visited:
            BinaryTree.visited.append(node.value)
            if node.left!=None or node.right!=None:
                BinaryTree.roadused.append(node)

        #Appel Récursif, d'abord à gauche puis à droite si à gauche n'existe pas OU a déjà été visité.
        if node.left and (node.left.value not in BinaryTree.visited):
            node=BinaryTree.preorder_search(self, node.left, find_val)
        elif node.right and (node.right.value not in BinaryTree.visited):
            node=BinaryTree.preorder_search(self, node.right, find_val)


        """Ici, on check Si on a fini le boulot. Si roadused est à 0 c'est à dire qu'on a fait le tour du tree sans trouver ce qu'on cherche.
        Ce code se répète plusieurs fois parce il y a plusieurs appels récursif.
        C'est à ça que Node==True sert. Si Node est déjà True, ça veut dire qu'on a trouvé la réponse plut haut.

        Aussi,Faut que ces lignes de code soit là parce qu'apparamment les mettre plus haut ça marchait pas."""
        if len(BinaryTree.roadused)==0:
            return False
        elif node==True or node.value==find_val:
            return True


        #ça c'est les lignes de code pour le backtracking. On vérifie d'abord si c'est une leaf pour éviter l'erreur de "left.value existe pas"
        if (node.left==None and node.right==None) or (node.left.value and node.right.value) not in BinaryTree.visited:
            node=BinaryTree.roadused.pop()
            return BinaryTree.preorder_search(self, node, find_val)


    def preorder_print(self, node):
        """Helper method - use this to create a 
        recursive print solution."""
        if node.value not in BinaryTree.visited:
            BinaryTree.visited.append(node.value)
            if node.left!=None or node.right!=None:
                BinaryTree.roadused.append(node)

        if node.left and (node.left.value not in BinaryTree.visited):
            node=BinaryTree.preorder_print(self, node.left)
        elif node.right and (node.right.value not in BinaryTree.visited):
            node=BinaryTree.preorder_print(self, node.right)

        if len(BinaryTree.roadused)==0:
            return BinaryTree.visited

        if (node.left==None and node.right==None) or (node.left.value and node.right.value) not in BinaryTree.visited:
            node=BinaryTree.roadused.pop()
            return BinaryTree.preorder_print(self, node)



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())
