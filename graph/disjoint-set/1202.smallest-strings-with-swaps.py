class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        size = len(s)
        root = [i for i in range(size)]
        rank = [1 for _ in range(size)]

        def find(node):
            while root[node] != node:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return 0
            if rank[r1] < rank[r2]:
                root[r1] = r2
                rank[r2] += rank[r1]
            else:
                root[r2] = r1
                rank[r1] += rank[r2]
            return 1

        for p in pairs:
            union(p[0], p[1])

        # Grouping
        # chars that are connected will be put in the same group along with their indexes
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)
        print(group)

		# Sorting
        # sort each groups indexes and chars in lexicogrphic order
        # then, build the result string with sorted char for that corresponding index
        res = [''] * size
        for ids, chars in group.values():
            ids.sort()
            print(ids)
            chars.sort()
            print(chars)
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)