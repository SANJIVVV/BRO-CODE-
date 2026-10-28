class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch

        return new == new[::-1]
