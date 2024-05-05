class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # time: O(M*N), for traversing all queries (with each queries potentially needing to traverse entire grpah).
        # M = number of queries, N = number of equations.
        # space: O(N), number of equations for building the graph out

        graph = defaultdict(defaultdict)

        def dfs(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = dfs(neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # 1. Build graph, with graph[A][B] represents the value of A/B, also means A points to B.
        # graph[A] returns all the node A points to.
        # time: O(N), N = number of equations
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # 2. Traverse queries, each queries might need to traverse the entire graph
        # time: O(M * N), M to traverse all equations, and N for traverse entire graph
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0
            elif dividend == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = dfs(dividend, divisor, 1, visited)
            results.append(ret)
        return results