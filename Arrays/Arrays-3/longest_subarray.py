class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        
        # prefixSum = 0
        # dict =  {}
        # ans = 0
        # dict[prefixSum] = 0
        # for i in range(0,n):
        #     prefixSum+=arr[i]
        #     prefixSumEarlier = prefixSum-k
        #     if(prefixSumEarlier in dict):
        #         ans = max(ans,i+1-dict[prefixSumEarlier])
                
        #     if(prefixSum not in dict):
        #         dict[prefixSum] = i+1
        # return ans

        i,j = 0,0
        n = len(arr)
        sum = 0
        ans = 0
        while(j<n):
            sum+=arr[j]
            if(sum==k):ans = max(ans,j-i+1)   
            while(sum>k):
                sum-=arr[i]
                i+=1
            j+=1

        return ans
                        
        
k = int(input())
nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.lenOfLongSubarr(nums,len(nums),k))


