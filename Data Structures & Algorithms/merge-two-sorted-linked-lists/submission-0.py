# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        merged_list_head = None
        while list1 or list2:
            list1_val = list1.val if list1 else 101
            list2_val = list2.val if list2 else 101

            if not merged_list:
                val = min(list1_val, list2_val)
                merged_list = ListNode(val)
                merged_list_head = merged_list    
            else:
                val = min(list1_val, list2_val)
                merged_list.next = ListNode(val)
                merged_list = merged_list.next
            
            if list1_val < list2_val:
                list1 = list1.next
            else:
                list2 = list2.next
            
        
        return merged_list_head