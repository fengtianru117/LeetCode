class Solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if nums[x]+nums[y]==target:
                    return [x,y]

if __name__ == '__main__':
    nums=[2, 7, 11, 15]
    target=9
    s=Solution()
    print(s.twoSum(nums,target))
