class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s)==len(t):
            for i in range(len(s)):
                d1[s[i]]=d1.get(s[i],0)+1
                d2[t[i]]=d2.get(t[i],0)+1
            print(d1,d2)
            if d1 == d2:
                return True
            else:
                return False
        else:
            return False


        