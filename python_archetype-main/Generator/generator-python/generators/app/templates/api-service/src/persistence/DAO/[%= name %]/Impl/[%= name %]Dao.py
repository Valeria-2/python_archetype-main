from .....model.[%= name %]Model  import [%= name %]Model
from ..I[%= name %]Dao import I[%= name %]Dao
from .....model.[%= name %]Model import db

class [%= name %]Dao(I[%= name %]Dao):
    
    def GetAllAsync(self) -> list[[%= name %]Model]:
        return db.session.query([%= name %]Model).filter([%= name %]Model.Active == True).all()

    def GetByIdAsync(self, id: int) -> [%= name %]Model:
        return db.session.get([%= name %]Model, id)

    def GetByEmailAsync(self, email: str) -> [%= name %]Model:
        return db.session.query([%= name %]Model).filter([%= name %]Model.Email == email).first()

    def InsertAsync(self, model: [%= name %]Model) -> bool:
        db.session.add(model)
        db.session.commit()
        return True

    def UpdateAsync(self) -> bool:
        db.session.commit()
        return True
