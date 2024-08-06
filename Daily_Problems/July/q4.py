from typing import List,Optional
import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class LinkedList:
    def __init__(self):
       self.head = None

    def append(self,newNode):
       if(self.head==None): 
           self.head = newNode
           return
       mover = self.head
       while(mover.next!=None):
           mover = mover.next
       mover.next = newNode

def printLinkedList(head):
    while head:
       print(head.val,end = " ")
       head = head.next
    print()


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while(curr.next):
            start = curr
            sum = 0
            while(curr.next and curr.next.val!=0):
                sum+=curr.next.val
                curr = curr.next
            start.val = sum
            curr = curr.next
            start.next = curr
        start.next = None
        return head



# time complexity: O(n)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        arr = list(map(int,input().strip().split()))
        ll = LinkedList()
        for i in range(len(arr)):
            newNode = ListNode(arr[i])
            ll.append(newNode)
        printLinkedList(ll.head)
        head = Solution().mergeNodes(ll.head)
        printLinkedList(head)
