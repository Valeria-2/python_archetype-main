from injector import Binder, Module, singleton
from .ProyectFacade.IProyectFacade import IProyectFacade
from .ProyectFacade.Impl.ProyectFacade import ProyectFacade
from ..persistence.DAO.Proyect.Impl.ProyectDao import ProyectDao
from ..services.ProyectService.Impl.ProyectService import ProyectService
from ..facade.ProyectFacade.IProyectFacade import IProyectFacade
from ..facade.ProyectFacade.Impl.ProyectFacade import ProyectFacade

class AddFacade(Module):
    
    def configure(self, binder: Binder):
        binder.bind(IProyectFacade, to=ProyectFacade(ProyectService(ProyectDao())), scope=singleton)
        
        