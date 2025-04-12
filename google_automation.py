from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Función para obtener datos manualmente
def obtener_datos():
    busqueda_google = input("Ingresa el término de búsqueda para Google: ")
    busqueda_imagenes = input("Ingresa el término de búsqueda para Google Imágenes: ")
    return busqueda_google, busqueda_imagenes

# Llamar a la función para obtener datos del usuario
termino_google, termino_imagenes = obtener_datos()

# Inicializar Chrome con versión específica
chrome_driver_path = ChromeDriverManager(driver_version="135.0.7049.85").install()
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.maximize_window()

resultados = []

# 1. Buscar en Google
try:
    driver.get("https://www.google.com")
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(termino_google)
    search_box.submit()
    time.sleep(3)
    resultados.append(f"Búsqueda en Google con el término '{termino_google}' realizada correctamente.")
except Exception as e:
    resultados.append(f"Error en búsqueda de Google: {e}")

# 2. Buscar por imágenes
try:
    driver.get("https://images.google.com")
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(termino_imagenes)
    search_box.submit()
    time.sleep(3)
    resultados.append(f"Búsqueda por imágenes con el término '{termino_imagenes}' realizada correctamente.")
except Exception as e:
    resultados.append(f"Error en búsqueda de imágenes: {e}")

# 3. Ir a Google Maps
try:
    driver.get("https://www.google.com/maps")
    time.sleep(5)
    resultados.append("Se accedió a Google Maps correctamente.")
except Exception as e:
    resultados.append(f"Error en Maps: {e}")

# 4. “Me siento con suerte”
try:
    driver.get("https://www.google.com")
    time.sleep(2)
    lucky_button = driver.find_element(By.NAME, "btnI")
    lucky_button.click()
    time.sleep(3)
    resultados.append('"Me siento con suerte" funcionó correctamente.')
except Exception as e:
    resultados.append(f"Error con 'Me siento con suerte': {e}")

# 5. Cambiar idioma del interfaz
try:
    driver.get("https://www.google.com/preferences")
    time.sleep(3)
    driver.find_element(By.XPATH, '//div[contains(text(),"Español")]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@class,"form-buttons")]//div[text()="Guardar"]').click()
    time.sleep(2)
    try:
        driver.switch_to.alert.accept()  # Aceptar alerta si aparece
    except:
        pass
    resultados.append("Idioma cambiado a Español correctamente.")
except Exception as e:
    resultados.append(f"Error al cambiar el idioma: {e}")

# Cerrar el navegador
driver.quit()

# Crear el reporte HTML
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Automatización</title>
</head>
<body>
    <h1>Resultados de Pruebas Automatizadas</h1>
    <ul>
"""
for r in resultados:
    html += f"<li>{r}</li>\n"

html += """
    </ul>
</body>
</html>
"""

# Guardar el archivo HTML
with open("reporte_google.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Script finalizado. Reporte generado como 'reporte_google.html'")
