"""
143. Reorder list
https://leetcode.com/problems/reorder-list/description/
https://neetcode.io/problems/reorder-linked-list/question

Four steps:
1. find a middle
2. split onto tow list
3. reverse second
4. merge
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # empty or one element list
        if not head.next or not head.next.next:
            return None
        
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split
        second = slow.next
        slow.next = None

        # reverse
        prev, curr = None, second
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        second = prev

        # merge
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2