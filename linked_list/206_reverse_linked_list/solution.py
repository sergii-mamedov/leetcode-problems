"""
206. Reverse linked list
https://leetcode.com/problems/reverse-linked-list/description/
https://neetcode.io/problems/reverse-a-linked-list/question
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        return prev