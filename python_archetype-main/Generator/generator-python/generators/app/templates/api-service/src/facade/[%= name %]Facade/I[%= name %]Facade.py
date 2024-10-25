from abc import abstractmethod, ABC
from ...common.Dtos.Response.[%= name %]Dto import [%= name %]Dto
from ...common.Dtos.Request.[%= name %]RequestDto import [%= name %]RequestDto

class I[%= name %]Facade(ABC):

    @abstractmethod
    def GetAllAsync(self) -> list[[%= name %]Dto]:
        pass

    @abstractmethod
    def GetByIdAsync(self, id: int) -> [%= name %]Dto:
        pass

    @abstractmethod
    def InsertAsync(self, request: [%= name %]RequestDto) -> bool:
        pass

    @abstractmethod
    def UpdateAsync(self, id: int, request: [%= name %]RequestDto) -> bool:
        pass

    @abstractmethod
    def DeleteAsync(self, id: int) -> bool:
        pass