# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

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

    def printList(self,head):
        while head:
            print(head.val,end = " ")
            head = head.next
            print()


class Solution:
    def deleteNode(self, node):
        if(head==None or head.next==None):return None
    
        if(k==1):
            temp = head
            head = head.next
            temp.next = None
            return head
        
        current = head
        while(current):
            k-=1
            if(k==1):break
            current = current.next
        
        temp = current.next
        current.next = current.next.next
        temp.next = None
        return head






arr = list(map(int,input().strip().split()))
ll = LinkedList()
for i in range(len(arr)):
    newNode = Node(arr[i])
    ll.append(newNode)

mover = ll.head
cnt = 3
for i in range(1,cnt):
    mover = mover.next
node = mover

print(Solution().deleteNode(node))
printList(ll.head)
        