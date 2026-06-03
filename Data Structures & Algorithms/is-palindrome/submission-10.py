class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=""
        for i in s:
            if i.isalnum():
                check+=i.strip().lower()
        return check==check[::-1]
        # s=''.join(ch for ch in s if ch.isalnum())
        # s=s.lower()
        # print(s)
        # if (s==s[::-1]) or (s==""):
        #     return True
        # else:
        #     return False