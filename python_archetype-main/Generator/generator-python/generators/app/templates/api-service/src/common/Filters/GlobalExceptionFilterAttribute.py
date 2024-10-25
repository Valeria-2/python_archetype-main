from ..Dtos.ErrorMessageDto import ErrorMessageDto
from flask import jsonify

class GlobalExceptionFilterAttribute():
    # Manejador de errores para tu excepción personalizada
    def handle_custom_exception(error):
        errorMessage = ErrorMessageDto(error.httpStatus, error.message, "", error.message).__dict__
        return jsonify(errorMessage), error.httpStatus