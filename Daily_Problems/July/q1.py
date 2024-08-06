from typing import List,Optional
import sys
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        while(i<n):
            if(arr[i]%2==0):i+=1
            else:
                if(i+2<n and (arr[i+1]%2==1) and (arr[i+2]%2==1)):
                    return True
                i+=1
        return False


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().threeConsecutiveOdds(arr))