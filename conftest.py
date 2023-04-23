import os
import time


def pytest_sessionstart() -> None:
    os.system('docker-compose up --detach --build')
    time.sleep(5)


def pytest_sessionfinish() -> None:
    time.sleep(5)
    os.system('docker-compose down')
