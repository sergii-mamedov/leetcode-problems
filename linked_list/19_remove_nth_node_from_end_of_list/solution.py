"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
https://neetcode.io/problems/remove-node-from-end-of-linked-list/question

slow/fast, iterate fast n-times
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next