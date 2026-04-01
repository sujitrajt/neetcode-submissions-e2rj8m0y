class Solution:
    def isPalindrome(self, s: str) -> bool:
   
        s = s.lower()
        s = "".join(filter(str.isalnum,s))
        left = 0
        right = len(s) - 1
        print(s)
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True       