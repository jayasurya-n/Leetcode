class Solution:
    def countSubSequences(self,arr,index,currentSum,target):
        if(currentSum>target):return 0
        if(index==len(arr)):
            if(currentSum==target):return 1
            else:return 0
        
        cnt1 =  self.countSubSequences(arr,index+1,currentSum+arr[index],target)
        cnt2 =  self.countSubSequences(arr,index+1,currentSum,target)

        return cnt1+cnt2
    
    def perfectSum(self, arr, n, sum):
        currentSum = 0
        index = 0
        return self.countSubSequences(arr,index,currentSum,sum)


arr = list(map(int,input().strip().split()))
target = int(input().strip()) 
print(Solution().perfectSum(arr,len(arr),target))