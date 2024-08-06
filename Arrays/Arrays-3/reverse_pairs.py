class Solution:
    
    
    def reversePairs(self, nums: list[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)


    def cntPairs(self,arr,low,mid,high):
        i = low
        right = mid+1
        pairs = 0

        while(i<=mid):
            for j in range(right,high+1):
                if(arr[i]<=2*arr[j]):
                    right = j
                    break
            
            pairs+= right-(mid+1)
            i+=1

        # i = low
        # j = mid+1
        # pairs = 0
        # while(i<=mid):
        #     while(j<=high and arr[i]>2*arr[j]):j+=1
        #     pairs+=j-(mid+1)
        #     i+=1
            
        return pairs


    def mergeSort(self,arr:list,low:int,high:int):
        cnt = 0
        if(low>=high):return cnt
        mid = (high+low)//2
        cnt+=self.mergeSort(arr,low,mid)
        cnt+=self.mergeSort(arr,mid+1,high)
        cnt+=self.cntPairs(arr,low,mid,high)
        self.merge(arr,low,mid,high)
        return cnt

    def merge(self,arr,low,mid,high):
        merged = [0 for i in range(high-low+1)]
        i = low
        j = mid+1
        k = 0
        
        while(i<=mid and j<=high):

            if(arr[i]<=arr[j]):
                merged[k] = arr[i]
                i+=1
                k+=1
                
            else:
                merged[k] = arr[j]
                j+=1
                k+=1
        
        while(i<=mid):
            merged[k] = arr[i]
            i+=1
            k+=1

        while(j<=high):
            merged[k] = arr[j]
            j+=1
            k+=1
        
        for k in range(0,len(merged)):
            arr[low+k] = merged[k]
        



    

nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.reversePairs(nums))
# print(nums)