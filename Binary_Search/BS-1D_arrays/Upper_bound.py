def getFloorAndCeil(arr, n, x):
    # code here
    arr.sort()
    low = 0
    high = n-1
    ceil = -1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]>=x):
            ceil = arr[mid]
            high = mid-1
        else:
            low = mid+1

    
    low = 0
    high = n-1
    floor = -1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]<=x):
            floor = arr[mid]
            low = mid+1
        else:
            high = mid-1
    
    return floor,ceil
    
    pass


        


            




x = int(input())
nums = [int(x) for x in input().strip().split()]
# obj = Solution()
print(getFloorAndCeil(nums,len(nums),x))