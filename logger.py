import time


def logged(func):
    def _logged(*args, **kwargs):
        print(f"Called {func.__name__}")
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"Done {func.__name__} in {end - start} seconds")
        return ret
    return _logged
