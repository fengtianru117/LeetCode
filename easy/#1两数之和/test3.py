class Solution:
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target:int
        :rtype List[int]
        """

        n = len(nums)
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 当字典中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]], x
            else:
                # 否则往字典增加键/值对
                d[a] = x
                # 边往字典增加键/值对，边查找nums[x+1]是否在字典d里头


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
