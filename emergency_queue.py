class Patient:
    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be an integer from 1 to 10.")
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()   # move last patient to the root
        self.heapify_down(0)
        return root


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print(next_up.name, next_up.urgency)

    served = heap.remove_min()
    print(served.name)
    heap.print_heap()

    print("\n--- Edge cases ---")
    empty = MinHeap()
    print("Peek on empty heap:", empty.peek())
    print("Remove from empty heap:", empty.remove_min())

    # Ties and many patients come out in urgency order
    big = MinHeap()
    for name, urg in [("A", 7), ("B", 2), ("C", 9), ("D", 2), ("E", 1), ("F", 4)]:
        big.insert(Patient(name, urg))
    order = []
    while big.peek() is not None:
        p = big.remove_min()
        order.append(f"{p.name}({p.urgency})")
    print("Served order:", order)

    # Invalid urgency
    try:
        Patient("Sam", 11)
    except ValueError as e:
        print("Invalid patient rejected:", e)