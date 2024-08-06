from typing import List
class Solution:
    def sumSubarrayMins(self, N, fruits):
        i,j = 0,0
        ans = 0
        hash = {}
        # while(j<len(fruits)):
        #     hash[fruits[j]] = hash.setdefault(fruits[j],0)+1
        #     while(len(hash)>2):
        #         hash[fruits[i]]-=1
        #         if(hash[fruits[i]]==0):del hash[fruits[i]]
        #         i+=1
        #     ans = max(ans,j-i+1)
        #     j+=1
        # return ans

        while(j<len(fruits)):
            hash[fruits[j]] = hash.setdefault(fruits[j],0)+1
            if(len(hash)>2):
                hash[fruits[i]]-=1
                if(hash[fruits[i]]==0):del hash[fruits[i]]
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans

            


# time complexity: O(2n) first case, O(n) in second case
# space complexity: O(1) in both cases as the dictionary takes only 3 elements at max 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        fruits = list(map(int,input().strip().split()))
        print(Solution().sumSubarrayMins(n,fruits))