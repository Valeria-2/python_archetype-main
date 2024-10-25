from injector import Binder, Module, singleton
from .ProyectService.IProyectService import IProyectService
from .ProyectService.Impl.ProyectService import ProyectService
from ..persistence.DAO.Proyect.Impl.ProyectDao import ProyectDao

class AddServices(Module):
    
    def configure(self, binder: Binder):
        binder.bind(IProyectService, to=ProyectService(ProyectDao()), scope=singleton)
        