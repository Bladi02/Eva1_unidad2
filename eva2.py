#Codigo de Bladimir Araya
import urllib.parse
import requests
import json
while True:
    orig = input("\nCiudad de origen (S para salir): ")
    if orig.lower() == "s":
        break
    dest = input("\nCiudad de destino (S para salir): ")
    if dest.lower() == "s":
        break       
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "M4r3Tfi6oBaKiqmK0oSi46GanKq0KONh"
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "unit": "k"})

    json_data = requests.get(url).json()

    distan = json_data["route"]["distance"]
    tiempo = json_data["route"]["formattedTime"]
    camino = json_data["route"]["legs"][0]["maneuvers"]
    print("\nEstas son las indicaciones:")
    for i, maniobra in enumerate(camino):
        print(f"{i+1}. {maniobra['narrative']}")
    print(f"\nLa ruta más corta entre {orig} y {dest} es de {distan} kilómetros.")    
    print(f"\nSi se viaja en auto, en {tiempo} se estará en {dest}.")   
print("¡Chaao!")