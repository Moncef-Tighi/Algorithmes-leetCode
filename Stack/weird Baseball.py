"""You are keeping score for a baseball game with strange rules.
 The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record.
 You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record."""


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        x=0
        result=[]
        while x<len(ops):
            if ops[x]=="C":
                result.pop()
            elif ops[x]=="D":
                result.append((result[-1])*2)
            elif ops[x]=="+":
                result.append((result[-1])+(result[-2])) 
            else:
                result.append(int(ops[x]))
            x+=1
        return sum(result)