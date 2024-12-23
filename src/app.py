from src.decorators import timer_decorator, repeat, count_calls, repeat_function


@repeat_function(num_times=3)
@timer_decorator
def run_for_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])

run_for_some_time(1000)
