from injector import Binder, Module, singleton
from .[%= name %]Facade.I[%= name %]Facade import I[%= name %]Facade
from .[%= name %]Facade.Impl.[%= name %]Facade import [%= name %]Facade
from ..persistence.DAO.[%= name %].Impl.[%= name %]Dao import [%= name %]Dao
from ..services.[%= name %]Service.Impl.[%= name %]Service import [%= name %]Service
from ..facade.[%= name %]Facade.I[%= name %]Facade import I[%= name %]Facade
from ..facade.[%= name %]Facade.Impl.[%= name %]Facade import [%= name %]Facade

class AddFacade(Module):
    
    def configure(self, binder: Binder):
        binder.bind(I[%= name %]Facade, to=[%= name %]Facade([%= name %]Service([%= name %]Dao())), scope=singleton)
        
        