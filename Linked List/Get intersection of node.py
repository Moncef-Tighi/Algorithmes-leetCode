"""L'idée c'est qu'on traverse la Linked List avec A et B, et si on arrive à la fin de A ou de B, celui qui est arrivé à la fin devient l'autre."""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA,nodeB=headA,headB
        
        while nodeA!=nodeB:
            if nodeA:
                nodeA=nodeA.next
            else:
                nodeA=headB
            
            if  nodeB:
                nodeB=nodeB.next
            else:
                nodeB=headA               
        
        return nodeA