class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, new_data) -> None:
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def get(self, index: int):
        last_node = self.head
        node_index = 0
        while node_index < index:
            try:
                node_index = node_index + 1
                last_node = last_node.next_node
            except AttributeError:
                break

        if node_index == index:
            return last_node.data

    def remove(self, index: int) -> None:
        head_node = self.head
        node_index = 0

        if head_node is None:
            return

        if index == 0:
            self.head = head_node.next_node
            return

        while head_node is not None:
            if index == node_index:
                break
            last_node = head_node
            head_node = head_node.next_node
            node_index += 1

        if head_node is None:
            return

        last_node.next_node = head_node.next_node

    def list(self) -> list:
        data_list = []
        head_node = self.head
        while head_node is not None:
            data_list.append(head_node.data)
            head_node = head_node.next_node
        return data_list


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list.list())
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list.list())

# зачтено
