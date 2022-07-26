class Solution:
    def searchRange(self, nums, target: int): 
        def startend(nums,flag):
            l = 0
            r = len(nums) -1
            x = -1
            while l <= r:
                m = (l + r)//2
                if nums[m] == target:
                    x = m
                    
                if flag == 0:
                    if target <= nums[m]:
                        r = m -1
                        
                    elif target > nums[m]:
                        l = m +1
                else: 
                    if target >= nums[m]:
                        l = m +1
                        
                    elif target < nums[m]:
                        r = m -1
          
            return x

        left = startend(nums,0)
        right = startend(nums,1)
        return [left,right]

s = Solution()
assert [-1, -1] == s.searchRange([5,7,7,8,8,10], 6)
assert [3, 4] == s.searchRange([5,7,7,8,8,10], 8)
assert [-1, -1] == s.searchRange([], 0)
assert [0,0] == s.searchRange([1, 3, 4], 1)
assert [0, 2] == s.searchRange([1, 1, 1], 1)