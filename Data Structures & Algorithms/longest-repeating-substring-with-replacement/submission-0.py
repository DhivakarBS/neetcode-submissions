class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        left,count,max_freq=0,0,0
        for right in range (len(s)):
            d[s[right]]=d.get(s[right],0)+1
            max_freq=max(max_freq,d[s[right]])
            while(right - left + 1) - max_freq>k:
                d[s[left]]-=1
                left+=1
            count=max(count,right-left+1)
        return count