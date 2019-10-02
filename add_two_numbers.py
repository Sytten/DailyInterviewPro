from typing import Optional


# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# Date: 2019-10-02


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode, c=0) -> Optional[ListNode]:
    # Breaking condition
    if l1 is None or l2 is None:
        if c != 0:
            return ListNode(c)
        return None

    # Calculation
    total = l1.val + l2.val + c
    current_number = total % 10

    # Create node
    node = ListNode(current_number)
    node.next = add_two_numbers(l1.next, l2.next, int(total/10))
    return node


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


if __name__ == "__main__":
    result = add_two_numbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
