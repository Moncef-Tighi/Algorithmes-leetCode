"""C'est intéressant parce que ça montre comment trouver un l'index d'un élément avec sa value"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dictionary={}
        for number in A:
            if number not in dictionary.keys():
                dictionary[number]=1
            else:
                dictionary[number]+=1
        values=list(dictionary.values())
        keys=list(dictionary.keys())
        position=values.index(len(A)//2)
        return keys[position]


"""Mais en vrai pas besoin de tout ça parce que le seul élément qui se répétait plusieurs fois c'était celui qu'on cherche.
Les autres ne sont répétés qu'une fois donc on peut juste faire :"""
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dictionary={}
        for number in A:
            if number not in dictionary.keys():
                dictionary[number]=1
            else:
                return number
"""Mais c'est beaucoup moins intéressant"""