import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class TestVote(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://buggy.justtestit.org/model/ckl2phsabijs71623vk0%7Cckl2phsabijs71623vng")

    def tearDown(self):
        self.driver.quit()  
        
    #TEST CASE 1
    def test_successful_vote(self):
        #buscando inputs para el login
        login_input = self.driver.find_element(By.NAME, "login")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success[type='submit']")
       
        #Llenando los datos
        login_input.send_keys("juanperez08")
        password_input.send_keys("Juanperez0@")
        
        #Hacer login
        login_button.click()
        
        self.driver.implicitly_wait(5)
        
        #buscando contador de votos
        vote_before = WebDriverWait(self.driver, timeout=5).until(lambda d: d.find_element(By.CSS_SELECTOR, ".card-block h4 strong"))
        vote_number_before = int(vote_before.text)
        
        #Hacer click en el boton de votar
        btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-block button")
        btn.click()
        time.sleep(8)
    
        try:
            vote_after =  WebDriverWait(self.driver, timeout=15).until(lambda d: d.find_element(By.CSS_SELECTOR, ".card-block h4 strong"))
            vote_number_after = int(vote_after.text)
            self.assertGreater(vote_number_after,vote_number_before)
            print("Voto exitoso") 
        except TimeoutException():
             self.fail("Fallo la votacion")
            
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
