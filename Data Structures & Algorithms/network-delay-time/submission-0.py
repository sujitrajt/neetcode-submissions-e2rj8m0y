class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u ,v, w in times:
            graph[u].append((v,w))
        distances = {k: 0}
        heap = [(0, k)]

        while heap:
            distance,node = heapq.heappop(heap)
            if distance > distances.get(node, float('inf')):
                continue
            
            for nei,wei in graph[node]:
                new_dist = distance + wei
                if new_dist < distances.get(nei, float('inf')):
                    distances[nei] = new_dist
                    heapq.heappush(heap,(new_dist,nei))
        if len(distances) != n:
            return -1
        return max(distances.values())