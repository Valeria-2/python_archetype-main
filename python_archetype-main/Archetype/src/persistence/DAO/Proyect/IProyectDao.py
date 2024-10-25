from abc import ABC, abstractmethod
from ....model.ProyectModel import ProyectModel

class IProyectDao(ABC):

    @abstractmethod
    def GetAllAsync(self) -> list[ProyectModel]:
        pass

    @abstractmethod
    def GetByIdAsync(self, id: int) -> ProyectModel:
        pass

    @abstractmethod
    def GetByEmailAsync(self, email: str) -> ProyectModel:
        pass

    @abstractmethod
    def InsertAsync(self, model: ProyectModel) -> bool:
        pass

    @abstractmethod
    def UpdateAsync(self) -> bool:
        pass
