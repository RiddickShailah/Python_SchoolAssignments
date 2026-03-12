
#Shailah_Riddick_HW1_Task4
# Node Class: Represents a process in the system
class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid              # ID
        self.burst_time = burst_time  # Remaining Time
        self.next = None            # Pointer to next process


# Circular Linked List Class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Add a new process to the circular list
    def append(self, pid, burst_time):
        new_node = Node(pid, burst_time)
        if not self.head:  # Empty list
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    # Remove a process from the list
    def remove(self, node):
        if not self.head:
            return

        if self.head == node and self.head.next == self.head:
            self.head = None
            return

        if self.head == node:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        while current != self.head:
            if current == node:
                prev.next = current.next
                return
            prev = current
            current = current.next

    # Display all processes
    def display(self):
        if not self.head:
            print("No processes remaining.")
            return
        current = self.head
        while True:
            print(f"Process {current.pid}: Remaining Burst Time = {current.burst_time}")
            current = current.next
            if current == self.head:
                break

    # Check if list empty
    def is_empty(self):
        return self.head is None


# Round Robin Scheduler
def round_robin_scheduler(processes, quantum):
    cll = CircularLinkedList()
    
    # Add all processes to circular linked list
    for pid, burst in processes:
        cll.append(pid, burst)

    print("Processes in the list:")
    cll.display()
    print()

    total_time = 0
    current = cll.head

    # Continue until all processes finish
    while not cll.is_empty():
        next_process = current.next  

        # Run process
        if current.burst_time > quantum:
            print(f"Running Process {current.pid} for {quantum} units.")
            current.burst_time -= quantum
            total_time += quantum
        else:
            print(f"Running Process {current.pid} for {current.burst_time} units (Finished).")
            total_time += current.burst_time
            current.burst_time = 0
            cll.remove(current)

        # Display remaining processes 
        print("Remaining Processes:")
        cll.display()
        print()

        # Move to next process
        current = next_process if not cll.is_empty() else None

    print(f"Total time taken: {total_time} units")


#driver
if __name__ == "__main__":
    # Example Input
    processes = [(1, 10), (2, 5), (3, 8)]  # (Process ID, Burst Time)
    quantum_time = 4

    # Run Round Robin Scheduler
    round_robin_scheduler(processes, quantum_time)