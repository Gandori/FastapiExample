def pytest_sessionstart() -> None:
    print('TEST START')


def pytest_sessionfinish() -> None:
    print('TEST END')
