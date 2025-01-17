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

def printList(head):
    while head:
       print(head.val,end = " ")
       head = head.next
    print()


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        old,new = -1,0
        oldest = -1
        minDistance,maxDistance = sys.maxsize,0
        cnt = 0

        prev = head
        while(prev and prev.next and prev.next.next):
            cnt+=1
            Next = prev.next
            NextNext = prev.next.next
            if(prev.val<Next.val and NextNext.val<Next.val or
                prev.val>Next.val and NextNext.val>Next.val):
                if(oldest==-1):oldest = cnt+1
                old = new
                new = cnt+1
                if(old!=0):minDistance = min(minDistance,new-old)
            prev = prev.next
        if(old==0 or old==-1):return [-1,-1]
        return [minDistance,new-oldest]




        
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
        # printList(ll.head)
        print(Solution().nodesBetweenCriticalPoints(ll.head))

