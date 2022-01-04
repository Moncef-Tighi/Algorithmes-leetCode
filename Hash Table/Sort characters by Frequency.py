class Solution:
    def frequencySort(self, s: str) -> str:
        frequency={}
        for letter in s:
            if letter in frequency.keys():
                frequency[letter]+=1
            else:
                frequency[letter]=1
        sortedDict=dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)) #La ligne de code qui rend tout possible
        output=""
        for letter in sortedDict:
            while sortedDict[letter]>0:
                output+=letter
                sortedDict[letter]-=1
        return output