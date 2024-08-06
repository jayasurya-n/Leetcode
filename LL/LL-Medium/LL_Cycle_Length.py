# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    slow,fast = head, head
    while(fast!=None and fast.next!=None):
        slow = slow.next
        fast = fast.next.next
        if(slow==fast):
            meet = slow
            cnt = 1
            slow = slow.next            
            while(slow!=meet):
                cnt+=1
                slow = slow.next
            return cnt
    
    return 0