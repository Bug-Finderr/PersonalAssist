from src.decorators.run_time import run_time
import time
import logging


@run_time
def test(sec: int) -> None:
    logging.basicConfig(level=logging.DEBUG,
                        format="\n%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        datefmt="%d-%b-%y %H:%M:%S")
    logging.debug("Testing run_time decorator...")

    time.sleep(sec)
