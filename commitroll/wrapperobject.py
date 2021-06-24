import commitable
import copy
from functools import wraps

class WrapperObject:
    def __init__(self, executor, obj_type, *args, **kwargs):
        self.executor = executor
        self.obj = obj_type(*args, **kwargs)
        self.previous_state = None

    def __getattr__(self, name):

        try:
            func = getattr(self.obj, name)
        except Exception as e:
            raise(e)

        if not self.__is_commitable(func):
            return func

        @wraps(name)
        def _wrapped(*args, **kwargs):
            # previous state is None, this is the first pass through
            if self.previous_state is None:
                self.previous_state = copy.deepcopy(self.obj.__dict__)
                self.executor.commit(self, self.previous_state)

            # execute the function
            ret = func(*args, **kwargs)

            # get the new state
            state = copy.deepcopy(self.obj.__dict__)

            state_diff = {k[0]: k[1] for k in set(state.items()) - set(self.previous_state.items())}

            # commit only the difference
            self.executor.commit(self, state_diff)

            # store the previous state
            self.previous_state = copy.deepcopy(state_diff)

            return ret

        return _wrapped

    def __is_commit_all(self):
        return hasattr(self.obj, commitable.COMMIT_ALL)

    def __is_commitable_function(self, func):
        return hasattr(func, commitable.COMMIT)

    def __is_not_commitable_function(self, func):
        return hasattr(func, commitable.NO_COMMIT)

    def __is_commitable(self, func):
        if self.__is_commit_all():
            return not self.__is_not_commitable_function(func)
        else:
            return self.__is_commitable_function(func)

    def execute(self, state):
        self.obj.__dict__.update(state)
        i = 0
