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

    def test_despliegue_drawer_creacion(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//h1//following::button[1]").click()
        time.sleep(1)
        actual=self.driver.find_element(By.XPATH, "//h2").text
        esperado="Crea un nuevo producto"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_creacion_sin_datos(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//h1//following::button[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'Crear']").click()
        actual=self.driver.find_element(By.XPATH, "//p[text() ='EL nombre del producto es requerido']").text
        esperado="EL nombre del producto es requerido"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"

    def test_creacion_de_producto(self):
        self.driver.find_element(By.XPATH, "//h1//following::button[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys('Prueba')
        self.driver.find_element(By.XPATH, "//input[@name = 'unitPrice']").send_keys('10')
        self.driver.find_element(By.XPATH, "//input[@id = 'image']").send_keys('C:/Users/Adhemar/Workspace/applitools/test_cases/test_productos/polera.jpg')
        self.driver.find_element(By.XPATH, "//button[text() = 'Crear']").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH, "//div[text() ='Producto creado']").text
        esperado="Producto creado"
        assert esperado == actual, f"FAIL: actual: {actual}, esperado {esperado}"
