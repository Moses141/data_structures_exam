
       # Queue Algorithm:

class StudentQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, student):
        self._queue.append(student)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)


# Example 

student_queue = StudentQueue()


student_queue.enqueue("Nkangi")
student_queue.enqueue("Moses")
student_queue.enqueue("Aaron")
student_queue.enqueue("Jane")
student_queue.enqueue("Joseph")
student_queue.enqueue("Darren")
student_queue.enqueue("Lynet")
student_queue.enqueue("Stacey")


# Checking for served student
served_student = student_queue.dequeue()
print(f"The first student to be served is: {served_student}")

# Checking if queue is empty
is_empty = student_queue.is_empty()
print(f"Is the queue empty? {is_empty}")

# Getting the queue size
queue_size = student_queue.size()
print(f"The current size of the queue is: {queue_size}")












