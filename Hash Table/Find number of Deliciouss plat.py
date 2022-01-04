"""Bit of a crappy one, mon code n'a pas passé un edge case et je sais pas pourquoi."""

def findPreviousPowerOf2(n):
    while (n & n - 1):
        n = n & n - 1
    return n
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        seen={}
        output=0
        for item in deliciousness:
            holder=item-findPreviousPowerOf2(item) 
            if holder==0:
                holder=item
            
            print("Item=",item)
            print("Holder=",holder)

            
            if holder in seen.keys():
                print("Result=", item)
                output+=seen[holder]
            if item not in seen.keys():
                seen[item]=1
            else:
                seen[item]+=1
        return output

"""Le seul truc vraiment intéressant dans le code c'est les quatre lignes à la fin (avant return)
le +=1 c'est pour prendre en compte la fréquence. Donc si un chiffre apparait 10 fois on pourra prendre en compte ça plutôt que d'ajouter
1 seulement.