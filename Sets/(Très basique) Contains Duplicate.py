#Est-ce que la liste de numéro contient des duplicates?
#Ici on exploite juste le fait que les sets ne peuvent pas avoir de duplicates.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets=set(nums)
        if len(sets)==len(nums):
            return False
        else:
            return True