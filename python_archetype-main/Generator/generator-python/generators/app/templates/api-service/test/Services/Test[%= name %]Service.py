from src.services.[%= name %]Service.Impl.[%= name %]Service import [%= name %]Service
from unittest import TestCase
from src.model.[%= name %]Model import [%= name %]Model
from config import config
from src.api import InitController
from ..BaseTest import BaseTest
from .Util.FunctionsUtil import FunctionsUtil
from src.common.Exceptions.BusinessException import BusinessException
from src.persistence.DAO.[%= name %].Impl.[%= name %]Dao import [%= name %]Dao
from src.persistence.Db.database import db

class Test[%= name %]Service(TestCase, BaseTest):   
    
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

        self.mock[%= name %]Dao = [%= name %]Dao()
        self.[%= name %]Service = [%= name %]Service(self.mock[%= name %]Dao)
        
    def setUp(self):
        FunctionsUtil.DeleteAllRecords()
        db.session.add_all(self.GetAll[%= name %]Model())
        db.session.commit()
        
        
    def test_GetAllAsync(self):
        response = self.[%= name %]Service.GetAllAsync()
        self.assertIsNotNone(response)
        self.assertEqual(2, len(response))
     
    def test_GetByIdAsync(self):
        id = 1
        username = "user1"
        response = self.[%= name %]Service.GetByIdAsync(id)
        
        self.assertIsNotNone(response)
        self.assertEqual(id, response["Id"])
        self.assertEqual(username, response["Username"])
        
    def test_InsertAsync(self):
        data = self.Get[%= name %]RequestDto()
        
        before = [%= name %]Model.query.all()
        response = self.[%= name %]Service.InsertAsync(data)
        after = [%= name %]Model.query.all()
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        self.assertEqual(len(before) + 1, len(after))
        
    def test_InsertAsyncBusinessException(self):
        data = self.Get[%= name %]RequestDto()
        data["email"] = "user1@gmail.com"
        with self.assertRaises(BusinessException):
            self.[%= name %]Service.InsertAsync(data)
        
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
        
        response = self.[%= name %]Service.UpdateAsync(id, data)
        after = self.controller.db.session.get([%= name %]Model, id)
        
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
            self.[%= name %]Service.UpdateAsync(id, data)
        
    def test_DeleteAsync(self):
        id = 2
        response = self.[%= name %]Service.DeleteAsync(id)
        after = db.session.get([%= name %]Model, id)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        self.assertFalse(after.Active)
        
    def test_DeleteAsyncBusinessException(self):
        id = 100
        with self.assertRaises(BusinessException):
            self.[%= name %]Service.DeleteAsync(id)