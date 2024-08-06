# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self,head):
        slow, fast = head, head
        fast = fast.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self,head1, head2):
        left = head1
        right = head2

        dummy = ListNode(-1,None)
        prev = dummy

        while(left and right):
            if(left.val<=right.val):
                prev.next = left
                prev = left
                left = left.next
            else:
                prev.next = right
                prev = right
                right = right.next
            
        if(left):prev.next = left
        if(right):prev.next = right

        return dummy.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):return head

        head1 = head
        mid = self.middle(head)
        head2 = mid.next
        mid.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1,head2)
        return head
        