**more Undestanding Linked List**
```python
class Solution:
def print(self, li):
current = li
while current:
print(current.value)
current = current.next
​
def add_two_numbers(self, list1, list2):
num1 = list1.cvt_2int()
num2 = list2.cvt_2int()
result = num1 + num2
li = LinkedList()
for s in str(result):
li.append(s)
return li
​
def num2list(self, num):
if num == 0:
return Node(0)
​
dummy = Node()
current = dummy
​
while num > 0:
digit = num % 10