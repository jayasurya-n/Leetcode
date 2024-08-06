class Solution:
    def solve(self,s,k):
        if(len(s)==0 or k==0):return 0

        count = dict()
        start = 0
        ans = 0
        distinct = 0

        for end in range(len(s)):
            count[s[end]] = count.setdefault(s[end],0)+1
            if(count[s[end]]==1):distinct+=1
            
            while(distinct>k):
                count[s[start]]-=1
                if(count[s[start]]==0):distinct-=1
                start+=1
            
            ans+= end-start+1
        return ans

    def substrCount (self,s, k):
        return self.solve(s,k) - self.solve(s,k-1)
    
    # Brute Force - O(N**2)
    # def substrCount (self,s, k):
    #     ans = 0
    #     for i in range(len(s)):
    #         count = [0]*26
    #         distinct = 0
    #         for j in range(i,len(s)):
    #             count[ord(s[j])-ord('a')]+=1
    #             if(count[ord(s[j])-ord('a')]==1):distinct+=1
    #             if(distinct>k):break
    #             if(distinct==k):ans+=1
    #     return ans



s = input()
k = int(input())
print(Solution().substrCount(s,k))