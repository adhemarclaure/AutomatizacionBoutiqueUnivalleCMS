from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager  
import requests
import time

class TestOEliminacionProductos:


    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get('https://boutique-univalle-next.vercel.app/login')
        self.driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("sergio@est.univalle.edu")
        self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secretPassword")
        self.driver.find_element(By.XPATH, "//button[text() = 'Continuar']").click()
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
        print("\nPrueba finalizada")

    def test_eliminacion_producto_cancelar(self):
        self.driver.find_element(By.XPATH, "//tr//td[text() = 'Prueba']//following::button[1]").click()
        self.driver.find_element(By.XPATH, "//span[text() = 'Eliminar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text() = 'Cancelar']").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH, "//h1[text() ='Productos']").text
        esperado="Productos"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_eliminacion_producto(self):
        self.driver.find_element(By.XPATH, "//tr//td[text() = 'Prueba']//following::button[1]").click()
        self.driver.find_element(By.XPATH, "//span[text() = 'Eliminar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'Eliminar']").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH, "//h1[text() ='Productos']").text
        esperado="Productos"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    
