class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        n=len(nums)
        ans=[1]*n
        for i in range(n):
            ans[i]=prefix
            prefix*=nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]

        return ans        