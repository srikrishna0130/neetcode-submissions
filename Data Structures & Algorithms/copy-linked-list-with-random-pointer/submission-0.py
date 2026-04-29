class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Map: Original Node -> Clone Node
        old_to_new = {}
        
        # PASS 1: Create all nodes (don't connect pointers yet)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # PASS 2: Connect the clones
        curr = head
        while curr:
            copy = old_to_new[curr]
            # Use the map to find the clones of the neighbors
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]