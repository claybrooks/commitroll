import commitroll as cr

class Executor:
    def __init__(self, commitroll=None):
        if commitroll is None:
            commitroll = cr.CommitRoll()

        self.commitroll = commitroll

    def commit(self, obj_ref, state):
        self.commitroll.commit((obj_ref, state))

    def roll_backward(self):
        if not self.commitroll.can_roll_backward:
            return False

        self.commitroll.roll_backward()
        self.__execute()
        return True

    def roll_forward(self):
        if not self.commitroll.can_roll_forward:
            return False

        self.commitroll.roll_forward()
        self.__execute()
        return True

    def __execute(self):
        next = self.commitroll.current

        if next is None:
            return

        obj_ref, state = next
        obj_ref.execute(state)
