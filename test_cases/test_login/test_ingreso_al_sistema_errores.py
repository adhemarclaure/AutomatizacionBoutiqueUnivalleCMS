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

    def test_ingreso_con_dominio_incorrecto(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("error@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//button[text() = 'Continuar']").click()
        time.sleep(2)
        
        actual=self.driver.find_element(By.XPATH, "//div[text() = 'Usuario no encontrado']").text
        esperado="Usuario no encontrado"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_ingreso_con_usuario_incorrecto(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("error@est.univalle.edu")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//button[text() = 'Continuar']").click()
        time.sleep(2)
        
        actual=self.driver.find_element(By.XPATH, "//div[text() = 'Usuario no encontrado']").text
        esperado="Usuario no encontrado"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_ingreso_con_contraseña_incorrecta(self):
        self.driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("sergio@est.univalle.edu")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//button[text() = 'Continuar']").click()
        time.sleep(2)
        
        actual=self.driver.find_element(By.XPATH, "//div[text() = 'Autorizacion denegada, revise las credenciales']").text
        esperado="Autorizacion denegada, revise las credenciales"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"
    
