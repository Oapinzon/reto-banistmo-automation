import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from behave import given, when, then

# Configuración del navegador
def iniciar_driver():
    chrome_options = Options()
    return webdriver.Chrome(options=chrome_options)

@given("el usuario abre el sitio web de Banistmo")
def step_open_website(context):
    context.driver = iniciar_driver()
    context.wait = WebDriverWait(context.driver, 10)
    context.driver.get("https://www.banistmo.com/wps/portal/banistmo/empresas")
    context.driver.maximize_window()

@when("acepta las cookies")
def step_accept_cookies(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Entendido')]"))).click()

@when("navega a la sección de \"Cuentas\"")
def step_navigate_to_accounts(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='navbar-collapse-grid']/ul/li[3]/a"))).click()

@when("selecciona \"Depósitos\"")
def step_select_deposits(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Depósitos')]"))).click()

@when("accede a \"Cuenta de Ahorro Comercial\"")
def step_access_savings_account(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.3);")
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cuenta de Ahorro Comercial')]"))).click()

@when("abre la pestaña \"Tarifario\"")
def step_open_tariff_tab(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.2);")
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='filialTabs']/li[5]/a"))).click()

@then("la página debe cargar correctamente")
def step_page_loads_correctly(context):
    assert "banistmo" in context.driver.current_url.lower(), "La página no cargó correctamente"
    context.driver.quit()
