# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # cnt1,cnt2 = 0,0
        # l1, l2 = headA, headB

        # while(l1.next):
        #     cnt1+=1
        #     l1 = l1.next

        # while(l2.next):
        #     cnt2+=1
        #     l2 = l2.next

        # if(l1!=l2):return None

        # l1,l2 = headA,headB
        # if(cnt1>=cnt2):
        #     while(cnt1!=cnt2):
        #         cnt1-=1
        #         l1 = l1.next
        # else:
        #     while(cnt2!=cnt1):
        #         cnt2-=1
        #         l2 = l2.next

        # while(l1 and l2):
        #     if(l1==l2):return l1
        #     l1 = l1.next
        #     l2 = l2.next

        l1,l2  = headA,headB

        while(l1!=l2):
            l1 = l1.next
            l2 = l2.next

            if(l1==l2):return l1
            if(l1==None):l1 = headB
            if(l2==None):l2 = headA
        
        return l1