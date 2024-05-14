import time
from typing import Any


def run_time(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"Function * {func.__name__} * took {end - start} seconds to run.")
        return result

    return wrapper


if __name__ == "__main__":
    @run_time
    def sleep_n_seconds(n: int) -> None:    # test function
        time.sleep(n)

    sleep_n_seconds(5)
