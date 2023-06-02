class Solution:
    def hammingWeight(self, n: int) -> int:
        num_binary = bin(n)
        return num_binary.count('1')