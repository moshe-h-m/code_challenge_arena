from typing import List


def add_edge(nodes_dict, edge):
    if edge[1] not in nodes_dict:
        nodes_dict[edge[1]] = [edge[0]]
    else:
        nodes_dict[edge[1]].append(edge[0])
    return nodes_dict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        nodes_dict = {}

        for edge in prerequisites:
            nodes_dict = add_edge(nodes_dict, edge)
        print(nodes_dict)

    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     lend = [0 for i in range(numCourses)]
    #     for i in range(len(prerequisites)):
    #         if prerequisites[i][0] == prerequisites[i][1]:
    #             return False
    #         lend[prerequisites[i][0]] += 1
    #     print(lend)
    #     for i in range(len(lend)):
    #         if lend[i] == 0:
    #             return True
    #     return False


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
    print(s.canFinish(2, [[1, 0]]))
    print(s.canFinish(2, [[1, 0], [0, 1]]))
    print(s.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
    s.canFinish(3, [[1,0],[0,1]])
    s.canFinish(3, [[1,0],[0,2],[2,1]])
    s.canFinish(3, [[1,0],[0,2],[2,1],[1,2]])
    s.canFinish(3, [[1,0],[0,2],[2,1],[1,2],[2,0]])