import os
import random
import string
import time

import pytest


def pytest_sessionstart() -> None:
    os.system('bash start_docker_compose.sh')
    time.sleep(10)


def pytest_sessionfinish() -> None:
    time.sleep(5)
    os.system('docker-compose down')


def pytest_collection_modifyitems(items):
    numrepeats = 10
    items.extend(items * (numrepeats - 1))


def create_random_string(length: int = 5) -> str:
    random_string: str = ""
    for _ in range(length):
        random_int: int = random.randint(0, (len(string.ascii_letters) - 1))
        random_string += string.ascii_letters[random_int]
    return random_string


@pytest.fixture()
def random_id() -> int:
    return random.randint(0, 1000)


@pytest.fixture()
def item_payload() -> dict:
    return {'name': create_random_string(), 'description': create_random_string()}


@pytest.fixture()
def user_payload() -> dict:
    return {'name': create_random_string()}
