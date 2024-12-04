import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
from PIL import ImageTk, Image
import os
import time
import csv
from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import customtkinter as ctk
import urllib
import requests

url = 'https://i0.wp.com/www.strengthlog.com/wp-content/uploads/2020/03/Dumbbell-Chest-Press.gif?resize=600%2C600&ssl=1'
headers = {
    'User-Agent': 'Mozilla/5.0'
}
request = requests.get(url, headers = headers)
if request.status_code == 200:
    with open("fluidimage.gif", 'wb') as f:
        for chunk in request.iter_content(1024):
            f.write(chunk)
'''Trying to use urllib kept not working. I looked online for why this was the case, and couldn't
get an exact answer. But I did hear people saying that I should solve this by not using urllib
and instead using requests directly. They also said to use a Mozilla User-Agent
https://stackoverflow.com/questions/42441211/python-urllib-error-httperror-http-error-404-not-found
I used this to help me generate image from requests:
https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests'''
