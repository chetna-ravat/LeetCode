class Solution:
    def intersection(self, nums1, nums2):
        l = list()
        d = dict()
        for i in nums1:
            d[i] = 0
        for i in nums2:
            if i in d:
                d[i] +=1
        for k, v in d.items():
            if v >=1:
                l.append(k)
        return l 
        
        
        
        
        # output = set()
        # S = set(nums1)
        # for i in nums2:
        #     if i in S:
        #         output.add(i)
        # return list(output)    
        

s = Solution()
assert [2] == s.intersection([1,2,2,1], [2,2])
assert ([9,4] == s.intersection([4,9,5], [9,4,9,8,4]) or [4,9] == s.intersection([4,9,5], [9,4,9,8,4]))