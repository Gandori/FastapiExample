import pydantic
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware


class Middleware(pydantic.BaseSettings):
    allowed_hosts: str = '*'

    def __init__(self) -> None:
        super().__init__()

    def setup(self, app: FastAPI) -> None:
        allowed_hosts: list = self.allowed_hosts.split(',')
        app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
