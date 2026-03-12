#Shailah_Riddick_HW1_Task2
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#Inserts new node
def insert(head, insertVal):
    new_node = Node(insertVal)

    if not head:
        new_node.next = new_node
        return new_node

    current = head
#If list is empty
    while True:
        if current.val <= insertVal <= current.next.val:
            break

        if current.val > current.next.val:
            if insertVal >= current.val or insertVal <= current.next.val:
                break

        current = current.next

        if current == head:
            break
#insert new node
    new_node.next = current.next
    current.next = new_node

    return head


def build_circular_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next
#Makes circular
    current.next = head
    return head


def print_circular_list(head):
    if not head:
        print("List is empty")
        return

    current = head
    while True:
        print(current.val, end=" -> ")
        current = current.next
#Stop when reach top/head
        if current == head:
            break
    print("(back to head)")


if __name__ == "__main__":
    values = [3, 4, 1]
    insertVal = 2

    head = build_circular_list(values)

    print("Original list:")
    print_circular_list(head)

    head = insert(head, insertVal)

    print("After insertion:")
    print_circular_list(head)