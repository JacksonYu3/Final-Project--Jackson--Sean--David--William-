'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.acefitness.org/resources/everyone/exercise-library")

exlist = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "grid-x grid-margin-x grid-margin-y small-up-2 bp600-up-3 medium-up-4"))
    )  '''
from bs4 import BeautifulSoup
import requests
import html5lib
import csv

source = requests.get("https://www.fitsw.com/exercise-list/").text
soup = BeautifulSoup(source, "lxml")

data_file = open("exerlist.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Muscle Group", "Exercise Name", "Equipment", "Animation"])
table_contents = soup.find("tbody")
for i in table_contents.find_all("tr"):
    row = i.find_all("td")
    group = row[0].text
    name = row[1].text
    level = row[2].text
    equipment = row[3].text
    gif = row[5].span.get("data-preview-src")
    csv_writer.writerow([group, name, level, equipment, gif])
data_file.close()