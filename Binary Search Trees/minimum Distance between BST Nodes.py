The idea is to use an in-order traversal and find the difference between the current node and the node previously checked.

Think of this question like a variation on "what is the smallest distance between any two values in a sorted array?" With a sorted array, all you do is scan through the entire array looking for the absolute minimum difference between two adjacent values since you know, when the array is sorted, that the answer can only be found between those two ADJACENT values.

To scan the BST like a sorted array, just go through IN-ORDER traversal and keep track of the previous node evaluated.

    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return
        
        self.minDiffInBST(root.left)
		# evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
		
        self.minDiffInBST(root.right)
        return self.res


"""Ma réponse est correcte mais lente, j'ai pas utilisé in-order donc ça m'a donné un truc faux inititalement.
(donc, on traverse du plus petit au plus grand)
 Au lieu de ça j'ai créé une nested-loop et j'ai vérifié chaque résultat possible, donc plus lent.
class Solution:
    liste=[]
    def minDiffInBST(self, root: TreeNode):
        minimum=9999999999
        holder=0
        self.liste=[]
        self.liste= self.minDiffInBST_helper(root)
        for number in self.liste:
            x=0
            while x<len(self.liste):
                holder=number-self.liste[x]
                if holder>0 and minimum>holder:
                    minimum=holder
                x+=1
        return minimum
    def minDiffInBST_helper(self, root: TreeNode) -> int:
        if root:
            self.liste.append(root.val)
            if root.left:
                self.minDiffInBST_helper(root.left)
            if root.right:
                self.minDiffInBST_helper(root.right)
        return self.liste
"""