"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # current = head
        # hashDict = {}
        # while(current):
        #     newNode = Node(current.data,None,None)
        #     hashDict[current] = newNode
        #     current = current.next 
        # hashDict[None] = None

        # current = head
        # while(current):
        #     copy = hashDict[current]
        #     copyNext = hashDict[current.next]
        #     copyRandom = hashDict[current.random]

        #     copy.next = copyNext
        #     copy.random = copyRandom
        #     current = current.next 
        # return hashDict[head]

        current = head
        while(current):
            copy = Node(current.data,None,None)
            front = current.next
            copy.next = front
            current.next = copy
            current = front
        
        # Random Pointers connection
        # Cannot do next pointers connection in this traversal
        current = head
        while(current):
            originalRandom = current.random
            copy = current.next
            if(originalRandom):copy.random = originalRandom.next
            else:copy.random = None
            current = current.next.next
        
        # Next Pointers connection
        current = head
        newHead = head.next
        while(current):
            originalNext = current.next.next
            copy = current.next
            if(originalNext):copy.next = originalNext.next
            else:copy.next = None
            current.next = originalNext
            current = originalNext
            
        return newHead

        # temp = head
        # dummyNode = Node(-1)
        # res = dummyNode

        # while temp:
        #     res.next = temp.next
        #     res = res.next

        #     temp.next = temp.next.next
        #     temp = temp.next

        # return dummyNode.next

