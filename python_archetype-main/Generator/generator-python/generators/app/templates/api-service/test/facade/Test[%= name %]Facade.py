from unittest.mock import MagicMock
from src.facade.[%= name %]Facade.Impl.[%= name %]Facade import [%= name %]Facade
from src.common.Dtos.Response.[%= name %]Dto import [%= name %]Dto
from unittest import TestCase
from ..BaseTest import BaseTest
from src.services.[%= name %]Service.I[%= name %]Service import I[%= name %]Service

class Test[%= name %]Facade(TestCase, BaseTest):
    
    def setUp(self):
        self.mock[%= name %]Service = MagicMock(return_value = I[%= name %]Service)
        self.[%= name %]Facade = [%= name %]Facade(self.mock[%= name %]Service)
        
        data = [%= name %]Dto(1, 1, "Usuario 1", "user1", "user1@gmail.com", "system", "2023-08-03 14:40:10", "system", "2023-08-03 14:40:10", True)
        list = [data,]
        
        self.[%= name %]Facade.[%= name %]Service.GetAllAsync = MagicMock(return_value = list)
        self.[%= name %]Facade.[%= name %]Service.GetByIdAsync = MagicMock(return_value = data)
        self.[%= name %]Facade.[%= name %]Service.InsertAsync = MagicMock(return_value = True)
        self.[%= name %]Facade.[%= name %]Service.UpdateAsync = MagicMock(return_value = True)
        self.[%= name %]Facade.[%= name %]Service.DeleteAsync = MagicMock(return_value = True)
    
    def test_GetAllAsync(self):
        response = self.[%= name %]Facade.GetAllAsync()
        
        self.assertIsNotNone(response)
        self.assertEqual(1, len(response))
        
    def test_GetByIdAsync(self):
        id = 1
        response = self.[%= name %]Facade.GetByIdAsync(id)
        
        self.assertIsNotNone(response)
        self.assertEqual(id, response.Id)
        
    def test_InsertAsync(self):
        data = self.Get[%= name %]RequestDto()
        response = self.[%= name %]Facade.InsertAsync(data)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        
    def test_UpdateAsync(self):
        id = 1
        data = self.Get[%= name %]RequestDto()
        data["id"] = id
        response = self.[%= name %]Facade.UpdateAsync(id, data)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        
    def test_DeleteAsync(self):
        id = 1
        response = self.[%= name %]Facade.DeleteAsync(id)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)