from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = max_num
        list_counter = 0
        for num in nums:
            if num > 0:
                list_counter += num
            if num <= min_num and num > 0:
                min_num = num
        counter = int(sum(int(i) for i in range(min_num, max_num + 1)))
        missing_argument = counter - list_counter
        if not missing_argument and (len(list(range(min_num, max_num + 1))) < len(nums)):
            missing_argument = max_num + 1
        if min_num > 1:
            missing_argument = 1
        return missing_argument


if __name__ == '__main__':
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))