class Solution:
    def reverseBits(self, n: int) -> int:
        y = '{:032b}'.format(n)
        
        l = list (y)
        l.reverse()
        z = ("".join(l))
     

        
        sum = 0
        k = 31
        for i in z:
            sum += (2**k) * int(i)
            k -= 1
        return sum 

s = Solution()
assert 964176192 == s.reverseBits(43261596)
assert 4294967293 == s.reverseBits(3221225471)