import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import Loginy #plik z haslami

def Open_Usos(link = None, Title_erro = 'Wymagane zalogowanie - USOSWEB PW'):
    chrome_options = Options()
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    if link == None:
        link = "https://usosweb.usos.pw.edu.pl/kontroler.php?_action=home/index"
    driver.get(link)
    title = driver.title
    if title == Title_erro:
        return driver
    else:
        raise ValueError("Zla strona podana")


def Open_usos_to_login():
    driver = Open_Usos('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=logowaniecas/index', Title_erro='Logowanie')
    return driver


def Login_to_Usos(driver, Login, Haslo):
    login = '//*[@id="username"]'
    haslo = '//*[@id="password"]'
    WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.XPATH, login)))
    login_ele = driver.find_element(By.XPATH, login)
    haslo_ele = driver.find_element(By.XPATH, haslo)
    login_ele.send_keys(Login)
    haslo_ele.send_keys(Haslo)
    x = driver.find_element(By.XPATH, '//*[@id="fm1"]/div[3]/div[1]/button').click()
    return driver

def is_analiza_updated(driver):
    analiza = '//*[@id="layout-c22"]/div/div/div[2]/usos-frame[1]/div/ul/li[1]/div/a'
    WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.XPATH, analiza)))
    driver.find_element(By.XPATH, analiza).click()
    WebDriverWait(driver, 180).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="childrenof236137"]/table[7]/tbody/tr/td[2]')))
    zad1 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[1]/tbody/tr/td[3]/b')
    zad2 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[2]/tbody/tr/td[3]/b')
    try:
        zad3 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[3]/tbody/tr/td[3]/b')
        zad4 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[4]/tbody/tr/td[3]/b')
    except:
        zad3 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[3]/tbody/tr/td[3]/span')
        zad4 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[4]/tbody/tr/td[3]/span')
    zad5 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[5]/tbody/tr/td[3]/b')
    zad6 = driver.find_element(By.XPATH, '//*[@id="childrenof236155"]/table[6]/tbody/tr/td[3]/b')
    return zad1.text, zad2.text, zad3.text, zad4.text, zad5.text, zad6.text

def wyniki_zmatmy():
    Login = Loginy.Login
    Halso = Loginy.Halso
    Driver = Open_usos_to_login()
    Driver = Login_to_Usos(Driver, Login, Halso)
    a1,a2,a3,a4,a5,a6 = is_analiza_updated(Driver)
    wyniki = [a1,a2,a3,a4,a5,a6]
    return wyniki

def calosc_w_loopie():
    print('start')
    wyniki = wyniki_zmatmy()
    while True:
        print(wyniki)
        time.sleep(360)
        wyniki_2 = wyniki_zmatmy()
        for x in range(len(wyniki_2)):
            if wyniki[x] != wyniki_2[x]:
                pyautogui.alert("Masz wyniki")
        print(wyniki_2)
if __name__=="__main__":
    calosc_w_loopie()