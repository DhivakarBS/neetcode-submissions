class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        count=1
        max_val=1
        # for i in range(len(nums)):
        #     d[nums[i]]=d.get(nums[i],0)+1
        # x=dict(sorted(d.items(),key=lambda x:x[0]))
        # print(len(x))
        num=sorted(set(nums))
        print(num)
        left=0
        if len(num)==0:
            return 0
        for right in range(1,len(num)):
            print(num[left],num[right])
            if(num[right] - num[right-1])==1:
                count+=1
                # left+=1
            else:
                count=1
            max_val=max(max_val,count)
        return max_val
            
            