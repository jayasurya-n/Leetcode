from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum,righSum = 0,0
        for i in range(k):
            leftSum+=cardPoints[i]
        
        ans = leftSum+righSum
        i = k-1;j = len(cardPoints)-1
        while(i>=0):
            leftSum-=cardPoints[i]
            righSum+=cardPoints[j]
            ans = max(ans,leftSum+righSum)
            i-=1
            j-=1
        return ans

            


# time complexity: O(2k)
# space complexity: O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        cardPoints = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().maxScore(cardPoints,k))