class Solution:
    def addStrings(self, nums1: str, nums2: str) -> str:
        carry = 0
        l = list()
        i = len(nums1)-1
        j = len(nums2)-1
        while i >=0 or j >=0:
            sum = carry
            if i >= 0:
                sum += int(nums1[i])
            if j >= 0:
                sum += int(nums2[j])

            if sum >9:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            l.append(str(sum))
            i -=1
            j -=1
        if carry == 1:
            l.append(str(carry))
        l.reverse()
        output = "".join(l)
        return output

############# Test Case #############
nums1 = "11"
nums2 = "123"
s = Solution()
assert "134" == s.addStrings(nums1, nums2)

nums1 = "0"
nums2 = "0"
assert "0" == s.addStrings(nums1, nums2)  

nums1 = "4"
nums2 = "69"
assert "73" == s.addStrings(nums1, nums2) 