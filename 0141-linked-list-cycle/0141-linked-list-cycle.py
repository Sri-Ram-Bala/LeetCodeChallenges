# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       freq_map = {}
       if not head:
            return False
       current = head
       freq_map[0] = current 
       check, i = True, 1
       while check:       
            if not current.next:
                return False
            if current.next in freq_map.values():
                return True 
            freq_map[i] = current.next
            current = current.next
            i += 1