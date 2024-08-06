class Solution:
    cnt = 0
    ans = ""
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i+1 for i in range(n)]
        factorial = 1
        for i in range(1,n):
            factorial*=i

        k-=1
        ans = []
        while(nums):
            block = int(k//factorial)
            ans.append(nums[block])
            k %= factorial
            if(len(nums)>1):factorial = factorial/(len(nums)-1)
            nums.remove(nums[block])
        
        return "".join(str(i) for i in ans)


# time complexity: O(n^2)  
# space complexity: O(n)  
n,k  = list(map(int,input().strip().split()))
print(Solution().getPermutation(n,k))       
        