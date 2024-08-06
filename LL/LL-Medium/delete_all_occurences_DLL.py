# Node Class
# class Node:
#     def __init__(self, data): 
#         self.data = data
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        current = head
        while(current):
            if(current.data==x):
                back = current.prev
                front = current.next
                if(back):back.next = front
                else:head = front
                if(front):front.prev = back
                current.next = None
                current.prev = None
                current = front
            else:current = current.next
        return head