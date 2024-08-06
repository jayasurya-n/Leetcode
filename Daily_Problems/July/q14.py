from typing import List,Optional
import sys
class Solution:
    # def countOfAtoms(self, formula: str) -> str:
    #     n = len(formula)
    #     i = 0
    #     stack = [{}]

    #     while(i<n):
    #         if(formula[i]=='('):
    #             stack.append({})
    #             i+=1
    #         elif(formula[i]==')'):
    #             top = stack.pop()
    #             multiplier = ""
    #             i+=1
    #             while(i<n and formula[i].isdigit()):
    #                 multiplier+=formula[i]
    #                 i+=1
    #             if(multiplier):
    #                 multiplier=int(multiplier)
    #                 for atom in top:
    #                     top[atom]*=multiplier
                
    #             for  atom in top:
    #                 stack[-1][atom] = stack[-1].get(atom,0)+top[atom]
    #         else:
    #             substring = formula[i]
    #             i+=1
    #             while(i<n and formula[i].islower()):
    #                 substring+=formula[i]
    #                 i+=1

    #             multiplier = ""
    #             while(i<n and formula[i].isdigit()):
    #                 multiplier+=formula[i]
    #                 i+=1
    #             if(multiplier):multiplier = int(multiplier)
    #             else:multiplier=1

    #             stack[-1][substring] = stack[-1].get(substring,0)+multiplier
        
    #     ans = dict(sorted(stack[-1].items()))
    #     ans_string = ""

    #     for i in ans:
    #         ans_string+=i
    #         if(ans[i]>1):ans_string+=str(ans[i])
            
    #     return ans_string
    
    def parse(self,index,formula,atomCount):
        n = len(formula)

        while(index<n):
            if(formula[index].isupper()):
                substring = formula[index]
                index+=1
                while(index<n and formula[index].islower()):
                    substring+=formula[index]
                    index+=1
                
                multiplier = ""
                while(index<n and formula[index].isdigit()):
                    multiplier+=formula[index]
                    index+=1


                if(multiplier):multiplier = int(multiplier)
                else:multiplier=1
                atomCount[substring] = atomCount.get(substring,0)+multiplier
            
            elif(formula[index]=='('):
                nested_map = dict()
                index = self.parse(index+1,formula,nested_map)
                index+=1
                multiplier = ""
                while(index<n and formula[index].isdigit()):
                    multiplier+=formula[index]
                    index+=1

                if(multiplier):multiplier = int(multiplier)
                else:multiplier=1

                for atom in nested_map:
                    atomCount[atom] = atomCount.get(atom,0)+nested_map[atom]*multiplier
                
            elif(formula[index]==')'):
                return index

    
    def countOfAtoms(self, formula: str) -> str:
        ans = dict()
        _ = self.parse(0,formula,ans)

        ans = dict(sorted(ans.items()))
        ans_string = ""

        for i in ans:
            ans_string+=i
            if(ans[i]>1):ans_string+=str(ans[i])
            
        return ans_string



# time complexity: O(n^2+nlogn), O(n^2+nlogn)
# space complexity: O(n), O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        formula = input().strip()
        print(Solution().countOfAtoms(formula))