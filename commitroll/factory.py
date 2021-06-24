import executor
import wrapperobject

class Factory:
    def __init__(self, commitroll=None):
        self.executor = executor.Executor(commitroll)

    def create(self, obj_type, *args, **kwargs):
        return wrapperobject.WrapperObject(self.executor, obj_type, *args, **kwargs)
