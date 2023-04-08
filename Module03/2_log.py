import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.ERROR,
    handlers=[logging.FileHandler("program.log"), logging.StreamHandler()],
)
logging.info("An example message.")
logging.error("Another message!")
