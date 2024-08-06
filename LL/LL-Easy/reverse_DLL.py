#User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if(head==None):return head
        
        # current = head
        # finalHead = None
        # while(current!=None):
        #     front = current.next
        #     current.next = current.prev
        #     current.prev = front
        #     if(current.prev==None):finalHead = current
        #     current = current.prev
        # return finalHead

        current = head
        last  = None
        while(current!=None):
            last = current.prev
            current.prev  = current.next
            current.next = last
            current = current.prev
        return last.prev            