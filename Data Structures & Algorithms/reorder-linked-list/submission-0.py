# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        halfway = (length + 1) // 2
        reverse = head
        prev = None
        count = 0
        while count<halfway:
            count+=1
            prev = reverse
            reverse = reverse.next
        prev.next = None
        prev, curr = None, reverse
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        forward_pt, reverse_pt = head, prev
        take_from_reverse = True
        while reverse_pt:
            print(forward_pt.val or -1)
            print(reverse_pt.val or -1)
            if take_from_reverse:
                temp1 = forward_pt.next
                temp2 = reverse_pt.next
                forward_pt.next = reverse_pt
                reverse_pt.next = temp1
                forward_pt = reverse_pt
                reverse_pt = temp2
                take_from_reverse = False
            else:
                forward_pt = forward_pt.next
                take_from_reverse = True
