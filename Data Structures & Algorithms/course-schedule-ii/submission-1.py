class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()


        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        order = []
        while queue:
            course = queue.popleft()
            order.append(course)

            for nei in graph[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        return order if len(order) == numCourses else []
