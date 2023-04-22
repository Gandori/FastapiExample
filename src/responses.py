from fastapi.responses import JSONResponse


class Response:
    def __init__(self, message: str, status_code: int) -> None:
        self.message: str = message
        self.status_code: int = status_code

    def response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code, content={'message': self.message}
        )


class Error(Response):
    def __init__(self) -> None:
        self.message: str = 'Es ist ein Fehler aufgetreten.'
        self.status_code: int = 200
        super().__init__(message=self.message, status_code=self.status_code)
