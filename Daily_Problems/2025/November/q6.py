import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def processQueries(self, n: int, connections, queries):
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        online = [True]*n
        components = [-1]*n
        hash = defaultdict(list)

        def dfs(u,cnt):
            components[u] = cnt
            heapq.heappush(hash[cnt],u)
            for v in adj[u]:
                if(components[v]==-1):
                    dfs(v,cnt)

        cnt = 0
        for u in range(n):
            if(components[u]==-1):
                cnt+=1
                dfs(u,cnt)
        
        ans = []
        for type,x in queries:
            x-=1
            if(type==2):online[x] = False
            else:
                if(online[x]):ans.append(x+1)
                else:
                    pq = hash[components[x]]
                    while pq and not online[pq[0]]:heapq.heappop(pq)
                    if(not pq):ans.append(-1)
                    else:ans.append(1+pq[0])
        
        return ans
        
# time complexity: O(q+m+nlogn)
# space complexity: O(m+n)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)