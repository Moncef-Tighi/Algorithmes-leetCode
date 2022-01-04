class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sets1=set(nums1)
        sets2=set(nums2)
        sets3= sets1 & sets2
        return list(sets3)