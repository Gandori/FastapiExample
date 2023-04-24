from starlette import status

from src.exeptions.base_exeption import BaseExeption


class UserCreatedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'User Erfolgreich Erstellt'


class UserDeletedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'User Erfolgreich Entfernt'


class UserNotFound(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'User Exestiert nicht'


class UserUpdatedSucess(BaseExeption):
    status_code = status.HTTP_200_OK
    message = 'Update Erfolgreich'
