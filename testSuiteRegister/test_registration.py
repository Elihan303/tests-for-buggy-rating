import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://buggy.justtestit.org/register")

    def tearDown(self):
        self.driver.quit()  
        
    #TEST CASE 1
    def test_successful_registration(self):
        #Esperar que la pagina cargue
        self.driver.implicitly_wait(10)
        #buscando inputs
        username_input = self.driver.find_element(By.ID, "username")
        first_name_input = self.driver.find_element(By.ID, "firstName")
        last_name_input = self.driver.find_element(By.ID, "lastName")
        password_input = self.driver.find_element(By.ID, "password")
        confirm_password_input = self.driver.find_element(By.ID, "confirmPassword")
        submit_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
    
        
        #Llenando los datos
        username_input.send_keys('juanperez12')
        first_name_input.send_keys("Juan")
        last_name_input.send_keys("Perez")
        password_input.send_keys("Juanperez0@")
        confirm_password_input.send_keys("Juanperez0@")
        #mandado el formulario
        submit_button.click()
  
        #validacion que se creo
        try:
            success_message = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, "alert-success"))
            self.assertIn("Registration is successful", success_message.text)
            print("Registro exitoso")
            
        except TimeoutException():
            self.fail("Registro fallo")
    
    #TEST CASE 2       
    def test_fail_registration(self):
        #Esperar que la pagina cargue
        self.driver.implicitly_wait(10)
        #buscando inputs
        username_input = self.driver.find_element(By.ID, "username")
        first_name_input = self.driver.find_element(By.ID, "firstName")
        last_name_input = self.driver.find_element(By.ID, "lastName")
        password_input = self.driver.find_element(By.ID, "password")
        confirm_password_input = self.driver.find_element(By.ID, "confirmPassword")
        submit_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
    
        #Llenando los datos
        username_input.send_keys('juanperez01')
        first_name_input.send_keys("Juan")
        last_name_input.send_keys("Perez")
        password_input.send_keys("Juanperez0@")
        confirm_password_input.send_keys("Juanperez0@")
        #mandado el formulario
        submit_button.click()
  
        try:
            error_message = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "//div[@class='result alert alert-danger']"))
            self.assertIn("UsernameExistsException: User already exists", error_message.text)
            print("No se registro con un user name ya creado")
            
        except TimeoutException():
            self.fail("Se registro con un user name ya existen")
            
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())

    