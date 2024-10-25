from flask_sqlalchemy import SQLAlchemy # type: ignore
from injector import Binder, Module, singleton
from flask import Flask
from .DAO.Proyect.IProyectDao import IProyectDao
from .DAO.Proyect.Impl.ProyectDao import ProyectDao
from .Db.database import db
from ..model.ProyectModel import ProyectModel

class AddPersistence(Module):
    
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db, scope=singleton)
        binder.bind(Flask, to=Flask(__name__), scope=singleton)
        binder.bind(ProyectModel, to=ProyectModel(), scope=singleton)
        binder.bind(IProyectDao, to=ProyectDao(), scope=singleton)
        
        