# Binary Search Template

## Template 1
```shell
l = 0
r = n 
while l <= r:
	m = l + (r-l)//2
	if nums[m] == target:
		return m
	elif nums[m] > target:  # Target is on the left
		r = m -1
	elif nums[m] < target:  # Target is on the right
        l = m + 1

return -1
```

## Template 2
