import tkinter as tk
from PIL import ImageTk, Image
import os
import time
from bs4 import BeautifulSoup
import requests
import html5lib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import tracker
import body_images


def go_to_body():
    root1.quit()
    root2 = tk.Tk()
    body_images.bodies_buttons(root2)


def go_to_tracker():
    root1.quit()
    root3 = tk.Tk()
    tracker.tracker_fun(root3)


def home_screen_fun(root):
    title_text = tk.Label(root, text="Exercise Planner", font=("Arial", 12,"bold"))
    title_text.pack(pady=5)


    exercise_button = tk.Button(root, text="Exercise List", font=50, command=go_to_body)
    exercise_button.pack(pady=5)


    tracker_button = tk.Button(root, text="Past Exercises", font=50, command=go_to_tracker)
    tracker_button.pack(pady=5)
   

if __name__ == "__main__":
    root1 = tk.Tk()
    root1.geometry("600x600")
    root1.title("Exercise Planner")
    home_screen_fun(root1)
    root1.mainloop()