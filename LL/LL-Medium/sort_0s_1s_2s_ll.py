#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    def segregate(self, head):
        # mover = head
        # cnt0, cnt1, cnt2 = 0,0,0
        # while(mover):
        #     if(mover.data==0):cnt0+=1
        #     elif(mover.data==1):cnt1+=1
        #     else:cnt2+=1
        #     mover = mover.next
        
        # cnt = 0
        # mover = head
        # while(mover):
        #     cnt+=1
        #     if(cnt<=cnt0):mover.data = 0
        #     elif(cnt0<cnt<=cnt0+cnt1):mover.data=1
        #     else:mover.data = 2
        #     mover = mover.next
        # return head

        if(head==None or head.next==None):return head
        dummy0 = Node(-1)
        dummy1 = Node(-1)
        dummy2 = Node(-1)

        temp0 = dummy0
        temp1 = dummy1
        temp2 = dummy2

        mover = head
        while(mover):
            if(mover.data==0):
                temp0.next = mover
                temp0 = temp0.next 
            elif(mover.data==1):
                temp1.next = mover
                temp1 = temp1.next  
            else:
                temp2.next = mover
                temp2 = temp2.next
            mover = mover.next

        if(dummy1.next):temp0.next = dummy1.next
        else:temp0.next = dummy2.next
        dummy1.next = None
        temp1.next = dummy2.next
        dummy2.next = None
        temp2.next = None
        return dummy0.next  