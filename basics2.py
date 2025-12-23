import logging

logging.basicConfig(
    filename="prac.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_and_print(message):
    print(message)
    logging.info(message)

def greet(name):
    log_and_print(f"Hello {name}")

def add(a, b):
    return a + b

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

log_and_print("For loop:")
for i in range(1, 6):
    if i == 3:
        continue
    log_and_print(i)

log_and_print("While loop:")
count = 1
while count <= 5:
    if count == 4:
        break
    log_and_print(count)
    count += 1

greet("Megha")
log_and_print(f"Addition result: {add(10, 20)}")
log_and_print(f"Factorial result: {factorial(5)}")

log_and_print("Program ended")
