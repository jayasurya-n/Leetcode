class Solution:
    def findCombination(self,index,digits,store,ans,mapping):
        if(len(digits)==0):return []
        if(index==len(digits)):
            s = "".join(store[:])
            ans.append(s)
            return

        for i in mapping[int(digits[index])]:
            self.findCombination(index+1,digits,store+[i],ans,mapping)

    def letterCombinations(self, digits: str) -> list[str]:
        ans,store = [],[]
        mapping = [[],[]]
        for i in range(2,10):
            if i==2:mapping.append(['a','b','c'])
            elif i==3:mapping.append(['d','e','f'])
            elif i==4:mapping.append(['g','h','i'])
            elif i==5:mapping.append(['j','k','l'])
            elif i==6:mapping.append(['m','n','o'])
            elif i==7:mapping.append(['p','q','r','s'])
            elif i==8:mapping.append(['t','u','v'])
            elif i==9:mapping.append(['w','x','y','z'])

        self.findCombination(0,digits,store,ans,mapping)
        return ans


# time complexity: O(3^len(digits))  
# space complexity: O(len(digits)) 
digits = input().strip()
print(Solution().letterCombinations(digits))