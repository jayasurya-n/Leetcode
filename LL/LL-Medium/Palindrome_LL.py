# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseLL(self,head):
        if(head==None or head.next==None):
            return head
        
        newHead = self.reverseLL(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # l = []
        # mover = head
        # while(mover):
        #     l.append(mover.val)
        #     mover = mover.next
        # if(l==l[::-1]):return True
        # return False

        slow, fast = head, head
        while(fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        newHead = self.reverseLL(mid.next)

        first,second = head,newHead
        while(second):
            if(first.val!=second.val):
                temp = self.reverseLL(newHead)
                return False
            first = first.next
            second = second.next
        temp = self.reverseLL(newHead)
        return True