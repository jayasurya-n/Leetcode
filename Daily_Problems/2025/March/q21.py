from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # n = len(recipes)
        # hash_supplies = set(supplies)
                
        # adj = defaultdict(list)
        # for i,recipe in enumerate(recipes):
        #     adj[recipe] = ingredients[i]
        

        # def dfs(recipe,pathVisited,memo):
        #     if(recipe in hash_supplies):return True
        #     if(recipe not in adj):return False
            
        #     if(recipe in memo):return memo[recipe]
            
        #     pathVisited.add(recipe)
        #     for v in adj[recipe]:
        #         if(v in pathVisited):return False
        #         if(not dfs(v,pathVisited,memo)):
        #             memo[recipe] = False
        #             pathVisited.remove(recipe)
        #             return False
        #     pathVisited.remove(recipe)
        #     memo[recipe] = True
        #     return True 
        
        # memo = {}
        # pathVisited = set()
        # ans = []
        # for recipe in recipes:
        #     if(dfs(recipe,pathVisited,memo)):ans.append(recipe)
        # return ans
        
        # # memo = {}
        # # pathVisited = set()
        # # for recipe in recipes:
        # #     if(recipe not in memo):dfs(recipe,pathVisited,memo)
        
        # # ans = []
        # # for recipe in recipes:
        # #     if(recipe in memo and memo[recipe]):ans.append(recipe)
        # # return ans

 
        n = len(recipes)
        hash_supplies = set(supplies) 
        hash_recipe = defaultdict(int)
        for i,recipe in enumerate(recipes):hash_recipe[recipe] = i
        
        adj = defaultdict(list) 
        indegree = [0]*n
        for i,recipe in enumerate(recipes):
            for ingre in ingredients[i]:
                if(ingre not in hash_supplies):
                    adj[ingre].append(recipe)
                    indegree[i]+=1
        
        q = deque([])
        for i in range(n):
            if(indegree[i]==0):q.append(i)
        
        ans = []
        while q:
            ind = q.popleft()
            ans.append(recipes[ind])
            for v in adj[recipes[ind]]:
                indegree[hash_recipe[v]]-=1
                if(indegree[hash_recipe[v]]==0):q.append(hash_recipe[v])
        return ans
        
# time complexity: O(n+m+s),O(n+m+s)
# space complexity: O(n+m),O(n+m)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))