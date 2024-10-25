from unittest.mock import MagicMock
from src.facade.ProyectFacade.Impl.ProyectFacade import ProyectFacade
from src.common.Dtos.Response.ProyectDto import ProyectDto
from unittest import TestCase
from ..BaseTest import BaseTest
from src.services.ProyectService.IProyectService import IProyectService

class TestProyectFacade(TestCase, BaseTest):
    
    def setUp(self):
        self.mockProyectService = MagicMock(return_value = IProyectService)
        self.proyectFacade = ProyectFacade(self.mockProyectService)
        
        data = ProyectDto(1, 1, "Usuario 1", "user1", "user1@gmail.com", "system", "2023-08-03 14:40:10", "system", "2023-08-03 14:40:10", True)
        list = [data,]
        
        self.proyectFacade.proyectService.GetAllAsync = MagicMock(return_value = list)
        self.proyectFacade.proyectService.GetByIdAsync = MagicMock(return_value = data)
        self.proyectFacade.proyectService.InsertAsync = MagicMock(return_value = True)
        self.proyectFacade.proyectService.UpdateAsync = MagicMock(return_value = True)
        self.proyectFacade.proyectService.DeleteAsync = MagicMock(return_value = True)
    
    def test_GetAllAsync(self):
        response = self.proyectFacade.GetAllAsync()
        
        self.assertIsNotNone(response)
        self.assertEqual(1, len(response))
        
    def test_GetByIdAsync(self):
        id = 1
        response = self.proyectFacade.GetByIdAsync(id)
        
        self.assertIsNotNone(response)
        self.assertEqual(id, response.Id)
        
    def test_InsertAsync(self):
        data = self.GetProyectRequestDto()
        response = self.proyectFacade.InsertAsync(data)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        
    def test_UpdateAsync(self):
        id = 1
        data = self.GetProyectRequestDto()
        data["id"] = id
        response = self.proyectFacade.UpdateAsync(id, data)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)
        
    def test_DeleteAsync(self):
        id = 1
        response = self.proyectFacade.DeleteAsync(id)
        
        self.assertIsNotNone(response)
        self.assertTrue(response)