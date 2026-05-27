class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res=[1]*len(nums)
        # product=1
        # print(res)
        # for i in range (len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         res[i]*=nums[j]
        # return res
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        print(left)
        print(right)

        for i in range (len(nums)):
            nums[i]=left[i]*right[i]
        return nums

