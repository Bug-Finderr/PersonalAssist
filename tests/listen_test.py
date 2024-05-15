from src.methods.listen import get_audio
import logging


def test() -> None:
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        datefmt="%d-%b-%y %H:%M:%S")

    logging.debug("Testing get_audio()...")
    get_audio()
