class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,p in flights:
            graph[u].append((v,p))
        
        heap = [(0,src,0)]
        best = {}

        while heap:
            cost,city,stops = heapq.heappop(heap)

            #if city is dest
            if city == dst:
                return cost
            
            #if k is >
            if stops > k:
                continue
            
            if (city,stops) in best and best[(city,stops)] <= cost:
                continue
            
            best[(city,stops)] = cost
            for nei,price in graph[city]:
                new_cost = cost + price

                heapq.heappush(heap, (new_cost,nei,stops+1))
        return -1 