class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # time: O(V + E * a(N))
        # space: O(V)
        roots = [i for i in range(n)]
        ranks = [1] * n

        def find(node):
            while node != roots[node]:
                roots[node] = roots[roots[node]]
                node = roots[node]
            return node

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return 0

            if ranks[r1] < ranks[r2]:
                roots[r1] = r2
                ranks[r2] += ranks[r1]
            else:
                roots[r2] = r1
                ranks[r1] += ranks[r2]
            return 1

        res = n
        for e in edges:
            res -= union(e[0], e[1])
        return res