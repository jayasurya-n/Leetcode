# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None or head.next==None):return head
        length = 0
        mover = head
        while(mover):
            length+=1
            mover = mover.next
        
        k  = k%length
        if(k==0):return head
        
        slow,fast = head, head
        while(fast):
            k-=1
            fast = fast.next
            if(k==0):break

        while(fast.next):
            slow = slow.next
            fast = fast.next

        front = slow.next
        slow.next = None
        fast.next = head
        head = front
        return head
        

        
