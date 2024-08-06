from typing import List,Optional
import sys
class Solution:
    # def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    #     map = dict()
    #     for i in range(len(names)):
    #         map[names[i],i] =  heights[i]
    #     map = dict(sorted(map.items(),key=lambda x:-x[1]))

    #     i = 0
    #     for key in map:
    #         names[i] = key[0]
    #         i+=1
    #     return names

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            maxi = i
            for j in range(i,n):
                if(heights[maxi]<heights[j]):maxi = j
            heights[i],heights[maxi] = heights[maxi],heights[i]
            names[i],names[maxi] = names[maxi],names[i]
        return names

# time complexity: O(nlogn),O(n^2)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        names = input().strip().split()
        heights = list(map(int,input().strip().split()))
        print(Solution().sortPeople(names,heights))