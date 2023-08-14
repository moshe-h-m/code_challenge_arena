

def no_of_islend(matrix):

    if not matrix:
        return 0

    island_counter = 0
    reviewed_island = {}

    for i in range(matrix):
        for j in range(matrix[0]):
            place = (str(i) + str(j))
            if matrix[i][j] == '1':
                reviewed_island(place) == True;
                if(not is_visited(matrix, reviewed_island, i, j)):
                    island_counter += 1

    return island_counter


def is_visited(matrix, dict, i, j):
    if i <=0 or j <= 0 or i >= len(matrix) -1 or j >= len(matrix[0]):
        pass
    if dict(str(i) + str(j + 1)):
        return True
    elif dict(str(i) + str(j -1)):
        return True
    elif dict(str(i + 1) + str(j)):
        return True
    elif dict(str(i - 1) + str(j)):
        return True
    return False