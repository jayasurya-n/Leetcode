# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        cnt = 0
        while(head):
            cnt+=1
            head = head.next
        return cnt
    
    def reverseLL(self,head):
        if(head==None or head.next==None):return head
        newHead = self.reverseLL(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(self.length(head)<k):return head
        mover = head
        cnt = 0
        while(mover):
            if(cnt==k-1):break
            cnt+=1
            mover = mover.next
            
        newHead2 = self.reverseKGroup(mover.next,k)
        mover.next = None
        newHead1 = self.reverseLL(head)
        head.next = newHead2
        return newHead1
            
        