class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1={}
        complement=0
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in d1:
                return [d1[complement],i]
            d1[nums[i]]=i
        