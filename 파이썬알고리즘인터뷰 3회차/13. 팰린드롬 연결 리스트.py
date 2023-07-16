from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def checkPalindrome(head: ListNode, size: int) -> (bool, ListNode):
            l = []
            half_size = size // 2
            is_even = True
            if size % 2 == 1:
                is_even = False

            cur = head
            for i in range(half_size):
                l.append(cur.val)
                cur = cur.next
            if not is_even:
                cur = cur.next
            while cur:
                if l[-1] != cur.val:
                    return False
                l.pop()
                cur = cur.next
            return True

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return checkPalindrome(head, length)


def make_list(l):
    head = ListNode()
    cur = head
    for val in l:
        cur.next = ListNode(val)
        cur = cur.next
    return head.next

l = [1, 2, 2, 1]
head = make_list(l)
cur = head
while cur:
    print(cur.val)
    cur = cur.next

ret = Solution().isPalindrome(head)
print(ret)