class Solution:
    def nextGreatestLetter(self, nums, target: str) -> str:
        
        n = len(nums) -1
        l = 0
        r = n
        ans = -1
        flag = False
        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                flag = True
                index = m
                    
            elif target < nums[m]:
                ans = m
                r = m -1
            if target >= nums[m]:
                l = m + 1
        
        
        if flag == True:
            return nums[(index +1)% len(nums)]
        
        else:
            if ans == -1:
                return nums[0]
            else:
                return nums[ans % len(nums)]
            
   
        
s = Solution()
assert "c" == s.nextGreatestLetter(["c","f","j"], "a")
assert "f" == s.nextGreatestLetter(["c","f","j"], "c")
assert "f" == s.nextGreatestLetter(["c","f","j"], "d")