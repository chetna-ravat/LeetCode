class Solution:
    def hammingWeight(self, n: int) -> int:
         # binary to integer conversion
        k  = 0
        count = 0
        for i in range (0, 32):
            x = n & (1 << k)
            # print(x,z)
            if x > 0:
                count += 1
            k +=1
        return count 

s = Solution()
assert 3 == s.hammingWeight(11)
assert 1 == s.hammingWeight(32)
assert 31 == s.hammingWeight(4294967293)