class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in range (len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        x=dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        a=list(x)
        for i in range(0,k):
            res.append(a[i])
        return res