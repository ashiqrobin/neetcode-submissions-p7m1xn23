class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(c)-1
        while i < j:
            if c[i] == c[j]:
                i +=1
                j -=1
                continue
            else:
                return False
        return True
        