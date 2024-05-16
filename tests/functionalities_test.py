import logging
from src.methods import functionalities as f


def test() -> None:

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        datefmt="%d-%b-%y %H:%M:%S")
    logging.info("Testing functionalities...")

    logging.info("Testing greet()...")          # Test result: Works fine
    f.greet()

    logging.info("Testing date()...")           # Test result: Works fine
    f.date()

    logging.info("Testing time()...")           # Test result: Works fine
    f.time()

    logging.info("Testing search_wikipedia()...")   # Test result: Works fine
    f.search_wikipedia("Python programming")

    logging.info("Testing search_online()...")      # Test result: Works fine
    f.search_online()

    logging.info("Testing take_screenshot()...")    # Test result: Works fine
    f.take_screenshot()

    logging.info("Testing system_usage()...")       # Test result: Works fine
    f.system_usage()

    logging.info("Testing joke()...")           # Test result: Works fine
    f.joke()

    logging.info("Testing weather()...")        # Test result: Works fine
    f.weather()
