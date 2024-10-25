from flask_smorest import Blueprint
from  ...common.Filters.GlobalExceptionFilterAttribute import GlobalExceptionFilterAttribute

router = Blueprint(
    "[%= name %]", "[%= name %]Controller", url_prefix="/api/[%= name %]", description="[%= name %] API"
)

router.register_error_handler(Exception, GlobalExceptionFilterAttribute.handle_custom_exception)
from src.api.controllers.[%= name %]Controller import *