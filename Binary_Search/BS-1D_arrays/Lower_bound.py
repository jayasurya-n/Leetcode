class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        low = 0
        high = N-1
        ans = -1
        while(low<=high) : 
            mid = (low+high)//2

            if(A[mid]<=X):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        
        return ans

        # return A[ans] if ans!=-1 else -1


            




x = int(input())
nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.findFloor(nums,len(nums),x))