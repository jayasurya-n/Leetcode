#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    # def reverseLL(self, head):

    #     # if(head==None or head.next==None):
    #     #     return head
    #     # newHead = self.reverseLL(head.next)
    #     # front = head.next
    #     # front.next = head
    #     # head.next = None
    #     # return newHead 
        
    #     prev = None
    #     current = head

    #     while(current):
    #         front = current.next
    #         current.next = prev
    #         prev = current
    #         current = front
    #     return prev
    
    # def addOne(self,head):
        
    #     newHead = self.reverseLL(head)
        
    #     carry = 1
    #     mover = newHead
    #     while(mover):
            
    #         sum = mover.data+carry
    #         mover.data = sum%10
    #         carry = sum//10
    #         if(carry==0):break
    #         mover = mover.next
        
    #     head = self.reverseLL(newHead)
    #     if(carry):
    #         newNode = Node(carry)
    #         newNode.next = head
    #         head = newNode
        
    #     return head

    def recursive(self,head):
        if(head==None):return 1
        carry = self.recursive(head.next)
        sum = head.data+carry
        head.data = sum%10
        carry = sum//10
        return carry

    def addOne(self,head):
        carry = self.recursive(head)
        if(carry):
            newNode = Node(1)
            newNode.next = head
            return newNode
        return head