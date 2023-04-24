from src.schemas.example_1 import Example1


class Example1Grud:
    @staticmethod
    def example(*, name: str) -> Example1:
        return Example1(name=name)
