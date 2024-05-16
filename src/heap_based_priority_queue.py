class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class BinaryHeap:
    def __init__(self):
        self.priority_queue = []

    def swap_two_elements(self, i, j):
        self.priority_queue[i], self.priority_queue[j] = self.priority_queue[j], self.priority_queue[i]

    def add_element(self, value, priority):
        new_node = Node(value, priority)
        self.priority_queue.append(new_node)
        self._heapify_up(len(self.priority_queue) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.priority_queue[index].priority > self.priority_queue[parent_index].priority:
            self.swap_two_elements(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def pop_element(self):
        if not self.priority_queue:
            return None
        top_element = self.priority_queue[0]
        self.priority_queue[0] = self.priority_queue[-1]
        self.priority_queue.pop()
        self._heapify_down(0)
        return top_element

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        max_index = index
        if left_child_index < len(self.priority_queue) and self.priority_queue[left_child_index].priority > self.priority_queue[max_index].priority:
            max_index = left_child_index
        if right_child_index < len(self.priority_queue) and self.priority_queue[right_child_index].priority > self.priority_queue[max_index].priority:
            max_index = right_child_index
        if max_index != index:
            self.swap_two_elements(index, max_index)
            self._heapify_down(max_index)

    def show_queue(self):
        if not self.priority_queue:
            print(None)
        for node in self.priority_queue:
            print(f"Value: {node.value}, Priority: {node.priority}")

