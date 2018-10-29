#参考资料 https://blog.csdn.net/linfeng886/article/details/79772348
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if nums[x] + nums[y] == target:
                    return [x, y]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
