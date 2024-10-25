from flask.views import MethodView
from ...facade.[%= name %]Facade.Impl.[%= name %]Facade import I[%= name %]Facade
from ...common.Dtos.Request.[%= name %]RequestDto import [%= name %]RequestDto
from flask import jsonify
from . import router
from ..DependencyInjection import injector

class UsersController(MethodView):

    [%= name %]Facade: I[%= name %]Facade

    @router.route("", methods=["GET"])
    @router.response(status_code=200)
    def GetAllAsync():
        [%= name %]Facade = injector.get(I[%= name %]Facade)
        return jsonify([%= name %]Facade.GetAllAsync())
    
    @router.route("/<int:id>", methods=["GET"])
    @router.response(status_code=200)
    def GetByIdAsync(id: int):
        [%= name %]Facade = injector.get(I[%= name %]Facade)
        return jsonify([%= name %]Facade.GetByIdAsync(id))
    
    @router.route("", methods=["POST"])
    @router.response(201, [%= name %]RequestDto)
    @router.arguments([%= name %]RequestDto)
    def InsertAsync(request: [%= name %]RequestDto):
        [%= name %]Facade =  injector.get(I[%= name %]Facade)
        return jsonify([%= name %]Facade.InsertAsync(request))

    @router.route("/<int:id>", methods=["PUT"])
    @router.response(201, [%= name %]RequestDto)
    @router.arguments([%= name %]RequestDto)
    def UpdateAsync(request: [%= name %]RequestDto, id: int):
        [%= name %]Facade =  injector.get(I[%= name %]Facade)
        return jsonify([%= name %]Facade.UpdateAsync(id, request))
    
    @router.route("/<int:id>", methods=["DELETE"])
    @router.response(status_code=201)
    def DeleteAsync(id: int):
        [%= name %]Facade =  injector.get(I[%= name %]Facade)
        return jsonify([%= name %]Facade.DeleteAsync(id))
    
    @router.route("/ping", methods=["GET"])
    @router.response(status_code=200)
    def Ping():
        return jsonify("pong")
