class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        striped = "".join(char for char in lower if char.isalnum())
        reversed = striped[::-1]
        if striped == reversed:
        # if s == reversed:
            return True
        else: return False