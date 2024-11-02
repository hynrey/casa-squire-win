import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[CasaSquire Service] %(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
