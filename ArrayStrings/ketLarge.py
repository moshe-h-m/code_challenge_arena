from typing import Optional


class Solution:

    def kthLarge(self, nums:[Optional], k: int) -> int:
        max_i = 0

        for i in range(len(nums)):
            if nums[max_i] < nums[i]:
                max_i = i
        min_i = max_i
        for i in range(len(nums)):
            if nums[min_i] > nums[i]:
                min_i = i
        def assistMaxFind(nums, max):
            max_asist = min_i
            for i in range(len(nums)):
                if nums[max_asist] < nums[i] <= nums[max] and i not in max_arr:
                    max_asist = i
            return max_asist
        max_arr = [max_i]
        for i in range(k - 1):
            max_arr.append(assistMaxFind(nums, max_i))

        return nums[max_arr[-1]]

    def kthLarge2(self, nums:[Optional], k: int) -> int:
        return sorted(nums)[-k]


if __name__ == '__main__':
    print(Solution().kthLarge([3, 2, 1, 5, 6, 4], 2))
    print(Solution().kthLarge([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(Solution().kthLarge([1], 1))

    print("__________________")

    print(Solution().kthLarge2([3, 2, 1, 5, 6, 4], 2))
    print(Solution().kthLarge2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(Solution().kthLarge2([1], 1))


