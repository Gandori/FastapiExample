from src.schemas.example_1 import Example1


def example(*, name: str) -> Example1:
    return Example1(name=name)
