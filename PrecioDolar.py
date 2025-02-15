import requests
from bs4 import BeautifulSoup
import datetime 

dt = datetime

f_hoy = dt.datetime.now().date()
f_mañana = f_hoy + dt.timedelta(days=1)

while True:
    print("""Hola Bienvenido
1) Precio del dolar hoy
2) Precio del dolar mañana
3) Cerrar""")
    try:
        a = int(input("Ingrese una opción-> "))
        if a == 1:
            r = requests.get('https://dolar.wilkinsonpc.com.co/')
            soup = BeautifulSoup(r.text, 'lxml')

            precios = soup.find_all('span', class_='baja')
            if precios:
                precio_dolar = precios[0].get_text().strip()  
                print(f"Precio del dólar hoy {f_hoy} es de-> ", precio_dolar)
                b = input("Desea continuar? Y/N-> ")
                if b == "Y" or  b == "y":
                    print("Ok \n -----------------")
                elif b == "N" or b == "n":
                    print("Bye...")
                    break
            else:
                 print("No se pudo encontrar el precio del dólar.")
        elif a == 2:
            r = requests.get('https://dolar.wilkinsonpc.com.co/')
            soup = BeautifulSoup(r.text, 'lxml')

            precios = soup.find_all('span', class_='baja')
            if precios:
                precio_dolar = precios[1].get_text().strip()  
                print(f"Precio del dólar mañana {f_mañana} es de -> ", precio_dolar)    
                c = input("Desea continuar? Y/N-> ")
                if c == "Y" or c == "y":
                    print("Ok \n -----------------")
                elif c == "N" or c == "n":
                    print("Bye...")
                    break
            else:
                 print("No se pudo encontrar el precio del dólar.")
        elif a == 3:
            break
        else:
            print("Caracter invalido... \n -------------------")
    except:
        print("-----------------\nIngresa una opción valida\n-----------------")




