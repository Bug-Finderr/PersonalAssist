from typing import Any

import time
import logging


def run_time(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = time.perf_counter()
        logging.info(f"Function *{func.__name__}* took {end - start} seconds to run.")
        return result

    return wrapper


if __name__ == "__main__":
    from tests.run_time_test import test
    test(2)
