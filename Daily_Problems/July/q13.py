from typing import List,Optional
import sys
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        healthPair = dict(zip(positions,healths))
        directionPair = list(zip(positions,directions))

        directionPair.sort(key=lambda x:x[0])

        stack = []

        for i in range(len(directionPair)):
            if(not stack or directionPair[i][1]=='R' or stack[-1][1]=='L'):
                stack.append(directionPair[i])
            else:
                while(stack and stack[-1][1]=='R'):
                    top = stack.pop()
                    health1 = healthPair[top[0]]
                    health2 = healthPair[directionPair[i][0]]
                    # print(stack,health1,health2)

                    if(health1<health2):
                        healthPair[top[0]] = 0
                        healthPair[directionPair[i][0]]-=1
                    
                    if(health1>health2):
                        healthPair[top[0]]-=1
                        healthPair[directionPair[i][0]] = 0
                        stack.append(top)
                        break
                    elif(health1==health2):
                        healthPair[top[0]] = 0
                        healthPair[directionPair[i][0]] = 0
                        break

                if(not stack):stack.append(directionPair[i])       
        
        ans = []
        for i in healthPair:
            if(healthPair[i]!=0):
                ans.append(healthPair[i])

        return ans


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        positions = list(map(int,input().strip().split()))
        healths = list(map(int,input().strip().split()))
        directions = input().strip()
        print(Solution().survivedRobotsHealths(positions,healths,directions))