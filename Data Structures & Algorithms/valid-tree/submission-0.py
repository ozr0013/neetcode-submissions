class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # We have to make sure that this tree does not have a triangular loop
        preMap = {i:[]for i in range(n)}
        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        if not n:
            return True
        visit = set()
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for j in preMap[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
        






        