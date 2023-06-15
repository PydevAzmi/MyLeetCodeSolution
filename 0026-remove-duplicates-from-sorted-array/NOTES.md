```
list1 = list(dict.fromkeys(nums))
k = len(list1)
nums = list1 + nums[k:]
return k
```