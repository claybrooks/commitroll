
class Stack:

    def __init__(self, max_size=None):
        self.max_size = max_size
        self.elements = []

    @property
    def empty(self):
        return len(self.elements) == 0

    def peek(self):
        if self.empty:
            return None

        return self.elements[-1]

    def push(self, state):
        self.elements.append(state)

    def pop(self):
        if self.empty:
            return None

        return self.elements.pop()

    def clear(self):
        self.elements.clear()
