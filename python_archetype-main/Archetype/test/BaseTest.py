from abc import ABC
from src.common.Dtos.Request.ProyectRequestDto import ProyectRequestDto
from src.common.Dtos.Response.ProyectDto import ProyectDto
from src.model.ProyectModel import ProyectModel
from datetime import datetime

class BaseTest(ABC):
    def GetProyectRequestDto(self) -> ProyectRequestDto:
        return {
            "email": "user3@gmail.com",
            "name": "usuario 3",
            "roleId": 1,
            "username": "user3",
            "active": True
        }
        
    def GetProyectDto(self) -> ProyectDto:
        return ProyectDto(1, 1, "Usuario 1", "user1", "user1@gmail.com", "system", "2023-08-03 14:40:10", "system", "2023-08-03 14:40:10", True)
    
    def GetAllProyectModel(self) -> list[ProyectModel]:
        return [
            ProyectModel(Id = 1, RoleId = 1, Name = "usuario 1", Username = "user1", Email = "user1@gmail.com", UserCreated = "system", Created = datetime.now(), UserModified = "system", Modified = datetime.now(), Active = True ),
            ProyectModel(Id = 2, RoleId = 1, Name = "usuario 2", Username = "user2", Email = "user2@gmail.com", UserCreated = "system", Created = datetime.now(), UserModified = "system", Modified = datetime.now(), Active = True )
        ]