```python
class Solution(object):
def mySqrt(self, x):
"""
:type x: int
:rtype: int
"""
for i in range(x//2+2):
if x in range(i*i, (i+1)*(i+1)):
return i
```