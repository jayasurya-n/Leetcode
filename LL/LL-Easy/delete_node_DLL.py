#User function Template for python3

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteNode(self,head, x):
        # Code here
        if(head==None or head.next==None):
            return None
        
        
        if(x==1):
            back = head
            head = head.next
            
            head.prev = None
            back.next = None
           
            return head
        
        cnt = 0
        mover = head
        
        while(mover!=None):
            cnt+=1
            if(cnt==x):break
            mover = mover.next
        
        back = mover.prev
        front = mover.next

        back.next = front
        if(front!=None):front.prev = back
        
        mover.next = None
        mover.prev = None
