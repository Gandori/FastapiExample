import importlib.util
import os
import pathlib

from fastapi import APIRouter, FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse

from src.middleware import Middleware
from src.service import Service

new_service: Service = Service()
prefix: str = new_service.prefix
routers: list[APIRouter] = []
endpoints_folder_path: str = 'src/endpoints'

app: FastAPI = new_service.create()

new_middlewares = Middleware()
new_middlewares.setup(app=app)

for folder in os.listdir(path=endpoints_folder_path):
    folder_path: str = f'{endpoints_folder_path}/{folder}'
    exist_folder: bool = pathlib.Path(folder_path).is_dir()

    if exist_folder and folder not in ['__pycache__']:
        files: list = os.listdir(path=folder_path)

        for file in files:
            if file in ['endpoints.py']:
                name: str = file.replace('.py', '')
                spec = importlib.util.spec_from_file_location(
                    name, f'{endpoints_folder_path}/{folder}/{name}.py'
                )
                module = spec.loader.load_module()
                app.include_router(router=module.router, prefix=prefix)


@app.on_event('startup')
async def startup() -> None:
    pass


@app.on_event('shutdown')
async def shutdown() -> None:
    pass


@app.exception_handler(404)
async def not_found(request: Request, exc: HTTPException) -> RedirectResponse:
    return RedirectResponse('/')
