from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq
        
class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp,tweetId))
        self.timestamp+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        
        for timestamp,tweetId in self.tweets[userId][-10:]:
            if(len(minHeap)>=10):heapq.heappop(minHeap)
            heapq.heappush(minHeap,(timestamp,tweetId))
        
        for user in self.following[userId]:
            for timestamp,tweetId in self.tweets[user][-10:]:
                if(len(minHeap)>=10):heapq.heappop(minHeap)
                heapq.heappush(minHeap,(timestamp,tweetId))
        
        return [tweetId for _,tweetId in sorted(minHeap,reverse=True)]
                 
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if(followerId!=followeeId):self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId!=followeeId and followeeId in self.following[followerId]):
            self.following[followerId].remove(followeeId)
        

# time complexity: O(1),O(Flog10),O(1),O(1)
# space complexity: O(U+T)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))