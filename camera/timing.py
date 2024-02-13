import time

perf = {}

def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # print(f'Function {func.__name__} took {total_time:.4f} seconds')
        if perf.get(func.__name__) is None:
            perf[func.__name__] = total_time
        perf[func.__name__] += total_time
        perf[func.__name__] /= 2
        return result
    return timeit_wrapper