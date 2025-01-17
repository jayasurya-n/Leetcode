from typing import List,Optional
import sys
class Solution:
    # def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    #     ans = 0
    #     ans+=numBottles

    #     while(numBottles>=numExchange):
    #         ans+=numBottles//numExchange
    #         numBottles = numBottles//numExchange + numBottles%numExchange
    #     return ans
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles+(numBottles-1)//(numExchange-1)
        # In every step, x empty bottles are taken away for one full bottl, this means that
        # in total we will get reduced by x-1 bottles for every exchange, and keepping one bottle aside, on 
        # every exhange we can pour water into this bottle and drink, At last, the max remaining bottles can be 
        # (x-2)+1(kept aside) = (x-1) which is less than x 

# time complexity: O(logn) in first solution, O(1) in second solution
# space complexity: O(1) in both cases

t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        numBottles,numExchange = list(map(int,input().strip().split()))
        print(Solution().numWaterBottles(numBottles,numExchange))