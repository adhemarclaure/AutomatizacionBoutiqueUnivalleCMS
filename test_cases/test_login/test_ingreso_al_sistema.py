from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager  
import requests
import time

class TestIngresoAlSistema:


    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get('https://boutique-univalle-next.vercel.app/login')

        time.sleep(1)

    def teardown_method(self):
        self.driver.quit()
        print("\nPrueba finalizada")

    def test_ingreso_con_credenciales_incorrectas(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("error@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//button[text() = 'Continuar']").click()
        time.sleep(2)
        
        actual=self.driver.find_element(By.XPATH, "//h5").text
        esperado="Error"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"
    
    def test_ingreso_con_credenciales_correctas(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("sergio@est.univalle.edu")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secretPassword")
        self.driver.find_element(By.XPATH, "//button[text() = 'Continuar']").click()
        time.sleep(5)
        
        actual=self.driver.find_element(By.XPATH, "//span[text() = 'Boutique Univalle']").text
        esperado="Boutique Univalle"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"