from starlette import status

from src.exeptions.base_exeption import BaseExeption


class CreatedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'User Erfolgreich Erstellt'


class DeletedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'User Erfolgreich Entfernt'


class NotFound(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'User Exestiert nicht'


class UpdatedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'Update Erfolgreich'
