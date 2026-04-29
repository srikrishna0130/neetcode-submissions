class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle (Slow/Fast)
        slow, fast = head, head.next # fast starts at head.next to handle even/odd cleanly
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        slow.next = None # CRITICAL: Disconnect the two halves
        
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # 'prev' is now the head of the reversed second half

        # 3. Merge the two halves (Zig-Zag)
        first = head
        second = prev # This was 'prev' from the reverse step
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2