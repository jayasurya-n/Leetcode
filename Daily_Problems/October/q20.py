from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def parseBoolExpr(self, expression: str) -> bool:
    #     stack = []
        
    #     for ch in expression:
    #         if(ch==')'):
    #             operands = []
    #             while stack and stack[-1]!='(':
    #                 operands.append(stack.pop())
    #             stack.pop()
                
    #             operator = stack.pop()
                
    #             if operator=='!':
    #                 ans = 't' if operands[0]=='f' else 'f'
    #             elif operator=='|':
    #                 ans = 'f'
    #                 for op in operands:
    #                     if(op=='t'):ans = 't'
    #             else:
    #                 ans = 't'
    #                 for op in operands:
    #                     if(op=='f'):ans = 'f'
                
    #             stack.append(ans)
            
    #         elif ch!=',':stack.append(ch)
        
    #     return stack[-1]=='t'

    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(index,expression):
            curr = expression[index[0]]
            index[0] += 1
            
            if(curr=='t'):return True
            if(curr=='f'):return False
            if(curr=='!'):
                index[0]+=1
                result = not evaluate(index,expression)
                index[0]+=1
                return result
            
            operands=[]
            index[0]+=1
            while(expression[index[0]]!=')'):
                if(expression[index[0]]!=","):operands.append(evaluate(index,expression))
                else:index[0]+=1
            index[0]+=1
            
            if(curr=='&'):return all(operands)
            if(curr=='|'):return any(operands)
    
        index = [0]
        return evaluate(index,expression)
                
            
# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))