from typing import List,Optional
import sys
class Solution:
    # def findTheWinner(self, n: int, k: int) -> int:
    #     arr = [i for i in range(1,n+1)]

    #     last = 0
    #     while(len(arr)>1):
    #         last = int((last+k-1)%len(arr))
    #         arr.pop(last)
    #     return arr[0]

    # def findTheWinner(self, n: int, k: int) -> int:
    #     if(n==1):return 1
    #     winnerFor_nm1 = self.findTheWinner(n-1,k)
    #     ans = (winnerFor_nm1+k)%n
    #     if(ans==0):ans=n
    #     return ans

    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2,n+1):
            winner = (winner+k)%i
            if(winner==0):winner=i
        return winner



# time complexity: O(n^2), O(n), O(n)
# space complexity: O(1),O(n)(stack space), O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,k = list(map(int,input().strip().split()))
        print(Solution().findTheWinner(n,k))