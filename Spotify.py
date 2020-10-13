from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import getpass
import Youtube

def ingresar ():
    """ingresa a spotify con una cuenta de facebook. La funcion solamente funciona con cuenta de facebook, en caso de querer
    usar otra cuenta modificar desde btb-facebook en adelante"""
    global browser
    browser = webdriver.Chrome()
    print("ingreso a cuenta spotify a travez de Facebook")
    mail = input("ingrese Email : ")
    password = getpass.getpass('contraseña : ') 
    browser.get("https://accounts.spotify.com/es-ES/login")
    time.sleep(1)
    browser.find_element_by_class_name("btn-facebook").click()
    time.sleep(1)
    browser.find_element_by_id("email").send_keys(mail)
    time.sleep(1)
    browser.find_element_by_id("pass").send_keys(password)
    time.sleep(1)
    browser.find_element_by_id("loginbutton").click()
    time.sleep(4)
    if browser.current_url != "https://accounts.spotify.com/es-ES/status":
        print("error al ingresar, revisar mail o contraseña")
    else:
        print("ingreso a spotify todo OK")
    return
     
def crear_lista(nombre_lista):
    """Crea una nueva lista de reproduccion con el nombre proporcionado, se puede tener duplicados"""
    browser.get("https://open.spotify.com/")
    time.sleep(2)
    browser.find_element_by_xpath("//span[contains(text(),'Crear playlist')]").find_element_by_xpath("./..").click()
    time.sleep(1)
    browser.find_element_by_class_name("inputBox-input").send_keys(nombre_lista)
    browser.find_element_by_xpath("//button[contains(text(),'CREAR')]").click()
    return print(f"lista creada{nombre_lista}")
       
def buscar(cancion):
    url_base = "https://open.spotify.com/search/"
    url_cancion = cancion.replace(" ", "%20")
    url_endpoint = url_base+url_cancion
    browser.get(url_endpoint)
    return
     
def agregar(nombre_lista):
    """agrega una cancion a la lista dada. Asume que el buscador se encuentra en la pagina con la correspondiente cancion (ver buscar)"""
        cancion_el = browser.find_elements_by_xpath("//div[@class='contentSpacing']//a")
        #ActionChains me va a servir para hacer un click derecho
        actionChains = ActionChains(browser)
        actionChains.context_click(cancion_el[0]).perform()
        time.sleep(1)
        playlist_el = browser.find_elements_by_xpath("//nav[@role='menu']//div[contains(text(),'Añadir a playlist')]")
        #me aseguro que se muestre el menu y que el nombre proporcionado exista
        for i in playlist_el:
            if i.is_displayed():
                i.click()
                time.sleep(1)
                try:
                    x_path = f'//div[@class = "mo-info-name"]//span[contains(text(),"{nombre_lista}")]'
                    playlist = browser.find_elements_by_xpath(x_path)
                    playlist[0].find_element_by_xpath("./../../../..").click()
                    return print(f"cancion agregada exitosamente en la lista {nombre_lista}")
                except:
                    return print("lista no existe")
      
def buscar_agregar(lista_canciones,nombre_lista):
    for i in lista_canciones:
        print("buscando la cancion: "+ i)
        buscar (i)
        time.sleep(3.5)
        try:
            agregar(nombre_lista)
            time.sleep(1)
        except:
            print(f"la cancion: {i} no pudo ser agragada porque no se encotro o el programador la cago")
    return print("---------------------------------bulce finalizado---------------------------------")
             
def crear_buscar_agragar(nombre_lista,lista_canciones):
    crear_lista(nombre_lista)
    time.sleep(2)
    buscar_agregar(lista_canciones,nombre_lista)
    return print(f"lista {nombre_lista} creada y canciones agregadas")
     
def ingresa_crear_buscar_agregar(nombre_lista,lista_canciones):
    ingresar()
    time.sleep(2)
    crear_buscar_agragar(nombre_lista,lista_canciones)
    time.sleep(2)
    browser.close()        

def ingresa_crear_buscar_agregar_playlist(nombre_lista):
    lista_canciones = Youtube.playlist()
    time.sleep(2)
    ingresa_crear_buscar_agregar(nombre_lista=nombre_lista,lista_canciones=lista_canciones)
    return
    




