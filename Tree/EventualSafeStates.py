from typing import List


class Solution:

    def eventualSafeNodes1(self, graph: List[List[int]]) -> List[int]:
        safes = []

        for index, node in enumerate(graph):
            if node == []:
                safes.append(index)
        for i in range(len(graph)):
            for index, node in enumerate(graph):
                if index in safes:
                    continue
                if not (set(node) - set(safes)):
                    safes.append(index)

        return sorted(safes)




    def eventualSafeNodes2(self, graph: List[List[int]]) -> List[int]:
        lend = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if self.check(graph, i, lend):
                lend[i] = 1
        result = []
        for i in range(len(lend)):
            if lend[i] == 1:
                result.append(i)
        return result

    def check(self, graph, i, lend):
        if lend[i] == 1:
            return True
        if lend[i] == -1:
            return False
        lend[i] = -1
        for j in range(len(graph[i])):
            if not self.check(graph, graph[i][j], lend):
                return False
        lend[i] = 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.eventualSafeNodes1([[1,2],[2,3],[5],[0],[5],[],[]]))
    print(s.eventualSafeNodes1([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
    print(s.eventualSafeNodes1([[0],[2,3,4],[3,4],[0,4],[]]))

    print(s.eventualSafeNodes2([[1,2],[2,3],[5],[0],[5],[],[]]))
    print(s.eventualSafeNodes2([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
    print(s.eventualSafeNodes2([[0],[2,3,4],[3,4],[0,4],[]]))
