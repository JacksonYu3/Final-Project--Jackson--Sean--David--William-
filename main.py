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


root = tk.Tk()
root.title("Exercise App")
root.attributes("-fullscreen", True)
root.title("Exercise App")
#makes you able to switch between fullscreen and not by f11 and esc
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
home_frame = tk.Frame(root).pack()
exer_frame = tk.Frame(root).pack()


log_file = "exercise_log.csv"
df = pd.read_csv("exerlist.csv")


def home_page():
    title_text = tk.Label(home_frame, text="Exercise Planner", font=("Arial", 12,"bold"))
    title_text.pack(pady=5)


    exercise_button = tk.Button(home_frame, text="Exercise List", font=50, command=go_to_exer)
    exercise_button.pack(pady=5)


    tracker_button = tk.Button(home_frame, text="Past Exercises", font=50)
    tracker_button.pack(pady=5)


def go_to_exer():
    home_frame.destroy()
    bodies_buttons()


#back button function
def back_fun():
    root.quit()
    root = tk.Tk()


#body part functions
def shoulders_fun():
    print("shoulders")
    root.quit()
def biceps_fun():
    print("biceps")
    root.quit()
def triceps_fun():
    print("triceps")
    root.quit()
def forearms_fun():
    print("forearms")
    root.quit()
def chest_fun():
    print("chest")
    root.quit()
def back_fun():
    print("back")
    root.quit()
def abs_fun():
    print("abs")
    root.quit()
def glutes_fun():
    print("glutes")
    root.quit()
def legs_fun():
    print("legs")
    root.quit()
def calves_fun():
    print("calves")
    root.quit()


def bodies_buttons():
    #creates the image of the human bodies
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    global image
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\Dan\\Documents\\GitHub\\Exercise Project\\Images\\bodies.webp"))
    canvas = tk.Canvas(exer_frame)
    canvas.create_image(width / 2, height / 2, image=image, anchor="center")


    #lines connecting buttons to body image
    canvas.create_line(9*width/32, 175, 530, 195, width=3)
    canvas.create_line(9*width/32, 275, 530, 275, width=3)
    canvas.create_line(9*width/32, 375, 520, 375, width=3)
    canvas.create_line(9*width/32, 225, 530, 225, width=3)
    canvas.create_line(9*width/32, 325, 600, 325, width=3)
    canvas.create_line(9*width/32, 500, 570, 500, width=3)
    canvas.create_line(7*width/10, 235, 985, 245, width=3)
    canvas.create_line(7*width/10, 285, 900, 285, width=3)
    canvas.create_line(7*width/10, 400, 940, 400, width=3)
    canvas.create_line(7*width/10, 500, 940, 500, width=3)
    canvas.create_line(7*width/10, 650, 940, 650, width=3)


    canvas.pack(fill="both", expand=True)


    #back button
    back_btn = tk.Button(exer_frame, text="Back", command=back_fun)
    back_btn.place(x=50, y=50)


    #body part buttons
    shoulders_btn = tk.Button(exer_frame, text="Shoulders", command=shoulders_fun)
    biceps_btn = tk.Button(exer_frame, text="Biceps", command=biceps_fun)
    triceps_btn = tk.Button(exer_frame, text="Triceps", command=triceps_fun)
    forearms_btn = tk.Button(exer_frame, text="Forearms", command=forearms_fun)
    chest_btn = tk.Button(exer_frame, text="Chest", command=chest_fun)
    back_btn = tk.Button(exer_frame, text="Back", command=back_fun)
    abs_btn = tk.Button(exer_frame, text="Abs", command=abs_fun)
    glutes_btn = tk.Button(exer_frame, text="Glutes", command=glutes_fun)
    legs_btn1 = tk.Button(exer_frame, text="Legs", command=legs_fun)
    legs_btn2 = tk.Button(exer_frame, text="Legs", command=legs_fun)
    calves_btn = tk.Button(exer_frame, text="Calves", command=calves_fun)


    #body part button placements
    shoulders_btn.place(x=9*width/32, y=175, anchor="e")
    biceps_btn.place(x=9*width/32, y=275, anchor="e")
    triceps_btn.place(x=7*width/10, y=235, anchor="w")
    forearms_btn.place(x=9*width/32, y=375, anchor="e")
    chest_btn.place(x=9*width/32, y=225, anchor="e")
    back_btn.place(x=7*width/10, y=285, anchor="w")
    abs_btn.place(x=9*width/32, y=325, anchor="e")
    glutes_btn.place(x=7*width/10, y=400, anchor="w")
    legs_btn1.place(x=9*width/32, y=500, anchor="e")
    legs_btn2.place(x=7*width/10, y=500, anchor="w")
    calves_btn.place(x=7*width/10, y=650, anchor="w")


def byName(name):
    df_withname = df.loc[df['Name'] == name]
    for i, r in df_withname.iterrows():
        print(f"name: {r['Name']}\nPrimary Muscles: {r['primary']}\nSecondary Muscles: {r['secondary']}")
        #Can't display gifs yet so won't bother printing gif URL


def byMusc(muscle):
    df_muscle = df.loc[df['primary'].str.contains(muscle, na = False)]
    #I used this https://www.geeksforgeeks.org/select-rows-that-contain-specific-text-using-pandas/
    #and this https://stackoverflow.com/questions/66536221/getting-cannot-mask-with-non-boolean-array-containing-na-nan-values-but-the
    #when I was getting errors
    for i, r in df_muscle.iterrows():
        print(f"name: {r['Name']}\nPrimary Muscles: {r['primary']}\nSecondary Muscles: {r['secondary']}")




home_page()






root.mainloop()
