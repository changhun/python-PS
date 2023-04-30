from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_sort(head, length):
            if length == 1:
                head.next = None
                return head
            elif length == 0:
                return None

            first_size = length // 2
            second_size = length - first_size

            second_head = head

            for _ in range(first_size):
                second_head = second_head.next

            head = merge_sort(head, first_size)
            second_head = merge_sort(second_head, second_size)

            cur = dummy = ListNode()

            while first_size > 0 and second_size > 0:
                if head.val <= second_head.val:
                    cur.next = head
                    head = head.next
                    first_size -= 1
                else:
                    cur.next = second_head
                    second_head = second_head.next
                    second_size -= 1
                cur = cur.next

            if first_size > 0:
                cur.next = head
            else:
                cur.next = second_head

            merged_head = dummy.next
            del dummy
            return merged_head

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        ret = merge_sort(head, length)
        return ret

#head = [4,2,1,3]
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
ret = Solution().sortList(head)
print(ret)
while ret:
    print(ret.val)
    ret = ret.next
