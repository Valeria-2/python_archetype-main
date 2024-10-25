from .....model.ProyectModel  import ProyectModel
from ..IProyectDao import IProyectDao
from .....model.ProyectModel import db

class ProyectDao(IProyectDao):
    
    def GetAllAsync(self) -> list[ProyectModel]:
        return db.session.query(ProyectModel).filter(ProyectModel.Active == True).all()

    def GetByIdAsync(self, id: int) -> ProyectModel:
        return db.session.get(ProyectModel, id)

    def GetByEmailAsync(self, email: str) -> ProyectModel:
        return db.session.query(ProyectModel).filter(ProyectModel.Email == email).first()

    def InsertAsync(self, model: ProyectModel) -> bool:
        db.session.add(model)
        db.session.commit()
        return True

    def UpdateAsync(self) -> bool:
        db.session.commit()
        return True
