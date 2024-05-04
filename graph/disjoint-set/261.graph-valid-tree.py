class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        def find(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node
        
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            
            if r1 == r2:
                # When constructing a tree using the union-find algorithm,
                # adding an edge between two nodes essentially joins two
                # components together. However, if adding an edge between
                # two nodes that already belong to the same component, it 
                # indicates a cycle, making the structure not a tree.
                return -1
            
            if rank[r1] < rank[r2]:
                root[r1] = r2
                rank[r2] += rank[r1]
            else:
                root[r2] = r1
                rank[r1] += rank[r2]
            return 1
        
        res = n
        for e in edges:
            val = union(e[0], e[1])
            if val == -1:
                return False
            res -= val
        
        return res == 1