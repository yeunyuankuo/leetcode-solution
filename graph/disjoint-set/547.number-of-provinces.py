class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)

        # Initial root for each node be itself
        root = [i for i in range(n)]
        print(root)
        
        # The initial "rank" or connected nodes of each vertex is 1
        # assuming all node are not connected
        rank = [1] * n

        # The find function here is the same as that in the disjoint set with path compression.
        def find(node):
            # path compression
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node


        # The union function with union by rank
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            # both nodes already in same set; no union needed
            if r1 == r2:
                return 0

            if rank[r1] < rank[r2]:
                root[r1] = r2
                rank[r2] += rank[r1]
            else:
                root[r2] = r1
                rank[r1] += rank[r2]
            return 1

        res = n
        for n1 in range(n):
            for n2 in range(n1, n):
                if isConnected[n1][n2] == 1:
                    res -= union(n1, n2)
        return res
                