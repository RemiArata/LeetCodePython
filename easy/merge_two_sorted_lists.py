class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def add(self, val):
        n = ListNode(n)
        self.next = n
        

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    root = ListNode()
    head = root

    while l1 or l2:
        if l1:
            if l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    return root.next
    




lst1 = ListNode(1, next=ListNode(2, next=ListNode(4, ListNode(5))))
lst2 = ListNode(2, next=ListNode(3, next=ListNode(4, ListNode(7))))

val = mergeTwoLists(lst1, lst2)

while val:
    print(val.val)
    val = val.next