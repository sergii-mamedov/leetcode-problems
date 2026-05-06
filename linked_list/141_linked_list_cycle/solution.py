"""
141. Linked list cycle
https://leetcode.com/problems/linked-list-cycle/description/
https://neetcode.io/problems/linked-list-cycle-detection/question

two pointers: slow and fast
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False