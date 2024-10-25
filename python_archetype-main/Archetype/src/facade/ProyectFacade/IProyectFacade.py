from abc import abstractmethod, ABC
from ...common.Dtos.Response.ProyectDto import ProyectDto
from ...common.Dtos.Request.ProyectRequestDto import ProyectRequestDto

class IProyectFacade(ABC):

    @abstractmethod
    def GetAllAsync(self) -> list[ProyectDto]:
        pass

    @abstractmethod
    def GetByIdAsync(self, id: int) -> ProyectDto:
        pass

    @abstractmethod
    def InsertAsync(self, request: ProyectRequestDto) -> bool:
        pass

    @abstractmethod
    def UpdateAsync(self, id: int, request: ProyectRequestDto) -> bool:
        pass

    @abstractmethod
    def DeleteAsync(self, id: int) -> bool:
        pass