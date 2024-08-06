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
    
def printList(head):
    while head:
        print(head.val,end = " ")
        head = head.next
    print()


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next 
        pass






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
        