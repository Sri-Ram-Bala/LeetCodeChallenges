# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self, head):
        count = 1
        current = head      
        while current.next:
            count += 1
            current = current.next
        return count
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        current = prev.next
        lenth = self.len(head)
        if lenth <= 1 and n <= 1:
            head = None
            return head
        stop = lenth - n 
        if not stop:
            head = prev.next
            prev.next = None           
        i = 1
        while current:
            if i == stop:
                prev.next = current.next
                current.next = None
                break
            prev = current
            current = current.next
            i += 1
        return head  
        