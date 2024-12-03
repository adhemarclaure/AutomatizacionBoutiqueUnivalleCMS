from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager  
import requests
import time

class TestOverviewProductos:


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

    def test_carga_de_productos(self):
        time.sleep(1)
        actual=self.driver.find_element(By.XPATH, "//table//th[text() = 'Nombre']").text
        esperado="Nombre"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_despliegue_de_popup(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//table//tr[1]//Button").click()    
        actual=self.driver.find_element(By.XPATH, "//div[text() = 'Acciones']").text
        esperado="Acciones"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"
    
