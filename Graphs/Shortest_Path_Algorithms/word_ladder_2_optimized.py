from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        q = deque([beginWord])
        hash = set(wordList)
        if beginWord in hash:hash.remove(beginWord)
        
        map = dict()
        map[beginWord] = 1
        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                if(word==endWord):break
                
                level = map[word]
                for i in range(len(word)):
                    for j in range(97,123):
                        newWord = word[:i]+chr(j)+word[i+1:]
                        if(newWord in hash):
                            hash.remove(newWord)
                            map[newWord] = level+1
                            q.append(newWord)
            
        def backtrack(word,cur):
            if(word==beginWord):
                ans.append(cur[::-1])
                return 
            
            level = map[word]
            for i in range(len(word)):
                for j in range(97,123):
                    newWord = word[:i]+chr(j)+word[i+1:]
                    if(newWord in map and map[newWord]==level-1):
                        cur.append(newWord)
                        backtrack(newWord,cur)
                        cur.pop()
            
        ans = []
        cur = [endWord]
        if(endWord in map):backtrack(endWord,cur)
        return ans
    
    
# time complexity: O(varies from input to input)
# space complexity: O(varies from input to input)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        beginWord = input().strip()
        endWord = input().strip()
        wordList = input().strip().split()
        print(Solution().findLadders(beginWord,endWord,wordList))