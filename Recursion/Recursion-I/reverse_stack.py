class Solution:
    def reverse(self,stack):
        # Base Case: If stack is not empty
        if(len(stack)>0):
            temp  = stack.pop()
            self.reverse(stack)
            self.sortInsertAtEnd(stack,temp)
    
    def sortInsertAtEnd(self,stack,element):
        if(len(stack)==0):
            stack.append(element)
        else:
            temp = stack.pop()
            self.sortInsertAtEnd(stack,element)
            stack.append(temp)




stack = list(map(int,input().strip().split()))
Solution().reverse(stack)
print(stack)