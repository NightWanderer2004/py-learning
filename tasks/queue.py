# Реализовать очередь с использованием двух стеков. Вам необходимо создать класс Queue, который будет иметь методы enqueue и dequeue. Метод enqueue добавляет элемент в очередь, а метод dequeue удаляет и возвращает элемент из начала очереди.

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        elif self.stack2:
            return self.stack2.pop()
        else:
            return None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.stack1)
queue.dequeue()
queue.dequeue()
print(queue.stack2)
