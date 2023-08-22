# Section 1 - get xls url 
import requests
from bs4 import BeautifulSoup

def getExcel():
    URL = "https://www.copsi.ro/index.php/registre"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    el = soup.find("a", string="Descărcați fișierul...")
    link_url = el["href"]

    print("link_url:", link_url)
    # should print '/images/RUP_Partea_I_-_Atestate_de_liberă_practică-05.07.2023.xlsx'

    prefix = "https://www.copsi.ro/"
    fillUrl = prefix + link_url
    print("fillUrl:", fillUrl)
    #should print: https://www.copsi.ro/images/RUP_Partea_I_-_Atestate_de_liberă_practică-05.07.2023.xlsx

    # Section 2 - get excel by url and save html file 
    excelFile = requests.get(fillUrl)
    open('downloadedRUP.xlsx', 'wb').write(excelFile.content)

getExcel()