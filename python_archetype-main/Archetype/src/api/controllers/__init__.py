from flask_smorest import Blueprint
from  ...common.Filters.GlobalExceptionFilterAttribute import GlobalExceptionFilterAttribute

router = Blueprint(
    "Proyect", "ProyectController", url_prefix="/api/Proyect", description="Proyect API"
)

router.register_error_handler(Exception, GlobalExceptionFilterAttribute.handle_custom_exception)
from src.api.controllers.ProyectController import *