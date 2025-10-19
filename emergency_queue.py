class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left_child = 2*index + 1
        right_child = 2*index + 2
        if left_child < len(self.data) and self.data[left_child].urgency < self.data[smallest].urgency:
            smallest = left_child
        if right_child < len(self.data) and self.data[right_child].urgency < self.data[smallest].urgency:
            smallest = right_child
        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"[*] {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_patient

if __name__ == "__main__":
    print("***Testing***\n")

    p1 = Patient("Riley", 2)
    print(f"Patient name: {p1.name}")
    print(f"Patient urgency: {p1.urgency}")

    print("\n***Test 2***")
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    print("\n***Test 3***")
    next_up = heap.peek()
    print(f"Next patient: {next_up.name}, Urgency: {next_up.urgency}")

    print("\n***Test 4***")
    heap.insert(Patient("Morgan", 2))
    heap.insert(Patient("Casey", 4))
    heap.print_heap()

    print("\n***Test 5***")
    print("Processing patients in order of urgency:")
    while heap.peek() is not None:
        patient = heap.remove_min()
        print(f"    [*] Treating: {patient.name} (urgency {patient.urgency})")
    heap.print_heap()
