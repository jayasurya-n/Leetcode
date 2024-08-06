from typing import List
import sys
class Solution:
    def maximumMeetings(self,n,start,end):
        meetings = []
        for i in range(len(start)):
            meetings.append([start[i],end[i],i+1])
        meetings.sort(key=lambda x:(x[1],i))
        print(meetings)
        endTime = -1
        ans = 0
        for i in range(len(meetings)):
            if(endTime<meetings[i][0]):
                endTime = meetings[i][1]
                ans+=1
        return ans

# time complexity: O(n+nlogn+n
# space complexity: O(n)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        print(Solution().maximumMeetings(n,start,end))