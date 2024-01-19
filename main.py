import psutil
import time


def package(accumulator, seconds, percentage):
    if percentage:
        return (accumulator / seconds) * 100
    else:
        return accumulator / seconds


def get():
    while True:

        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        print(f'CPU: {cpu} %')
        print(f'RAM: {ram} %')

        time.sleep(1)


get()
