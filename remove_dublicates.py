class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        temp = head
        while (temp and temp.next):
            if (temp.next.data == temp.data):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

def display_linked_list(temp):
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

linked_list = Node(1)
linked_list.next = Node(1)
linked_list.next.next = Node(2)
linked_list.next.next.next = Node(3)
linked_list.next.next.next.next = Node(3)
linked_list.next.next.next.next.next = Node(3)

print("Original Linked List:")
display_linked_list(linked_list)

solution = Solution()
result = solution.deleteDuplicates(linked_list)

print("\nLinked List after deleting duplicates:")
display_linked_list(result)
