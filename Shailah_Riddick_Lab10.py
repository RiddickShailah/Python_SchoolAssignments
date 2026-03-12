#Shailah Riddick
# lab_stack_queue_short.py

# ---------- PART 1: Stack ----------
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        # add the item to the top of the stack
        self._data.append(item)

    def pop(self):
        # raise IndexError if stack is empty
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        # remove and return the top item from the stack
        return self._data.pop()

    def is_empty(self):
        # return True if stack is empty, False otherwise
        return len(self._data) == 0


# ---------- PART 2: Queue ----------
class Queue:
    def __init__(self):
        self._data = []
        self._front = 0      # points to the front element

    def enqueue(self, item):
        # add the item to the back of the queue
        self._data.append(item)

    def dequeue(self):
        # raise IndexError if queue is empty
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        # get the front item and move the front pointer
        item = self._data[self._front]
        self._front += 1
        # optional: periodically clean up unused space
        if self._front > len(self._data) // 2:
            self._data = self._data[self._front:]
            self._front = 0
        return item

    def is_empty(self):
        # return True if queue is empty, False otherwise
        return self._front >= len(self._data)


# ---------- PART 3: Practice ----------

def reverse_string(s: str) -> str:
    """Use Stack to reverse a string."""
    st = Stack()
    for ch in s:
        # push each character onto the stack
        st.push(ch)
    out = ""
    while not st.is_empty():
        # pop each character from the stack and add to out
        out += st.pop()
    return out


def printer_queue(jobs: list[str]) -> list[str]:
    """
    Simulate printer queue: jobs are printed in arrival order.
    Return a list of printed jobs in the order they were processed.
    """
    q = Queue()
    for job in jobs:
        q.enqueue(job)

    printed_jobs = []
    while not q.is_empty():
        printed_jobs.append(q.dequeue())
    return printed_jobs


# ------------------ Quick Tests --------------------
def run_tests():
    print("Running quick tests...")
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    jobs = ["Report.pdf", "Invoice.docx", "Graph.png"]
    assert printer_queue(jobs) == jobs
    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()
