from ..I[%= name %]Facade import I[%= name %]Facade
from ....services.[%= name %]Service.Impl.[%= name %]Service import [%= name %]Service
from ....services.[%= name %]Service.Impl.[%= name %]Service import I[%= name %]Service
from ....common.Dtos.Response.[%= name %]Dto import [%= name %]Dto
from ....common.Dtos.Request.[%= name %]RequestDto import [%= name %]RequestDto
from injector import inject

class [%= name %]Facade(I[%= name %]Facade):

    [%= name %]Facade: I[%= name %]Facade
    [%= name %]Service: [%= name %]Service

    @inject
    def __init__(self, [%= name %]Service: I[%= name %]Service):
        self.[%= name %]Service = [%= name %]Service

    def GetAllAsync(self) -> list[[%= name %]Dto]:
        return self.[%= name %]Service.GetAllAsync()

    def GetByIdAsync(self, id: int) -> [%= name %]Dto:
        return self.[%= name %]Service.GetByIdAsync(id)

    def InsertAsync(self, request: [%= name %]RequestDto) -> bool:
        return self.[%= name %]Service.InsertAsync(request)

    def UpdateAsync(self, id: int, request: [%= name %]RequestDto) -> bool:
        return self.[%= name %]Service.UpdateAsync(id, request)

    def DeleteAsync(self, id: int) -> bool:
        return self.[%= name %]Service.DeleteAsync(id)
