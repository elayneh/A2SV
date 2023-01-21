#!/usr/bin/python3
"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""
class Solution:
    # The goal is to flip all outgoing path from 0
    # Therefore, we can BFS from 0, starting with an undirected graph
    # When we build the graph, we also record the edge id
    # So later when we BFS, we also ask if the edge we use is forward going or reversed. If it is forward going, we add 1 to the res
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        for i, connection in enumerate(connections):
            u, v = connection
            graph[u].add((v, i))
            graph[v].add((u, i))

        dq, res = deque(), 0
        visited = [False for i in range(n)]
        dq.append(0)
        visited[0] = True
        while dq:
            node = dq.popleft()
            for nxt, ind in graph[node]:
                if not visited[nxt]:
                    if connections[ind] == [node, nxt]:
                        res += 1
                    dq.append(nxt)
                    visited[nxt] = True
        return res
