'''
Class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None



        
'''

# def flatten(root):
#     current = head
#     dummy = Node(-1)
    
#     while(current):
#         prev = dummy
#         left = dummy.bottom
#         right = current
#         front = current.next
#         right.next = None
#         while(left and right):
#             if(left.data<=right.data):
#                 prev.bottom = left
#                 prev = left
#                 left = left.bottom
#             else:
#                 prev.bottom = right
#                 prev = right
#                 right = right.bottom
        
#         if(left):prev.bottom = left
#         if(right):prev.bottom  = right
#         current = front
    
#     return dummy.bottom

def merge(head1,head2):
    dummy = Node(-1)
    prev = dummy
    left = head1
    right = head2
    while(left and right):
        if(left.data<=right.data):
            prev.bottom = left
            prev = left
            left = left.bottom
        else:
            prev.bottom = right
            prev = right
            right = right.bottom
        
    if(left):prev.bottom = left
    if(right):prev.bottom  = right
    return dummy.bottom

def flatten(head):
    if(head==None):return head
    newHead = flatten(head.next)
    return merge(head,newHead)

