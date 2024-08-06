# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # mover = head
        # cnt = 0
        # while(mover!=None):
        #     cnt+=1
        #     mover = mover.next
        
        # mid = cnt//2 + 1

        # cnt = 0
        # mover = head
        # while(mover!=None):
        #     cnt+=1
        #     if(cnt==mid):break
        #     mover = mover.next
        # return mover


        # Tortoise and Hare Algorithm
        slow = head
        fast = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow