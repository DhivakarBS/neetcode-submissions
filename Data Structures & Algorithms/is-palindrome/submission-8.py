class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch for ch in s if ch.isalnum())
        s=s.lower()
        print(s)
        if (s==s[::-1]) or (s==""):
            return True
        # elif (s==""):
        #     return True
        else:
            return False