import logging
def setup_logging():
    logging.basicConfig(
        filename="atm.log",
        level=logging.INFO,
        format="%(asctime)s-%(levelname)s - %(message)s",
        encoding="utf-8"
    )