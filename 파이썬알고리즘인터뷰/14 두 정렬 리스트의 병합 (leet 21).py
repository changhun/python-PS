# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None and list2 is None:
            return None

        #cur = head = ListNode()
        head = ListNode()
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                #cur.next, cur, list1 = list1, cur.next, list1.next
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                #cur.next, cur, list2 = list2, cur.next, list2.next
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return head.next


list1 = ListNode(4, None)
list1 = ListNode(2, list1)
list1 = ListNode(1, list1)
# while list1:
#     print(list1.val)
#     list1 = list1.next

list2 = ListNode(4, None)
list2 = ListNode(3, list2)
list2 = ListNode(1, list2)
sol = Solution()
ret = sol.mergeTwoLists(list1, list2)
while ret:
    print(ret.val)
    ret = ret.next