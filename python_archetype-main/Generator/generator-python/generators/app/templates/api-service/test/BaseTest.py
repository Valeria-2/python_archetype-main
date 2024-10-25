from abc import ABC
from src.common.Dtos.Request.[%= name %]RequestDto import [%= name %]RequestDto
from src.common.Dtos.Response.[%= name %]Dto import [%= name %]Dto
from src.model.[%= name %]Model import [%= name %]Model
from datetime import datetime

class BaseTest(ABC):
    def Get[%= name %]RequestDto(self) -> [%= name %]RequestDto:
        return {
            "email": "user3@gmail.com",
            "name": "usuario 3",
            "roleId": 1,
            "username": "user3",
            "active": True
        }
        
    def Get[%= name %]Dto(self) -> [%= name %]Dto:
        return [%= name %]Dto(1, 1, "Usuario 1", "user1", "user1@gmail.com", "system", "2023-08-03 14:40:10", "system", "2023-08-03 14:40:10", True)
    
    def GetAll[%= name %]Model(self) -> list[[%= name %]Model]:
        return [
            [%= name %]Model(Id = 1, RoleId = 1, Name = "usuario 1", Username = "user1", Email = "user1@gmail.com", UserCreated = "system", Created = datetime.now(), UserModified = "system", Modified = datetime.now(), Active = True ),
            [%= name %]Model(Id = 2, RoleId = 1, Name = "usuario 2", Username = "user2", Email = "user2@gmail.com", UserCreated = "system", Created = datetime.now(), UserModified = "system", Modified = datetime.now(), Active = True )
        ]