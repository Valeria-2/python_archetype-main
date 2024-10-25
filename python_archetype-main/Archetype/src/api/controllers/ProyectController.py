from flask.views import MethodView
from ...facade.ProyectFacade.Impl.ProyectFacade import IProyectFacade
from ...common.Dtos.Request.ProyectRequestDto import ProyectRequestDto
from flask import jsonify
from . import router
from ..DependencyInjection import injector

class UsersController(MethodView):

    proyectFacade: IProyectFacade

    @router.route("", methods=["GET"])
    @router.response(status_code=200)
    def GetAllAsync():
        proyectFacade = injector.get(IProyectFacade)
        return jsonify(proyectFacade.GetAllAsync())
    
    @router.route("/<int:id>", methods=["GET"])
    @router.response(status_code=200)
    def GetByIdAsync(id: int):
        proyectFacade = injector.get(IProyectFacade)
        return jsonify(proyectFacade.GetByIdAsync(id))
    
    @router.route("", methods=["POST"])
    @router.response(201, ProyectRequestDto)
    @router.arguments(ProyectRequestDto)
    def InsertAsync(request: ProyectRequestDto):
        proyectFacade =  injector.get(IProyectFacade)
        return jsonify(proyectFacade.InsertAsync(request))

    @router.route("/<int:id>", methods=["PUT"])
    @router.response(201, ProyectRequestDto)
    @router.arguments(ProyectRequestDto)
    def UpdateAsync(request: ProyectRequestDto, id: int):
        proyectFacade =  injector.get(IProyectFacade)
        return jsonify(proyectFacade.UpdateAsync(id, request))
    
    @router.route("/<int:id>", methods=["DELETE"])
    @router.response(status_code=201)
    def DeleteAsync(id: int):
        proyectFacade =  injector.get(IProyectFacade)
        return jsonify(proyectFacade.DeleteAsync(id))
    
    @router.route("/ping", methods=["GET"])
    @router.response(status_code=200)
    def Ping():
        return jsonify("pong")
