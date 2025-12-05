from collections import deque

class Stack:
    def __init__(self, array: list = []):
        self._data = array

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

class Queue:
    def __init__(self, array: deque = []):
        self._data = array

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self._data == []:
            raise IndexError
        else:
            return self._data.pop()

    def peek(self):
        if self._data == []:
            return None
        return self._data[-1]

    def is_empty(self):
        if self._data == []:
            return True
        else:
            return False

    def __len__(self):
        return len(self._data)
    
if __name__ == '__main__':
    print()
    print('stack')
    print()
    s = Stack([])
    s.push(8)
    s.push(2)
    print(s.pop())
    print(s.peek())
    print(s.__len__())
    print(s.is_empty())
    s.pop()
    print(s.is_empty())

    print()
    print('queue')
    print()
    que = Queue()
    que.enqueue(4)
    que.enqueue(10)
    print(que.dequeue())
    print(que.peek())
    print(que.__len__())
    print(que.is_empty())
    que.dequeue()
    print(que.is_empty())