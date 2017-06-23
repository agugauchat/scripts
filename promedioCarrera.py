# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys

rates = [str(x) for x in range(11)]
total = 0
subjects = 0

# Se crea una instancia de Selenium
driver = webdriver.Firefox()
driver.get('http://campus.ucse.edu.ar/ACwebLogin.aspx')

'''Buscamos los imputs del formulario de registracion
Se completan los campos con los datos del usuario
Renombrar estos tres campos con los datos personales 
'''
driver.find_element_by_name("txtnroDoc").send_keys('DOCUMENTO')
driver.find_element_by_name("txtUsuario").send_keys('USUARIO')
driver.find_element_by_name("txtclave").send_keys('PASSWORD')

# Buscamos el boton ingreso y le damos la orden de clickear
driver.find_element_by_id("btnAceptar").click()
main_window = driver.current_window_handle

# Selecciona en la parte de Ingenieria o Analista (Ingenieria)
tr = driver.find_elements_by_tag_name("tr")
for i in tr:
    if i.get_attribute('onclick') == "javascript:__doPostBack('Grid','Select$0')":
        i.send_keys(Keys.CONTROL + "t")			
        i.click()
driver.get('http://campus.ucse.edu.ar/ACwebPrincipal.aspx')

# Seleccionamos el menu consultas
a = driver.find_elements_by_tag_name("div")	
for i in a:
    if i.get_attribute('innerHTML')== '<a href="#1">&nbsp;Consultas </a>':
        i.click()

# Seleccionamos ficha academica
a = driver.find_elements_by_tag_name("a")	
for i in a:
    if "Ficha" in i.get_attribute('innerHTML'):
        i.send_keys(Keys.CONTROL + "t")
        i.click()

# Abrimos la ventana de calificaciones
driver.get('http://campus.ucse.edu.ar/ACwebConsultaFichaAcademica.aspx')

# Buscamos cada nota
td = driver.find_elements_by_tag_name("td")
for i in td:
    if i.get_attribute("align") == "center":
        if i.text != "Historial" and i.text in rates:
            subjects += 1
            total += int(i.text)
# Imprimimos el promedio
driver.close()
print "El promedio calculado de tu carrera es : ", '%.2f' % round(total/float(subjects), 2)   
