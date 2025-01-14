import logging

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("kaevor_ai.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("KaevorAI")
