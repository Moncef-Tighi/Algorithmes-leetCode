"""Problème ultra commun, voilà une manière standard de le résoudre"""

class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
            print (i, "-", value)
            print(remaining)
            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5

"""On cherche les deux nombre qui en s'aditionnant donne target
C'est possible d'utiliser une nested loop mais c'est du gâchis.
Beaucoup plus opti d'utiliser un dictionnaire (ici Seen) dans ce cas précis si une valeur est exactement égal à la substraction (remaining)
d'une valeur précédente ça veut dire que la valeur actuelle + la valeur précédente =  Target donc c'est ce qu'il faut output"""