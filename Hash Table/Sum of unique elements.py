"""Globalement bonne solution, j'ai vu quelqu'un qui a fait exactement le même principe et une autre personne qui fait beaucoup plus court en nombre
de ligne en utilisant une fonction par défaut de Python. Mais la rapitié est bonne"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dictionary={}
        result=0
        for number in nums:
            if number in dictionary.keys():
                dictionary[number]=0
            else:
                dictionary[number]=1
        for key in dictionary:
            if dictionary[key]==1:
                result+=key
        return result