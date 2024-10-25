from src.services.ProyectService.Impl.ProyectService import ProyectService
from unittest import TestCase
from src.model.ProyectModel import ProyectModel
from config import config
from src.api import InitController
from ..BaseTest import BaseTest
from .Util.FunctionsUtil import FunctionsUtil
from src.common.Exceptions.BusinessException import BusinessException
from src.persistence.DAO.Proyect.Impl.ProyectDao import ProyectDao
from src.persistence.Db.database import db

class TestProyectService(TestCase, BaseTest):   
    
    @classmethod
    def setUpClass(self):
        configuration = config["development"]
        configuration.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        configuration.SQLALCHEMY_TRACK_MODIFICATIONS = False
        
        self.controller = InitController()
        self.app = self.controller.init_app(configuration)
        
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.mockProyectDao = ProyectDao()
        self.proyectService = ProyectService(self.mockProyectDao)
        
    def setUp(self):
        FunctionsUtil.DeleteAllRecords()
        db.session.add_all(self.GetAllProyectModel())
        db.session.commit()
        
        
    def test_GetAllAsync(self):
        response = self.proyectService.GetAllAsync()
        self.assertIsNotNone(response)
        self.assertEqual(2, len(response))
     
    def test_GetByIdAsync(self):
        id = 1
        username = "user1"
        response = self.proyectService.GetByIdAsync(id)
        
        self.assertIsNotNone(response)
        self.assertEqual(id, response["Id"])
        self.assertEqual(username, response["Username"])
        
    def test_InsertAsync(self):
        data = self.GetProyectRequestDto()
        
        before = ProyectModel.query.all()
        response = self.proyectService.InsertAsync(data)
        after = ProyectModel.query.all()
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        self.assertEqual(len(before) + 1, len(after))
        
    def test_InsertAsyncBusinessException(self):
        data = self.GetProyectRequestDto()
        data["email"] = "user1@gmail.com"
        with self.assertRaises(BusinessException):
            self.proyectService.InsertAsync(data)
        
    def test_UpdateAsync(self):
        id = 1
        username = "user01"
        data = {
            "id": id,
            "email": "user1@gmail.com",
            "name": "usuario 1",
            "roleId": 1,
            "username": username,
            "active": True
        }
        
        response = self.proyectService.UpdateAsync(id, data)
        after = self.controller.db.session.get(ProyectModel, id)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        self.assertEqual(username, after.Username)
        
    def test_UpdateAsyncBusinessException(self):
        id = 100
        username = "user01"
        data = {
            "id": id,
            "email": "user1@gmail.com",
            "name": "usuario 1",
            "roleId": 1,
            "username": username,
            "active": True
        }
        
        with self.assertRaises(BusinessException):
            self.proyectService.UpdateAsync(id, data)
        
    def test_DeleteAsync(self):
        id = 2
        response = self.proyectService.DeleteAsync(id)
        after = db.session.get(ProyectModel, id)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        self.assertFalse(after.Active)
        
    def test_DeleteAsyncBusinessException(self):
        id = 100
        with self.assertRaises(BusinessException):
            self.proyectService.DeleteAsync(id)