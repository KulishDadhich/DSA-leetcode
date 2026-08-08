class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        n = x
        num = x
        result = 0

        while num > 0:
            ld = num % 10
            result = (result * 10) + ld
            num = num // 10

        return n == result

