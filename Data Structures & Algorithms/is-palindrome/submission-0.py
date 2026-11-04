class Solution:
    def isPalindrome(self, s: str) -> bool:
        # complexity O(n) space O(n)
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        length = len(s)

        for i in range(length//2):
            if s[i] != s[length - i - 1]:
                return False
        return True

