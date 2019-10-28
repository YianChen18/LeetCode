"""
    Given a linked list, determine if it has a cycle in it.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        thisset = set()     # 可以用set或者dict
        while head:
            if head not in thisset:
                thisset.add(head)
                head = head.next
            else:
                return True
        return False