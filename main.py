#черга через зв'язаний список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        result = []
        temp = self.front
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return "->".join(result)

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count

# Приклад використання черги на основі зв'язаного списку:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)

print("Dequeue:", q.dequeue())  # Видалення елемента з черги
print("Size of the queue:", q.size())  # Розмір черги