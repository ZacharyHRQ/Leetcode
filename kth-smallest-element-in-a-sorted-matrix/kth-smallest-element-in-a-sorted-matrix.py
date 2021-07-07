class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        for i in matrix:
            for v in i:
                a.append(v)
                
        a.sort()
        return a[k-1]