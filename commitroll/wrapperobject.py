import commitable
from functools import wraps

class WrapperObject:
    def __init__(self, executor, obj_type, *args, **kwargs):
        self.executor = executor
        self.obj = obj_type(*args, **kwargs)

    def __getattr__(self, name):

        try:
            func = getattr(self.obj, name)
        except Exception as e:
            raise(e)

        if not self.__is_commitable(func):
            return func

        @wraps(name)
        def _wrapped(*args, **kwargs):
            self.executor.commit(self, name, *args, **kwargs)
            return func(*args, **kwargs)

        return _wrapped

    def __is_commit_all(self):
        return hasattr(self.obj, commitable.COMMIT_ALL)

    def __is_commitable_function(self, func):
        return hasattr(func, commitable.COMMIT_FUNCTION)

    def __is_commitable(self, func):
        return self.__is_commit_all() or self.__is_commitable_function(func)

    def execute(self, func, *args, **kwargs):
        func = getattr(self.obj, func)
        func(*args, **kwargs)


