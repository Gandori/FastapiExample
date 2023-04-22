from src.schemas.example_2 import Example2


def example(*, name: str) -> Example2:
    return Example2(name=name)
