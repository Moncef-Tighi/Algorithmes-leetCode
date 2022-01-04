class Solution:
    dictionary = {}
    def tribonacci(self, n: int) -> int:
        if n <=0 :
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n in Solution.dictionary :
            return Solution.dictionary[n]
        else :
            Solution.dictionary[n] = Solution.tribonacci(self, n-1) + Solution.tribonacci(self, n-2) + Solution.tribonacci(self, n-3)
            return Solution.dictionary[n]