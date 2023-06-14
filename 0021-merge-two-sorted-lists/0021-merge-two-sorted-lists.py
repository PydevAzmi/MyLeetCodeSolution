# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def append(self, li, new_node):
        current = li
        if current:
            while current.next:
                current = current.next
            current.next = new_node
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        result = ListNode()
        if list1 or list2:
            current1 = list1
            current2 = list2
            while current1 and current2:
                if current1.val <= current2.val:
                    next0 = current1.next
                    current1.next = None
                    self.append(result, current1)
                    current1 = next0
                else:
                    next0 = current2.next
                    current2.next = None
                    self.append(result, current2)
                    current2 = next0
            if current1:
                self.append(result, current1)
                return result.next
            elif current2:
                self.append(result, current2)
                return result.next
            else:
                return result.next
        else:
            return result.next
