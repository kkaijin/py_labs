class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
       self.head = None
       self.tail = None
       self._size = 0

    def append(self,  value):
        new_n = Node(value)
        if self.head == None:
            self.head = new_n
            self.tail = new_n
        else:
            self.tail.next = new_n
            self.tail = new_n
        self._size += 1
    def prepend(self, value):
        new_n = Node(value)
        new_n.next = self.head
        self.head = new_n
        self._size += 1
    def insert(self, idx: int, value):
        if idx < 0 or idx > self._size:
            raise IndexError
        new_n = Node(value)
        if idx == 0:
            new_n.next = self.head
            self.head = new_n
            self._size += 1
            return
        if idx == self._size:
            self.tail.next = new_n
            self._size += 1
            return
        c = 0
        prev = None
        curr = self.head
        while curr != None:
            if c == idx:
                prev.next = new_n
                new_n.next = curr
                
                break
            prev = curr
            curr = curr.next
            c += 1

        
        self._size += 1
        
    def remove_at(self, idx: int):
        if idx < 0 or idx > self._size:
            raise IndexError
        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            return
        curr = self.head
        c = 0
        prev = None
        while c < idx:
            prev = curr
            curr = curr.next
            c += 1
            if curr.next == None:
                self.tail = prev
                self._size -= 1
                return

        prev.next = curr.next
        self._size -= 1
    def __iter__(self):
        curr = self.head
        while curr != None:
            yield curr.value
            curr = curr.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"SinglyLinkedList({list(self)})"

#test SinglyLinkedList
ll = SinglyLinkedList()
print(f"1. Пустой список: {ll}")
ll.append(7)
ll.append(8)
ll.append(10)
ll.append(20)
ll.append(30)
print(f"2. Добавление в конец (10, 20, 30): {ll}")
ll.prepend(5)
print(f"3. Добавление в начало (5): {ll}")
ll.insert(2, 15)
print(f"4. Вставка 15 по индексу 2: {ll}")
ll.insert(0, 1)
print(f"5. Вставка 1 по индексу 0: {ll}")
ll.insert(8, 100)
print(f"6. Вставка 100 в конец: {ll}")
ll.remove_at(2)
print(f"7. Удаление 15 (середина): {ll}")
ll.remove_at(1)
print(f"8. Удаление 1 (голова): {ll}")
ll.remove_at(5)
print(f"9. Удаление 100 (хвост): {ll}")
print(f"10. Размер: {len(ll)}")
print(f"11. Пуст ли список? {len(ll) == 0}")