import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Cotizaciones(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home = 'https://www.banistmo.com/wps/portal/banistmo/empresas'

    def test_RetoBanistmo(self):
        driver = self.driver
        driver.get(self.home)
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)  # Esperas dinámicas con un timeout de 10s

        # Aceptar cookies
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Entendido')]"))).click()

        # Navegar a Cuentas
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='navbar-collapse-grid']/ul/li[3]/a"))).click()

        # Seleccionar Depósitos
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Depósitos')]"))).click()

        # Scroll hacia abajo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.3);")

        # Seleccionar Cuenta de Ahorro Comercial
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cuenta de Ahorro Comercial')]"))).click()

        # Scroll hacia abajo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.2);")

        # Seleccionar la pestaña "Tarifario"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='filialTabs']/li[5]/a"))).click()

        # Hacer clic en el enlace del PDF
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tab5']/table/tbody/tr/td[2]/a/img"))).click()

        # Manejo de la nueva pestaña del navegador
        driver.switch_to.window(driver.window_handles[1])  # Cambiar a la nueva pestaña
        time.sleep(6)

        # Validar el texto dentro del PDF
        self.assertIn("PAL BANCO", driver.title, "El título del PDF no es el esperado")

        time.sleep(6)

    def tearDown(self):
        self.driver.quit()  # Cierra todas las pestañas

if __name__ == '__main__':
    unittest.main()
