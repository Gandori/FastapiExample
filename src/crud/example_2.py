from src.schemas.example_2 import Example2


class Example2Grud:
    @staticmethod
    def example(*, name: str) -> Example2:
        return Example2(name=name)
