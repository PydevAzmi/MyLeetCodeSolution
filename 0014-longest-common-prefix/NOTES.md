* this  solution for each prefix in any location in the word
```python
class Solution(object):
def longestCommonPrefix(self, strs):
"""
:type strs: List[str]
:rtype: str
"""
​
prefix = {}
smallest = min(strs, key=len)
for i in range(len(smallest)+1):
for j in range(len(smallest)+1):
if i < j :
prefix[smallest[i:j]] = 0
​
for i in range(len(smallest) + 1):
for j in range(len(smallest) + 1):
if i < j:
for s in strs:
if smallest[i:j] in s:
prefix[smallest[i:j]] += 1
​
longest_prefix = {key: value for key, value in prefix.items() if value == len(strs)}
if longest_prefix != {}:
longest_common = max(longest_prefix, key=lambda x: (len(x), longest_prefix[x]))
else:
longest_common = ''
return (longest_common)
```
​