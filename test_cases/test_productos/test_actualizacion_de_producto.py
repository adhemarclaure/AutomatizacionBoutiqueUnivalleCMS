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

    def test_despliegue_drawer_actualización(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//tr//td[text() = 'Prueba']//following::button[1]").click()
        self.driver.find_element(By.XPATH, "//span[text() = 'Editar']").click()
        time.sleep(1)
        actual=self.driver.find_element(By.XPATH, "//h2").text
        esperado="Actualizar Producto"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_actualizacion_nombre(self):
        self.driver.find_element(By.XPATH, "//tr//td[text() = 'Prueba']//following::button[1]").click()
        self.driver.find_element(By.XPATH, "//span[text() = 'Editar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys("Prueba")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'Actualizar']").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH, "//div[text() ='Producto Actualizado']").text
        esperado="Producto Actualizado"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

