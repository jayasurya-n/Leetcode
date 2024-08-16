from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]):
        q = deque([(beginWord,1)])
        hash = set(wordList)
        if beginWord in hash:hash.remove(beginWord)
        
        while q:
            size = len(q)
            for _ in range(size):
                word,level = q.popleft()
                if(word==endWord):return level
                
                for i in range(len(word)):
                    for j in range(97,123):
                        newWord = word[:i]+chr(j)+word[i+1:]
                        if(newWord in hash):
                            hash.remove(newWord)
                            q.append((newWord,level+1))
        return 0
     
# time complexity: O(nm)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        beginWord = input().strip()
        endWord = input().strip()
        wordList = input().strip().split()
        print(Solution().ladderLength(beginWord,endWord,wordList))