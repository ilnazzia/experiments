# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    return list(map(int, list(str(int(''.join(map(str, l1[::-1]))) + int(''.join(map(str, l2[::-1])))))[::-1]))

l1 = [2,4,3]
l2 = [5,6,4]

print(addTwoNumbers(l1, l2))


