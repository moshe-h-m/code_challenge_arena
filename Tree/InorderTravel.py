import math
import random
from hashlib import new
from typing import List, Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def num_of_nodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.num_of_nodes(root.left) + self.num_of_nodes(root.right) + 1

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
        values_araay = self.inorderTraversal(root)
        for i in range(len(values_araay) - 1):
            if values_araay[i] > values_araay[i + 1]:
                is_valid = False
        return is_valid

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._values_array = self.inorderTraversal(root)
        self._min_val = self._values_array[0]


    def next(self) -> int:
        return self._values_array.pop()
    def hasNext(self) -> bool:
        return len(self._values_array) > 0
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.right) + [root.val] + self.inorderTraversal(root.left)



if __name__ == '__main__':

    treeNode = TreeNode(1, None, TreeNode(2, TreeNode(1,TreeNode(0),TreeNode(2)), TreeNode(4, None, TreeNode(6))))
    s = Solution()
    print(s.inorderTraversal(treeNode))
    print(s.preorderTraversal(treeNode))
    print(s.postorderTraversal(treeNode))
    print(s.num_of_nodes(treeNode))
    print(s.isValidBST(treeNode))





# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# explain : https://www.youtube.com/watch?v=5dySuyZf9Qg

class Bus:
    def __init__(self, name, plateNumber, routeNumber, passengers):
        self.__name = name
        self.__PlateNumber = plateNumber
        self.__routeNumber = routeNumber
        self.__passengers = passengers

    def get_name(self):
        return self.__name

    def get_plateNumber(self):
        return self.__PlateNumber

    def get_routeNumber(self):
        return self.__routeNumber

    def get_passengers(self):
        return self.__passengers

    def set_name(self, name):
        self.__name = name

    def set_plateNumber(self, plateNumber):
        self.__PlateNumber = plateNumber

    def set_routeNumber(self, routeNumber):
        self.__routeNumber = routeNumber

    def set_passengers(self, passengers):
        self.__passengers = passengers


# Q_4_a
def brothers(num1, num2) -> bool:
    return (num1 // math.pow(10, (len(str(num1)) - 1)), num1 % 10) == (
    num2 // math.pow(10, (len(str(num2)) - 1)), num2 % 10)


# Q_4_b
b = [13, 743432, 59441, 1443, 7540007, 205]
# Q_4_c
"""
yes, cous the function btothers is a function that check if the first and last digit of the number are the same 
so the function what check if all the numbers in the array have the same first and last digit
so its no metter the doriction of this arrays
"""
# Q_4_d
"""
the function what is a function that check if all the numbers in the array have the same first and last digit
"""

print(f'that: {brothers(7, 7007)}')


def what(arr1, arr2) -> bool:
    for i in range(len(arr1)):
        flag = False
        for j in range(len(arr2)):
            if brothers(arr1[i], arr2[j]):
                flag = True
        if not flag:
            return False
    return True


def why(str) -> int:
    c = 0
    print(" %", end='')
    for i in range(len(str)):
        if str[i] < 'A' or str[i] > 'Z':
            print(i, end=' ')
        else:
            c += 1
    print(" %")
    return c

#
# def mystery(strArr) -> bool:
#     for i in range(len(strArr)):
#         if why(strArr[i]) != i:
#             return False
#     return True
#
# def Mystery(arr1, arr2):
#     if len(arr1) < len(arr2):
#         return False
#     if len(arr2) == 0:
#         return True
#     return Mystery(arr1[1:], arr2[1:]) and arr1[0] == arr2[0]
#
# def secret(arr1, arr2):
#     if len(arr1) < len(arr2):
#         return False
#     if len(arr2) == 0:
#         return True
#     return secret(arr1[1:], arr2) or Mystery(arr1, arr2)
#
#
# class node:
#     pass
#
# class tree:
#     pass
#
# if __name__ == "main":
#     pass
#     # busList = []
#     # busList.append(Bus("Alex", "1234", "14", 18))
#     # busList.append(Bus("Benny", "7596", "26A", 17))
#     # busList.append(Bus("Charly", "6051", "26B", 16))
#     # busList.append(Bus("Dany", "4472", "778", 21))
#     # busList.append(busList[3])
#     # m, s = 0, 0
#     # x = busList[1].get_passengers()
#     # busList[1].set_passengers(busList[3].get_passengers() + 5)
#     # busList[3].set_passengers(x)
#     # for i in range(len(busList)):
#     #     print(f'{busList[i].get_name()} {busList[i].get_passengers()}')
#     #     s = s + busList[i].get_passengers()
#     #     if busList[i].get_passengers() > 20 :
#     #         m = m + 1
#     # print(f'average: {(s / len(busList))}')
#     # print(m)
# # Q_10
# words = ( "hello", "world", "python", "is", "better", "than", "java")
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k' ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v' ,'w', 'x', 'y', 'z']
# letter = random.choice(letters)
# # Q_10_a
# def is_contain(words, letter) -> bool:
#     for word in words:
#         if word.find(letter) != -1:
#             return True
#     return False
# # Q_10_b
# def is_contain_all(words, letters) -> bool:
#     for letter in letters:
#         if not is_contain(words, letter):
#             return False
#     return True
#
# # Q_11
# str_colors = "red-green-blue-yellow-black-white"
# Tambur = ( "red", "green", "blue", "yellow", "black", "white")
# # Q_11_a
# def is_tambur_champ(str_colors, Tambur) -> bool:
#     new_colors = str_colors.split('-')
#     for color in new_colors:
#         if color not in Tambur:
#             return False
#     return True
#
# # Q_11_b
# print(sorted(Tambur))
# golden_age = {'356847263': 90, '456987152': 76, '987654396': 103}
# max_age = 0
# for key, value in golden_age.items():
#     if value > max_age:
#         max_age = value
#         id = key
# print(id)
# ages = sorted(golden_age.values())
# print(ages)
# for age in ages:
#     for key, value in golden_age.items():
#         if value == age:
#             print(key)
#             break
#
#
# print("something")
