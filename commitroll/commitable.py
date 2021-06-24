
COMMIT_FUNCTION="1__commit_function"
COMMIT_ALL="2__commit_all"

def CommitFunction(func):
    setattr(func, COMMIT_FUNCTION, True)
    return func

def CommitAll(obj):
    setattr(obj, COMMIT_ALL, True)
    return obj