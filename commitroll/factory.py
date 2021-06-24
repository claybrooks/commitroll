import executor
import wrapperobject

class Factory:
    def __init__(self, undoredo=None):
        self.executor = executor.Executor(undoredo)

    def create(self, obj_type, *args, **kwargs):
        return wrapperobject.WrapperObject(self.executor, obj_type, *args, **kwargs)
