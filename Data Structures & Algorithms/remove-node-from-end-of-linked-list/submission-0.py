# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if n==length:
            return head.next
        
        prev = head
        while prev:
            length -=1
            if length == n:
                prev.next = prev.next.next
            prev = prev.next
        return head