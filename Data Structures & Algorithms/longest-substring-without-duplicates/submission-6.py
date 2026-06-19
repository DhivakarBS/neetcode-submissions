class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        left,max_length=0,0
        if len(s)==0:
            return 0
        for right in range(0,len(s)):
            d[s[right]]=d.get(s[right],0)+1
            while((d.get(s[right]))>1):
                d[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length