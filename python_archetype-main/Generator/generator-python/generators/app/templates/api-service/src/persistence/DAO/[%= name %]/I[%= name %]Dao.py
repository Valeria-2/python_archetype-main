from abc import ABC, abstractmethod
from ....model.[%= name %]Model import [%= name %]Model

class I[%= name %]Dao(ABC):

    @abstractmethod
    def GetAllAsync(self) -> list[[%= name %]Model]:
        pass

    @abstractmethod
    def GetByIdAsync(self, id: int) -> [%= name %]Model:
        pass

    @abstractmethod
    def GetByEmailAsync(self, email: str) -> [%= name %]Model:
        pass

    @abstractmethod
    def InsertAsync(self, model: [%= name %]Model) -> bool:
        pass

    @abstractmethod
    def UpdateAsync(self) -> bool:
        pass
