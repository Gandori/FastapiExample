from starlette import status

from src.exeptions.base_exeption import BaseExeption


class ItemCreatedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'Item Erfolgreich Erstellt'


class ItemDeletedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'Item Erfolgreich Entfernt'


class ItemNotFound(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'Item Exestiert nicht'


class ItemUpdatedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'Item Update Erfolgreich'
