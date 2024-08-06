'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        hash = set()
        # mover = head
        # while(mover):
        #     if(mover.data in hash):
        #         back = mover.prev
        #         front = mover.next
            
        #         back.next = front
        #         if(front):front.prev = back
                
        #         mover.next = None
        #         mover.prev = None
        #         mover = front
        #     else:
        #         hash.add(mover.data)
        #         mover = mover.next
        # return head


        mover = head
        while(mover):
            front = mover.next
            while(front and front.data==mover.data):
                duplicate = front
                front = front.next
                duplicate.next = None
                duplicate.prev = None
            mover.next = front
            if(front):front.prev = mover
            mover = mover.next
        return head