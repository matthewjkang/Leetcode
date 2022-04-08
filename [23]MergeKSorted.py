
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        for i in lists:
            print(i.val)
            while next != None:
                i.val



list1 = ListNode(1,ListNode(4,  ListNode(5,  None)))

list2 = ListNode(1,  ListNode(3,  ListNode(4,  None)))

list3 = ListNode(2,  ListNode(6,  None))

lists = [list1,list2,list3]

print(Solution().mergeKLists(lists))