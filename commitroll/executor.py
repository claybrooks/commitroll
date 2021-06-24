import commitroll as cr

class Executor:
    def __init__(self, commitroll=None):
        if commitroll is None:
            commitroll = cr.CommitRoll()

        self.commitroll = commitroll

    def commit(self, obj_ref, func, *args, **kwargs):
        self.commitroll.commit((obj_ref, func, args, kwargs))

    def roll_backward(self):
        if not self.commitroll.can_roll_backward:
            return

        self.commitroll.roll_backward()
        self.__execute()

    def roll_forward(self):
        if not self.commitroll.can_roll_forward:
            return

        self.commitroll.roll_forward()
        self.__execute()

    def __execute(self):
        next = self.commitroll.current

        if next is None:
            return

        obj_ref, func, args, kwargs = next
        obj_ref.execute(func, *args, **kwargs)
