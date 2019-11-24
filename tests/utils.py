from IPython.core.magics.execution import TimeitResult, Timer


def timeit(expr, globals, repeat=10):
    timer = Timer(expr, globals=globals)
    number = 1
    all_runs = timer.repeat(repeat, number)
    best = min(all_runs) / number
    worst = max(all_runs) / number
    return str(TimeitResult(number, repeat, best, worst, all_runs, None, 3))
