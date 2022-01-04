"""Seul problème du code c'est qu'on gâche pas mal de mémoire en stockant toute les configuration possible
qui ne se répètent pas"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen={}
        result=[]
        i=0
        while i<len(s):
            sequence=s[i:i+10]
            print(seen)
            if sequence in seen and sequence not in result:
                result.append(sequence)
            elif sequence not in result:
                seen[sequence]=i
            i+=1
        return result