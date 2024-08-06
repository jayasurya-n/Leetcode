# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def length(self,head):
        if(head==None):return 0
        mover = head
        cnt=0
        while(mover):
            cnt+=1
            mover = mover.next
        return cnt

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if(self.length(head1)<self.length(head2)):return self.addTwoNumbers(l2,l1)
        
        c1,c2 = head1,head2
        carry = 0
        while(c2):
            sum = c1.val + c2.val + carry
            digit = sum%10
            carry = sum//10
            c1.val = digit
            c1 = c1.next
            c2 = c2.next

        while(c1):
            sum = c1.val + carry
            digit = sum%10
            carry = sum//10
            c1.val = digit
            c1 = c1.next

        if(carry):
            newNode = ListNode(carry)
            mover = head1
            while(mover.next):
                mover = mover.next
            mover.next = newNode
        return head1

