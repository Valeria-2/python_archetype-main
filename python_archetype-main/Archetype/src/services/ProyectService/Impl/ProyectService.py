from ..IProyectService import IProyectService
from ....persistence.DAO.Proyect import IProyectDao
from ....model.ProyectModel import ProyectModel
from ....common.Dtos.Response.ProyectDto import ProyectDto
from ....common.Util.ValidatorUtil import ValidatorUtil
from ....common.Dtos.Request.ProyectRequestDto import ProyectRequestDto
from datetime import datetime
from injector import inject

class ProyectService(IProyectService):

    @inject
    def __init__(self, proyectDao: IProyectDao):
        self.proyectDao = proyectDao

    def GetAllAsync(self) -> list[ProyectDto]:
        users = self.proyectDao.GetAllAsync()
        result = [ProyectDto(user.Id, user.RoleId, user.Name, user.Username, user.Email,
                         user.UserCreated, user.Created, user.UserModified,
                         user.Modified, user.Active).__dict__
        for user in users]
        return result
    
    def GetByIdAsync(self, id: int) -> ProyectDto:
        model = self.proyectDao.GetByIdAsync(id)
        ValidatorUtil.ValidateRequired(model, "El usuario no existe en la base de datos.")
            
        result = ProyectDto(model.Id, model.RoleId, model.Name, model.Username, model.Email,
            model.UserCreated, model.Created, model.UserModified,
            model.Modified, model.Active).__dict__
        
        return result
    
    def InsertAsync(self, request: ProyectRequestDto) -> bool:
        ValidatorUtil.ValidateNotRequired(
            self.proyectDao.GetByEmailAsync(request["email"]),
            "El correo electronico ya existe.")
        
        now = datetime.now()
        model = ProyectModel(
            RoleId = request["roleId"],
            Name = request["name"],
            Username = request["username"],
            Email = request["email"]
        )
        
        model.Id = None
        model.Created = now
        model.UserCreated = "system"
        model.Modified = now
        model.UserModified = "system"
        model.Active = True
        
        return self.proyectDao.InsertAsync(model) 
    
    def UpdateAsync(self, id: int, request: ProyectRequestDto) -> bool:
        dto = ProyectDto(
            request["id"],
            request["roleId"],
            request["name"],
            request["username"],
            request["email"],
            "",
            datetime.now(),
            "",
            datetime.now(),
            request["active"])
        
        model = self.proyectDao.GetByIdAsync(id)
        ValidatorUtil.ValidateRequired(model, "El usuario no existe en la base de datos.")
        
        model.RoleId = dto.RoleId
        model.Name = dto.Name
        model.Username = dto.Username
        model.Email = dto.Email
        model.Modified = datetime.now()
        model.UserModified = "system"
        model.Active = dto.Active
        
        response = self.proyectDao.UpdateAsync()
        return response
    
    def DeleteAsync(self, id: int) -> bool:
        model = self.proyectDao.GetByIdAsync(id)
        ValidatorUtil.ValidateRequired(model, "El usuario no existe en la base de datos.")
        
        model.Modified = datetime.now()
        model.UserModified = "system"
        model.Active = False
        
        response = self.proyectDao.UpdateAsync()
        return response
    
