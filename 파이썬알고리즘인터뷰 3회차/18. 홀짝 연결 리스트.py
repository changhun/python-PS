

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ODD = 0
EVEN = 1
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head = odd_tail = head
        even_head = even_tail = head.next
        cur = head.next.next
        even_odd = ODD
        while cur:
            if even_odd == ODD:
                odd_tail.next, odd_tail = cur, cur
                even_odd = EVEN
            else:
                even_tail.next, even_tail = cur, cur
                even_odd = ODD
            cur = cur.next
        odd_tail.next = even_head
        even_tail.next = None
        return odd_head


def l2ListNode(l):
    head = cur = ListNode(l[0])
    for val in l[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

l = [1,2,3,4,5]
head = l2ListNode(l)
ans = Solution().oddEvenList(head)
while ans:
    print(ans.val)
    ans = ans.next