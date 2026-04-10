class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        queue = deque()
        graph = defaultdict(list)

        for src,dest in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)
        
        # print(queue)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        return count == numCourses
                