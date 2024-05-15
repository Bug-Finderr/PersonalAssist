from src.methods.speak import speak

import logging


def test() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
    logging.info("Testing speak()...")
    speak('Hello Brother!')
