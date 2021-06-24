from functools import wraps

COMMIT="1__commit"
NO_COMMIT="2__no_commit"
COMMIT_ALL="3__commit_all"
SAVE_STATE="4__save_state"

def Commit(func):
    setattr(func, COMMIT, True)
    return func

def NoCommit(obj):
    setattr(obj, NO_COMMIT, True)
    return obj

def CommitAll(obj):
    setattr(obj, COMMIT_ALL, True)
    return obj

def SaveState(_lambda):
    def wrapper(f):
        @wraps(f)
        def wrapped(inst, *args, **kwargs):
            f(inst, *args, **kwargs)
            setattr(inst, SAVE_STATE, list(_lambda(inst)))
        return wrapped
    return wrapper
