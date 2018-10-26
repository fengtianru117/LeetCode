class Solution:
    def twoSum(selfs,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for x in range(n):
            a=target-nums[x]
            if a in nums:
                y=nums.index(a)
                if x==y:
                    continue
                else:
                    return [x,y]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target=9
    s=Solution()
    print(s.twoSum(nums,target))