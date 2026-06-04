class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        count=1
        max_val=1
        num=sorted(set(nums))
        print(num)
        left=0
        if len(num)==0:
            return 0
        for right in range(1,len(num)):
            if(num[right] - num[right-1])==1:
                count+=1
            else:
                count=1
            max_val=max(max_val,count)
        return max_val
            
            