from flask_sqlalchemy import SQLAlchemy # type: ignore
from injector import Binder, Module, singleton
from flask import Flask
from .DAO.[%= name %].I[%= name %]Dao import I[%= name %]Dao
from .DAO.[%= name %].Impl.[%= name %]Dao import [%= name %]Dao
from .Db.database import db
from ..model.[%= name %]Model import [%= name %]Model

class AddPersistence(Module):
    
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db, scope=singleton)
        binder.bind(Flask, to=Flask(__name__), scope=singleton)
        binder.bind([%= name %]Model, to=[%= name %]Model(), scope=singleton)
        binder.bind(I[%= name %]Dao, to=[%= name %]Dao(), scope=singleton)
        
        