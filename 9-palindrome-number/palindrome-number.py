class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        dup = x

        while x > 0:
            lastDigit = x % 10
            revNum = (revNum * 10) + lastDigit
            x //= 10

        return dup == revNum


