class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:(x[0],x[1]))

        answer = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if (answer == []) or (start > answer[-1][1]):
                answer.append([start, end])

            else:
                answer[-1][1] = max(end,answer[-1][1])
         
        return answer
                


        
n = int(input())
intervals = []
for i in range(n):
    intervals.append([int(x) for x in input().strip().split()])
obj = Solution()
print(obj.merge(intervals))