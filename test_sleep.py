import time


def eval(sleep_f, res=10000):
    start = time.time()
    for i in range(res):
        sleep_f(1.0 / res)
    end = time.time()
    diff = end - start
    print(diff)
    return diff


def busy_wait(time_f):
    def f(delay):
        start = time_f()
        while time_f() - start < delay:
            pass
        return
    return f


def busy_wait_ns(time_ns_f):
    def f(delay):
        to = int(delay * 1000000000)
        start = time_ns_f()
        while time_ns_f() - start < to:
            pass
        return
    return f


# eval(time.sleep)
eval(busy_wait(time.time))
eval(busy_wait(time.monotonic))
eval(busy_wait(time.perf_counter))
eval(busy_wait_ns(time.time_ns))
eval(busy_wait_ns(time.monotonic_ns))
eval(busy_wait_ns(time.perf_counter_ns))
