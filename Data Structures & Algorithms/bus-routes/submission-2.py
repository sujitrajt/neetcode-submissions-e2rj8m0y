class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        bus_stops = {}
        for i,route in enumerate(routes):
            for stop in route:
                if stop not in bus_stops:
                    bus_stops[stop] = []
                bus_stops[stop].append(i)
        
        if source not in bus_stops:
            return -1
            
        visited = set()
        queue = deque()
        for bus in bus_stops[source]:
            queue.append((bus,1))
            visited.add(bus)
        while queue:
            cur_bus, num_changes = queue.popleft()
            for stop in routes[cur_bus]:
                if stop == target:
                    return num_changes
                for connected_bus in bus_stops[stop]:
                    if connected_bus not in visited:
                        queue.append((connected_bus, num_changes+1))
                        visited.add(connected_bus)
        return -1
