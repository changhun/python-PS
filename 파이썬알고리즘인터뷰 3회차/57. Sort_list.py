from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        head.next = next = self.sortList(head.next)
        cur = head
        if next and cur.val > next.val:
            head = next

        prev = ListNode(0, cur)
        while next and cur.val > next.val:
            cur.next, next.next, prev.next = next.next, cur, next
            prev = next
            next = cur.next

        return head



def list2ListNode(l):
    if not l:
        return None
    head = ListNode(l[0])
    head.next = list2ListNode(l[1:])
    return head

def print_list(head):
    if not head:
        return
    print(head.val)
    print_list(head.next)


head = [4,2,1,3]
head = list2ListNode(head)
head = Solution().sortList(head)
print_list(head)