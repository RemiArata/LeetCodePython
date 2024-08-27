class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    result = ListNode()
    head = result
    remainder = 0

    while l1 or l2:
        if l1 and l2:
            if l1.val + l2.val + remainder > 9:
                val = (l1.val + l2.val + remainder) % 10
                remainder = 1
            else:
                val = (l1.val + l2.val + remainder) % 10
                remainder = 0
        elif l1:
            if l1.val + remainder > 9:
                val = (l1.val + remainder) % 10
                remainder = 1
            else:
                val = (l1.val + remainder) % 10
                remainder = 0
        elif l2:
            if l2.val + remainder > 9:
                val = (l2.val + remainder) % 10
                remainder = 1
            else:
                val = (l2.val + remainder) % 10
                remainder = 0
        
        result.next = ListNode(val=val)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        result = result.next
    if remainder == 1:
        result.next = ListNode(val=1)

    return head.next
    
lst1 = ListNode(2, ListNode(4, ListNode(3)))
lst2 = ListNode(5, ListNode(6, ListNode(4)))

l = add_two_numbers(lst1, lst2)

while l:
    print(l.val)
    l = l.next
print("-------------------------")

lst1 = ListNode(2, ListNode(4, ListNode(3)))
lst2 = ListNode(5, ListNode(6))

l = add_two_numbers(lst1, lst2)

while l:
    print(l.val)
    l = l.next
print("--------------------------")

lst1 = ListNode(2, ListNode(4))
lst2 = ListNode(5, ListNode(6, ListNode(4)))

l = add_two_numbers(lst1, lst2)

while l:
    print(l.val)
    l = l.next

print("--------------------------")

lst1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
lst2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

l = add_two_numbers(lst1, lst2)

while l:
    print(l.val)
    l = l.next