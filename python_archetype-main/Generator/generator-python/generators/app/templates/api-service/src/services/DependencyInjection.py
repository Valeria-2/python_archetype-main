from injector import Binder, Module, singleton
from .[%= name %]Service.I[%= name %]Service import I[%= name %]Service
from .[%= name %]Service.Impl.[%= name %]Service import [%= name %]Service
from ..persistence.DAO.[%= name %].Impl.[%= name %]Dao import [%= name %]Dao

class AddServices(Module):
    
    def configure(self, binder: Binder):
        binder.bind(I[%= name %]Service, to=[%= name %]Service([%= name %]Dao()), scope=singleton)
        