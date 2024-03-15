# LIBRARIES
from bs4 import BeautifulSoup
import pandas as pd
import os
from colorama import Fore
import requests

# SELENIUM LIBRARIES
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

# EXPORT TO EXCEL
def ToExcel():

    soup = BeautifulSoup(html_data, 'html.parser')

    rows = soup.find_all('tr', class_='Hover LastRecordLine')

    # LISTS TO DATA
    paises = []
    nombres = []
    categorias = []
    tiempos = []

    # PROCESS FOR EACH ROW & OBTAING REQUIRED DATA
    for row in rows:
        img_tag = row.find('img')
        if img_tag:
            pais = img_tag['src'].split('/')[-1].split('.')[0].upper()
        else:
            pais = "N/A"

        nombre = row.find('td', style='text-align: left;').find_next('td').find_next('td').text.strip()
        categoria = row.find('td', style='text-align: left;').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
        tiempo = row.find_all('td', style='text-align: left;')[-1].text.strip()

        # ADD DATA TO LISTS
        paises.append(pais)
        nombres.append(nombre)
        categorias.append(categoria)
        tiempos.append(tiempo)

    # CREATE DF FOR DATA
    data = pd.DataFrame({
        'Pais': paises,
        'Nombre': nombres,
        'Categoria': categorias,
        'Tiempo': tiempos
    })

    # FILTER BY COUNTRY == 'ES'
    data_es = data[data['Pais'] == 'ES']

    # SAVE ALL DATA IN EXCEL FILE
    data_es.to_excel('resultados_DEKA.xlsx', index=False)


# TELEGRAM INFORMATION
token = "XXXXXXXX:XXXXXXXXXXXXXXXXXX"
chat_id = "-XXXXXXXXXXX"

# CHROME INFORMATION
web = "https://es.deka.fit/race-results/?eventid=266769"

############################
####    WEB SCRAPING    ####
############################

# service = Service(executable_path=path)

# NAVIGATION OPTIONS
options = ChromeOptions()
options.add_argument("--headless")  # BACKGROUND
driver = webdriver.Chrome(options=options) # NO PATH, IT'S INNECESSARY IN MY COMPUTER

driver.get(web)

# GIVE TIME TO LOAD THE PAGE CORRECTLY
time.sleep(10)

competition = input("Selecciona la competición (FIT/MILE/STRONG): ").strip().lower()

while competition not in ("fit", "mile", "strong"):
    print("Please, select 'FIT', 'MILE' o 'STRONG'.")
    competition = input("Select competition (FIT/MILE/STRONG): ").strip().lower()

# PATHS
DEKA_STRONG_PATH = "/html/body/div[1]/div[3]/div[1]/div/main/div/article/section/div/div[2]/div[1]/div[2]/select/option[2]"
DEKA_MILE_PATH = "/html/body/div[1]/div[3]/div[1]/div/main/div/article/section/div/div[2]/div[1]/div[2]/select/option[3]"
DEKA_FIT_PATH = "/html/body/div[1]/div[3]/div[1]/div/main/div/article/section/div/div[2]/div[1]/div[2]/select/option[4]"

if competition == "fit":
    select_competition = driver.find_element(By.XPATH, DEKA_FIT_PATH)
    comp = "DEKA FIT"

elif competition == "mile":
    select_competition = driver.find_element(By.XPATH, DEKA_MILE_PATH)
    comp = "DEKA MILE"

else:
    select_competition = driver.find_element(By.XPATH, DEKA_STRONG_PATH)
    comp = "DEKA STRONG"

# SELECTING COMPETITION (FIT/MILE/STRONG)
select_competition.click()

time.sleep(1)

# SHOWING ALL PARTICIPANTS (BUTTON)
Show_all_participants = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div/article/section/div/div[4]/table/tbody[5]/tr/td/a[2]")
Show_all_participants.click()

time.sleep(2)

# EXTRACT HTML ELEMENTO TO ANALYSE IT
html_data = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div/article/section/div/div[4]/table/tbody[4]")
html_data = html_data.get_attribute('outerHTML')

driver.close()

# PRINT IN SCREEN
# NAME
my_name = input("Introduce el nombre registrado en DEKA: ")

# GENDER
gender = input("¿Vas a querer toda la clasificación, solo hombres o solo mujeres? (toda/hombres/mujeres): ").strip().lower()

while gender not in ("toda", "hombres", "mujeres"):
    print("Por favor, escribe 'toda', 'hombres' o 'mujeres'.")
    gender = input("¿Vas a querer toda la clasificación, solo hombres o solo mujeres? (toda/hombres/mujeres): ").strip().lower()

if gender == "hombres":
    my_gender = "M"
elif gender == "mujeres":
    my_gender = "F"
else:
    my_gender = "O"

# EXCEL
my_excel = input("¿Vas a querer también la información en un excel? (sí/no): \n").strip().lower()

while my_excel not in ("sí", "si", "no"):
    print("Por favor, escribe 'sí' o 'no'.")
    my_excel = input("¿Vas a querer también la información en un excel? (sí/no): \n").strip().lower()

# CLEANING
os.system('cls')

soup = BeautifulSoup(html_data, 'html.parser')

rows = soup.find_all('tr', class_ ='Hover LastRecordLine')

count = 1

print("\n  =======================")
print("|| CLASIFICACIÓN - DEKA ||")
print("  ======================\n")

# PROCESS FOR EACH ROW & OBTAING REQUIRED DATA
for row in rows:
    img_tag = row.find('img')
    if img_tag:
        pais = img_tag['src'].split('/')[-1].split('.')[0].upper()
    else:
        pais = "N/A"  # Or any other default value you want to assign when there is no 'img' tag

    nombre = row.find('td', style ='text-align: left;').find_next('td').find_next('td').text.strip()
    categoria = row.find('td', style ='text-align: left;').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    tiempo = row.find_all('td', style ='text-align: left;')[-1].text.strip()

    # CREATE THE OUT CHAIN FOR EACH FILE AND SHOW IT
    output = f"{pais} - {nombre} - {categoria}. Tiempo: {tiempo}"

    if pais == "ES":
        if my_gender in categoria:

            if nombre == my_name: # SEARCH MY NAME AND SAVE IT TO SHOW IT LATER
                my_position = count
                my_time = tiempo
                print(f"{Fore.RED}{count}. {output}")

            else:
                print(f"{Fore.RESET}{count}. {output}")

            count += 1

if my_excel in ("sí", "si"):
    ToExcel()

try:
    percent_position = (1 - (my_position / count)) * 100
    print(f"\nPosición {my_position}/{count - 1} | Tiempo: {my_time}")
    print(f"\nPor delante del {percent_position:.2f}% de todos los participantes")

    requests.post("https://api.telegram.org/bot" + token +"/sendMessage", data={"chat_id": chat_id, "text": "\n" + comp})
    requests.post("https://api.telegram.org/bot" + token +"/sendMessage", data={"chat_id": chat_id, "text": f"\n\nPosición {my_position}/{count - 1} | Tiempo: {my_time}"})
    requests.post("https://api.telegram.org/bot" + token +"/sendMessage", data={"chat_id": chat_id, "text": f"\nPor delante del {percent_position:.2f}% de todos los participantes"})

except:
    print("\nNo se encontró tu nombre en la clasificación. Vuelve a revisar tu nombre e inténtalo de nuevo")