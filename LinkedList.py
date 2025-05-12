class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index cannot be negative")
        new_node = Node(data)
        if index == 0:
            self.insert_at_start(data)
            return
        curr = self.head
        count = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if not curr:
            raise IndexError("Index out of bounds")
        new_node.next = curr.next
        curr.next = new_node

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        if not self.head:
            raise IndexError("List is empty")
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        count = 0
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1
        if not curr.next:
            raise IndexError("Index out of bounds")
        curr.next = curr.next.next

    def search(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def display(self):
        curr = self.head
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(values) if values else "List is empty")


# Examples
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.insert_at_index(1, 15)
    ll.display()

    print("Index of 20:", ll.search(20))
    ll.delete_at_index(2)
    ll.display()
