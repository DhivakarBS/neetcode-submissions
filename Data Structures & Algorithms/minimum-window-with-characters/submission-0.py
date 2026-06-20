class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        count={}
        left=0
        have,need=0,0
        reslen=float("inf")
        res=[-1,-1]
        for n in t:
            count[n]=count.get(n,0)+1
        need=len(count)
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1

            if s[right] in count and window[s[right]] == count[s[right]]:
                have+=1
            
            while have == need:
                if(right-left+1)<reslen:
                    reslen=right-left+1
                    res=[left,right]
                window[s[left]]-=1
                if s[left] in count and window[s[left]]<count[s[left]]:
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if reslen != float("inf") else ""
