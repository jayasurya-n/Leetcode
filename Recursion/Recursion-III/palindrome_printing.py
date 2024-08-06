class Solution:
    def isPalindrome(self,s,start,end):
        i = start
        j = end
        while(i<j):
            if(s[i]!=s[j]):return False
            i+=1
            j-=1
        return True

    def findPalindromes(self,index,s,store,ans):
        if(index ==len(s)):
            ans.append(store[:])
            return

        for i in range(index,len(s)):
            if(self.isPalindrome(s,index,i)):
                self.findPalindromes(i+1,s,store+[s[index:i+1]],ans)
        
    def partition(self, s: str) -> list[list[str]]:
        ans,store = [],[]
        index = 0
        self.findPalindromes(index,s,store,ans)
        return ans

# time complexity: O((2^n)*k*(n/2)), k is average length of palindrome  
# space complexity: O(n) + O(n)(stack space) 
s = input().strip()
print(Solution().partition(s))