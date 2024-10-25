from ..IProyectFacade import IProyectFacade
from ....services.ProyectService.Impl.ProyectService import ProyectService
from ....services.ProyectService.Impl.ProyectService import IProyectService
from ....common.Dtos.Response.ProyectDto import ProyectDto
from ....common.Dtos.Request.ProyectRequestDto import ProyectRequestDto
from injector import inject

class ProyectFacade(IProyectFacade):

    proyectFacade: IProyectFacade
    proyectService: ProyectService

    @inject
    def __init__(self, proyectService: IProyectService):
        self.proyectService = proyectService

    def GetAllAsync(self) -> list[ProyectDto]:
        return self.proyectService.GetAllAsync()

    def GetByIdAsync(self, id: int) -> ProyectDto:
        return self.proyectService.GetByIdAsync(id)

    def InsertAsync(self, request: ProyectRequestDto) -> bool:
        return self.proyectService.InsertAsync(request)

    def UpdateAsync(self, id: int, request: ProyectRequestDto) -> bool:
        return self.proyectService.UpdateAsync(id, request)

    def DeleteAsync(self, id: int) -> bool:
        return self.proyectService.DeleteAsync(id)
