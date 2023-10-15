class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.maxRob(nums[1:]),self.maxRob(nums[:-1]))


    def maxRob(self,nums):
        r1=r2=0
        for num in nums:
            temp=max(num+r1,r2)
            r1=r2
            r2=temp
        return r2
        
