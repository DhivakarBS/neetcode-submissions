class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        product=1
        print(res)
        for i in range (len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                res[i]*=nums[j]
        return res
