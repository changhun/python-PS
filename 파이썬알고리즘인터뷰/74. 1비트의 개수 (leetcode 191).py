""" sol1 : bit operator """
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
"""
""" sol2 : n & n - 1 => '1'로 설정된 LSB 를 0으로 변경한다. """
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count