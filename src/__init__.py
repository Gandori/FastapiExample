import importlib.util
import os

from fastapi import APIRouter, FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse

from src.database import db
from src.middleware import Middleware
from src.service import Service

new_service: Service = Service()
prefix: str = new_service.prefix
routers: list[APIRouter] = []
endpoints_folder_path: str = 'src/endpoints'

app: FastAPI = new_service.create()

new_middlewares = Middleware()
new_middlewares.setup(app=app)


for i in os.listdir(endpoints_folder_path):
    if i not in ['__init__.py', '__pycache__']:
        name: str = i.replace('.py', '')
        spec = importlib.util.spec_from_file_location(
            name, f'{endpoints_folder_path}/{name}.py'
        )
        module = spec.loader.load_module()
        app.include_router(router=module.router, prefix=prefix)


@app.on_event('startup')
async def startup() -> None:
    await db.create_tables()

    path: str = 'src/sql'
    for file_name in os.listdir(path):
        with open(f'{path}/{file_name}', mode='r') as file:
            for query in file.read().split(';'):
                if query != '':
                    await db.execute(query=query)


@app.on_event('shutdown')
async def shutdown() -> None:
    await db.drop_tables()


@app.exception_handler(404)
async def not_found(request: Request, exc: HTTPException) -> RedirectResponse:
    return RedirectResponse('/')
