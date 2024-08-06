from typing import List,Optional
import sys
class Solution:
    def findOperations(self,index,currentSum,prev,temp,ans,s,target):
        if(index==len(s)):
            if(currentSum==target):
                ans.append("".join(temp[:]))
            return
        

        for i in range(index,len(s)):
            if(i!=index and s[index]=='0'):break
            currentOperand = s[index:i+1]
            val = int(currentOperand)
            if(index==0):
                temp.append(currentOperand)
                self.findOperations(i+1,val,val,temp,ans,s,target)
                temp.pop()
            else:
                for op in ['+','-','*']:
                    temp.append(op)
                    temp.append(currentOperand)
                    if(op=='+'):self.findOperations(i+1,currentSum+val,val,temp,ans,s,target)
                    elif(op=='-'):self.findOperations(i+1,currentSum-val,-val,temp,ans,s,target)
                    else:self.findOperations(i+1,currentSum-prev+prev*val,prev*val,temp,ans,s,target)
                    temp.pop()
                    temp.pop()
        
        
            
    def addOperators(self, s: str, target: int) -> list[str]:
        ans = []
        self.findOperations(0,0,0,[],ans,s,target)
        return ans


# time complexity: O(n*4^n)
# space complexity: O(n+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        target = int(input().strip())
        print(Solution().addOperators(s,target))
