# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites ):
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for ai, bi in prerequisites:
            adj[bi].append(ai)
            indegree[ai] += 1
        
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        result = []

        while queue:
            course = queue.pop(0)
            result.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) == numCourses:
            print(result)
        else:
            print([])

def main():
    import ast
    numCourses, prerequisites = int(input()), ast.literal_eval(input())
    solution = Solution()
    solution.findOrder(numCourses=numCourses,prerequisites=prerequisites)

if __name__ == '__main__':
    main()

'''
4
[[3,2],[1,0],[2,0],[3,1]]
[0, 1, 2, 3]
'''
