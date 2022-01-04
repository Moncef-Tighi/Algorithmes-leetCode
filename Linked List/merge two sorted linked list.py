# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        liste=[]
        while l1!=None:
            liste.append(l1.val)
            l1=l1.next
        while l2!=None:
            liste.append(l2.val)
            l2=l2.next  
        liste.sort()
        result=[]
        x=0
        l3= ListNode()
        while x<len(liste):
            l3.val=liste[x]
            if x+1<len(liste):
                l3.next=ListNode(liste[x+1])
            result.append(l3)
            l3=l3.next
            x+=1
        if result:
            return result[0]
        else:
            return None