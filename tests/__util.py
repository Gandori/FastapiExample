import threading
import typing

import dotenv
import httpx
from httpx import Response
from pydantic import BaseSettings


class Request(BaseSettings):
    host: str = 'localhost'
    port: int = 8080
    prefix: str = ''

    def __init__(self) -> None:
        dotenv.load_dotenv()
        super().__init__()

    def get_request(self, route: str) -> Response:
        return httpx.get(url=f'http://{self.host}:{self.port}{self.prefix}{route}')

    def post_request(
        self, data: list[typing.Dict] | typing.Dict, route: str
    ) -> Response:
        return httpx.post(
            url=f'http://{self.host}:{self.port}{self.prefix}{route}', json=data
        )

    def put_request(self, data: typing.Dict, route: str) -> Response:
        return httpx.put(
            url=f'http://{self.host}:{self.port}{self.prefix}{route}', json=data
        )

    def delete_request(self, route: str) -> Response:
        return httpx.delete(url=f'http://{self.host}:{self.port}{self.prefix}{route}')


def thread_decorator(m) -> typing.Callable:
    def wrapper(*args, **kwargs) -> None:
        for _ in range(100):
            t = threading.Thread(target=m(*args, **kwargs), daemon=True)
            t.start()
            t.join()

    return wrapper
