import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://buggy.justtestit.org")

    def tearDown(self):
        self.driver.quit()  
        
    #TEST CASE 1
    def test_successful_login(self):
        #nombre de la cuenta
        name = "Juan"
        
        #Esperar que la pagina cargue
        self.driver.implicitly_wait(10)
        #buscando inputs
        login_input = self.driver.find_element(By.NAME, "login")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success[type='submit']")
        
        #Llenando los datos
        login_input.send_keys("juanperez01")
        password_input.send_keys("Juanperez0@")
         
        #mandado el formulario
        login_button.click() 
  
        #validacion que se creo
        try:
            success_login = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, "span.nav-link.disabled"))
            self.assertIn("Hi, " + name, success_login.text)
            print("Inicio de sesion exitoso")
            
        except TimeoutException():
            self.fail("Inicio de sesion fallo")
            
    #TEST CASE 2  
    def test_fail_login(self):        
        #Esperar que la pagina cargue
        self.driver.implicitly_wait(10)
        #buscando inputs
        login_input = self.driver.find_element(By.NAME, "login")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success[type='submit']")
        
        #Llenando los datos
        login_input.send_keys("juanperez01")
        password_input.send_keys("123")
         
        #mandado el formulario
        login_button.click() 
  
        #validacion que se creo
        try:
            fail_login = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, "span.label.label-warning"))
            self.assertIn("Invalid username/password", fail_login.text)
            print("Fallo en inicio sesion")            
        except TimeoutException():
            self.fail("Inicio de sesion")
            
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
