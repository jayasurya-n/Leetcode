# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # mover = head
        # l = []
        # while(mover):
        #     l.append(mover.val)
        #     mover = mover.next
        
        # mover = head
        # while(mover):
        #     mover.val = l.pop()
        #     mover = mover.next
        # return head

        prev = None
        current = head

        while(current):
            front = current.next
            current.next = prev
            prev = current
            current = front
        return prev

        