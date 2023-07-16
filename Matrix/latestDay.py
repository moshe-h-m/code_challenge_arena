from typing import List





class Solution:

    lend = []
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.lend = [[0 for i in range(col)] for j in range(row)]
        for i in range(len(cells)):
            self.lend[cells[i][0]-1][cells[i][1]-1] = 1
            if self.check():
                return i+1


    def check(self):
        lend_1 = self.lend
        self.print()
        for i in range(len(lend_1)):
            if lend_1[i][0] == 0:
                if self.check_help(i, 0):
                    return True
            if lend_1[i][len(lend_1[0])-1] == 0:
                if self.check_help(i, len(lend_1[0])-1):
                    return True
        for i in range(len(lend_1[0])):
            if lend_1[0][i] == 0:
                if self.check_help(0, i):
                    return True
            if lend_1[len(lend_1)-1][i] == 0:
                if self.check_help(len(lend_1)-1, i):
                    return True
        return False

    def check_help(self, param, i):
        lend_1 = self.lend
        if param == len(lend_1)-1:
            return True
        if param < 0 or param >= len(lend_1):
            return False
        if i < 0 or i >= len(lend_1[0]):
            return False
        if lend_1[param][i] == 1:
            return False
        lend_1[param][i] = 1
        if self.check_help(param+1, i):
            return True
        if self.check_help(param-1, i):
            return True
        if self.check_help(param, i+1):
            return True
        if self.check_help(param, i-1):
            return True
        return False

    def print(self):
        lend_1 = self.lend
        for i in range(len(lend_1)):
            for j in range(len(lend_1[0])):
                print(lend_1[i][j], end=' ')
            print()
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]))
    print(s.latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]))
    print(s.latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))