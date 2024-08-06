from typing import List,Optional
import sys
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prevFinishTime = customers[0][0]
        waitingTime = 0
        for i in range(len(customers)):
            start = customers[i][0]
            time = customers[i][1]
            if(prevFinishTime>start):
                waitingTime+=prevFinishTime-start
                start = prevFinishTime
            waitingTime+=time
            prevFinishTime = start+time
        return waitingTime/len(customers)





# time complexity: O(n)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        customers = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().averageWaitingTime(customers))