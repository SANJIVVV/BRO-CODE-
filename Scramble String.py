
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def solve(a, b):
            # If both strings are equal
            if a == b:
                return True

            # If characters are different in frequency
            if sorted(a) != sorted(b):
                return False

            # If we already solved this problem
            if (a, b) in memo:
                return memo[(a, b)]

            n = len(a)

            # Try every possible splitting position
            for i in range(1, n):

                # Case 1: Do not swap
                if (solve(a[:i], b[:i]) and
                    solve(a[i:], b[i:])):
                    memo[(a, b)] = True
                    return True

                # Case 2: Swap the two parts
                if (solve(a[:i], b[n-i:]) and
                    solve(a[i:], b[:n-i])):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return solve(s1, s2)
