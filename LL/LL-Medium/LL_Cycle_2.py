# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # hash = set()
        # mover = head
        # while(mover):
        #     if(mover in hash):
        #         print(type(mover))
        #         return mover
        #     else:
        #         hash.add(mover)
        #     mover = mover.next
        # return None

        # Floyd's Tortoise and Hare Algorithm
        slow,fast = head,head

        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next

            if(slow==fast):
                slow = head
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
