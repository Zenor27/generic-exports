import cProfile
import contextlib
import io
import pstats


@contextlib.contextmanager
def profile_context(enable_callers_trace=False):
    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    stream = io.StringIO()
    ps = pstats.Stats(pr, stream=stream).sort_stats("cumulative")
    ps.print_stats()
    if enable_callers_trace:
        ps.print_callers()
    print(stream.getvalue())
