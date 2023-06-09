# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        
    def cvt_2int(self,li):
        i = 0
        first = li
        num = 0
        
        while first:
            num += (10 ** i) * first.val
            first = first.next
            i += 1
        return num
    


    def num2list(self, num):
        if num == 0:
            return ListNode(0)
        
        dummy = ListNode()
        current = dummy
        
        while num > 0:
            digit = num % 10
            num = num // 10
            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next

    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.cvt_2int(l1)
        num2 = self.cvt_2int(l2)
        result = num1 + num2
        li = self.num2list(result)
        return li