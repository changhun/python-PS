# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_tail = odd_dummy_head = ListNode()
        even_tail = even_dummy_head = ListNode()

        while head and head.next:
            odd_tail.next = head
            even_tail.next = head.next
            odd_tail, even_tail = odd_tail.next, even_tail.next
            head = head.next.next

        if head:
            odd_tail.next = head
            odd_tail = odd_tail.next
        even_tail.next = None
        odd_tail.next = even_dummy_head.next
        return odd_dummy_head.next
