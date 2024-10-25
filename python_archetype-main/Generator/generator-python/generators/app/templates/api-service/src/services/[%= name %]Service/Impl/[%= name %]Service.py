from ..I[%= name %]Service import I[%= name %]Service
from ....persistence.DAO.[%= name %] import I[%= name %]Dao
from ....model.[%= name %]Model import [%= name %]Model
from ....common.Dtos.Response.[%= name %]Dto import [%= name %]Dto
from ....common.Util.ValidatorUtil import ValidatorUtil
from ....common.Dtos.Request.[%= name %]RequestDto import [%= name %]RequestDto
from datetime import datetime
from injector import inject

class [%= name %]Service(I[%= name %]Service):

    @inject
    def __init__(self, [%= name %]Dao: I[%= name %]Dao):
        self.[%= name %]Dao = [%= name %]Dao

    def GetAllAsync(self) -> list[[%= name %]Dto]:
        users = self.[%= name %]Dao.GetAllAsync()
        result = [[%= name %]Dto(user.Id, user.RoleId, user.Name, user.Username, user.Email,
                         user.UserCreated, user.Created, user.UserModified,
                         user.Modified, user.Active).__dict__
        for user in users]
        return result
    
    def GetByIdAsync(self, id: int) -> [%= name %]Dto:
        model = self.[%= name %]Dao.GetByIdAsync(id)
        ValidatorUtil.ValidateRequired(model, "El usuario no existe en la base de datos.")
            
        result = [%= name %]Dto(model.Id, model.RoleId, model.Name, model.Username, model.Email,
            model.UserCreated, model.Created, model.UserModified,
            model.Modified, model.Active).__dict__
        
        return result
    
    def InsertAsync(self, request: [%= name %]RequestDto) -> bool:
        ValidatorUtil.ValidateNotRequired(
            self.[%= name %]Dao.GetByEmailAsync(request["email"]),
            "El correo electronico ya existe.")
        
        now = datetime.now()
        model = [%= name %]Model(
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
        
        return self.[%= name %]Dao.InsertAsync(model) 
    
    def UpdateAsync(self, id: int, request: [%= name %]RequestDto) -> bool:
        dto = [%= name %]Dto(
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
        
        model = self.[%= name %]Dao.GetByIdAsync(id)
        ValidatorUtil.ValidateRequired(model, "El usuario no existe en la base de datos.")
        
        model.RoleId = dto.RoleId
        model.Name = dto.Name
        model.Username = dto.Username
        model.Email = dto.Email
        model.Modified = datetime.now()
        model.UserModified = "system"
        model.Active = dto.Active
        
        response = self.[%= name %]Dao.UpdateAsync()
        return response
    
    def DeleteAsync(self, id: int) -> bool:
        model = self.[%= name %]Dao.GetByIdAsync(id)
        ValidatorUtil.ValidateRequired(model, "El usuario no existe en la base de datos.")
        
        model.Modified = datetime.now()
        model.UserModified = "system"
        model.Active = False
        
        response = self.[%= name %]Dao.UpdateAsync()
        return response
    
