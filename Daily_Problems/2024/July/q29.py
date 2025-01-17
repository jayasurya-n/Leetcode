from typing import List,Optional
from collections import deque
import sys
class Solution:
    def numTeams(self, rating: List[int]):
        n = len(rating)
        teams = 0

        increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]

        for i in range(n):
            increasing_teams[i][1] = 1
            decreasing_teams[i][1] = 1

        for count in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] += increasing_teams[i][count - 1]
                    if rating[j] < rating[i]:
                        decreasing_teams[j][count] += decreasing_teams[i][count - 1]

        for i in range(n):
            teams += increasing_teams[i][3] + decreasing_teams[i][3]
        return teams


# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        rating = list(map(int,input().strip().split()))
        print(Solution().numTeams(rating))