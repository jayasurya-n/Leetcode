class Solution:
    def Sorted(self, stack):
        # Base Case: If stack is not empty
        if(len(stack)>0):
            temp  = stack.pop()
            self.Sorted(stack)
            self.sortInsert(stack,temp)
    
    def sortInsert(self,stack,element):
        if(len(stack)==0 or stack[-1] < element):
            stack.append(element)
        
        else:
            temp = stack.pop()
            self.sortInsert(stack,element)
            stack.append(temp)



stack = list(map(int,input().strip().split()))
Solution().Sorted(stack)
print(stack)