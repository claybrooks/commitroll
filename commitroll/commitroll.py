import stack

class CommitRoll:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.backward_stack = stack.Stack(self.max_size)
        self.forward_stack = stack.Stack(self.max_size)

    @property
    def can_roll_backward(self):
        return not self.backward_stack.empty

    @property
    def can_roll_forward(self):
        return not self.forward_stack.empty

    @property
    def empty(self):
        return not self.can_roll_forward and not self.can_roll_backward

    @property
    def current(self):
        return self.backward_stack.peek()

    def clear(self):
        self.backward_stack.clear()
        self.forward_stack.clear()
        return True

    def commit(self, state):
        self.backward_stack.push(state)
        self.forward_stack.clear()
        return True

    def roll_backward(self):
        self.forward_stack.push(self.backward_stack.pop())
        return True

    def roll_forward(self):
        self.backward_stack.push(self.forward_stack.pop())
        return True
