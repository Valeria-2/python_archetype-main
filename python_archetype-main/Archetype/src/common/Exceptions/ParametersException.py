from http import HTTPStatus

class ParametersException(Exception):
    def __init__(self, message, httpStatus = HTTPStatus.INTERNAL_SERVER_ERROR):
        self.message = message
        self.httpStatus = httpStatus

        super().__init__(self.message)