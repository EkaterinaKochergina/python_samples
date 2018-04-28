class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()
        n = len(nums)
        for i in range (1, n+1):
            sum += min(nums[i], nums[i+1])
        return sum

tst = Solution()
print(tst.arrayPairSum([1, 4, 3, 2]))