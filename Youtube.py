
from selenium import webdriver
import time
import Spotify

def playlist():
    """Al pasarle una lista de reproduccion de youtube, como por ejemplo el mix diario, devuelve una lista con los nombres"""
    options = Options()
    options.add_argument("--headless")
    lista_canciones=[]
    url = input("ingrese la url: ")
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    time.sleep(3)
    try:
        cancion_el = browser.find_elements_by_id("video-title")
    except:
        print("playlist no encontrada")
    for i in range(len(cancion_el)):
        lista_canciones.append(cancion_el[i].get_attribute("title"))
    time.sleep(1)
    browser.close()
    
    lista_canciones_final =[]
    for i in lista_canciones:
        if i.find("(") > 0:
            cancion_partida = i.split("(")[0]
            lista_canciones_final.append(cancion_partida)
        elif i.find("[")>0:
            cancion_partida = i.split("[")[0]
            lista_canciones_final.append(cancion_partida)      
        else:
            lista_canciones_final.append(i)
    return lista_canciones_final
