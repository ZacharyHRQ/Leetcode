class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        def dfs(v,t):
            if v not in seen:
                seen.add(v)
                if v == t: return True
                return any(dfs(i,t) for i in d[v])
        for u,v in edges:
            seen = set()
            if u in d  and v in d and dfs(u,v):
                return [u,v]
            d[u].add(v)
            d[v].add(u)
            