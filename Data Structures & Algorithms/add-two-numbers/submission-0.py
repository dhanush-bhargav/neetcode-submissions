# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = l2

        while curr and l1:
            s = curr.val + l1.val + carry
            carry = s // 10
            curr.val = s % 10
            curr = curr.next
            l1 = l1.next

        while curr:
            s = curr.val + carry
            carry = s // 10
            curr.val = s % 10
            curr = curr.next

        curr2 = l1
        while curr2:
            s = curr2.val + carry
            carry = s // 10
            curr2.val = s % 10
            curr2 = curr2.next

        curr = l2
        while curr:
            if curr.next is None:
                curr.next = l1
                break
            curr = curr.next

        if carry > 0:
            newNode = ListNode(carry)
            curr = l2
            while curr:
                if curr.next is None:
                    curr.next = newNode
                    break
                curr = curr.next


        return l2


