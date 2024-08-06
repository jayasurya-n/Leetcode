# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head==None or head.next==None):return None

        slow, fast = head, head
        
        for i in range(n):
            fast = fast.next
        
        if(fast==None):
            temp = head
            head = head.next
            temp.next = None
            return head
            
        while(fast.next):
            slow = slow.next
            fast = fast.next

        temp = slow.next
        slow.next = slow.next.next
        temp.next = None
        return head

        # N = 0
        # mover = head
        # while(mover):
        #     N+=1
        #     mover = mover.next
        
        # k = N-n
        # if(k==0):
        #     temp = head
        #     head = head.next
        #     temp.next = None
        #     return head
        
        # current = head
        # while(current):
        #     k-=1
        #     if(k==0):break
        #     current = current.next
        
        # temp = current.next
        # current.next = current.next.next
        # temp.next = None
        # return head
