import logging

logging.basicConfig(
    filename="simple.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_and_print(message):
    print(message)
    logging.info(message)

log_and_print("Program started")
log_and_print("Learning print and logging")
log_and_print("Program ended")