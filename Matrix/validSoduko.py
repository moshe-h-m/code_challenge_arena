import math
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dict_of_nums = {str(i) : [] for i in range(1,10)}
        print(dict_of_nums)
        def checkValidPlace(pairList, i, j):
                    if pairList[0] == i or pairList[1] == j or (math.ceil(pairList[1]/3) == math.ceil(j/3) and math.ceil(pairList[0]/3) == math.ceil(i/3)):
                        return False
                    return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    dict_of_nums[board[i][j]].append([i, j])
                    if len(dict_of_nums[board[i][j]]) > 1:
                        for pairlist in dict_of_nums[board[i][j]]:
                            if not checkValidPlace(pairlist, i, j):
                                return False

        return True

if __name__ == '__main__':
    print(Solution().isValidSudoku([[".",".",".",".","5",".",".","1","."],
                                    [".","4",".","3",".",".",".",".","."],
                                    [".",".",".",".",".","3",".",".","1"],
                                    ["8",".",".",".",".",".",".","2","."],
                                    [".",".","2",".","7",".",".",".","."],
                                    [".","1","5",".",".",".",".",".","."],
                                    [".",".",".",".",".","2",".",".","."],
                                    [".","2",".","9",".",".",".",".","."],
                                    [".",".","4",".",".",".",".",".","."]]))

    print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] ))
