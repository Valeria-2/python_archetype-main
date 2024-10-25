from abc import ABC, abstractmethod
from ...common.Dtos.Request.[%= name %]RequestDto import [%= name %]RequestDto
from ...common.Dtos.Response.[%= name %]Dto import [%= name %]Dto

class I[%= name %]Service(ABC):
    
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
