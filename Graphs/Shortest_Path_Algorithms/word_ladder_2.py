from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        q = deque([[beginWord]])
        hash = set(wordList)
        if beginWord in hash:hash.remove(beginWord)
        
        ans = []
        while q:
            size = len(q)
            usedWords = []
            for _ in range(size):
                previousWords = q.popleft()
                word = previousWords[-1]
                
                if(word==endWord):
                    if(len(ans)==0):ans.append(previousWords)
                    elif(len(previousWords)==len(ans[0])):ans.append(previousWords)
                
                for i in range(len(word)):
                    for j in range(97,123):
                        newWord = word[:i]+chr(j)+word[i+1:]
                        if(newWord in hash):
                            previousWords.append(newWord)
                            q.append(previousWords[:])
                            usedWords.append(newWord)
                            previousWords.pop()
                            
            for i in range(len(usedWords)):
                if(usedWords[i] in hash):hash.remove(usedWords[i])
        return ans
     
# time complexity: O(varies from input to input)
# space complexity: O(varies from input to input)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        beginWord = input().strip()
        endWord = input().strip()
        wordList = input().strip().split()
        print(Solution().findLadders(beginWord,endWord,wordList))