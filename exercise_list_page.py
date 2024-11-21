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
import home_screen


# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


if __name__ == "__main__":
    root2 = tk.Tk()
    root2.title("Exercise App")
    root2.attributes("-fullscreen", True)


    #makes you able to switch between fullscreen and not by f11 and esc
    root2.bind("<F11>", lambda event: root2.attributes("-fullscreen", not root2.attributes("-fullscreen")))
    root2.bind("<Escape>", lambda event: root2.attributes("-fullscreen", False))






#back button function
def back_fun():
    root2.quit()
    root1 = tk.Tk()
    home_screen.home_screen_fun(root1)




#body part functions
def shoulders_fun():
    print("shoulders")
    root2.quit()
def biceps_fun():
    print("biceps")
    root2.quit()
def triceps_fun():
    print("triceps")
    root2.quit()
def forearms_fun():
    print("forearms")
    root2.quit()
def chest_fun():
    print("chest")
    root2.quit()
def back_fun():
    print("back")
    root2.quit()
def abs_fun():
    print("abs")
    root2.quit()
def glutes_fun():
    print("glutes")
    root2.quit()
def legs_fun():
    print("legs")
    root2.quit()
def calves_fun():
    print("calves")
    root2.quit()




def bodies_buttons(root):
    #creates the image of the human bodies
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    global image
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\Dan\\Documents\\GitHub\\Exercise Project\\Images\\bodies.webp"))
    canvas = tk.Canvas(root)
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
    back_btn = tk.Button(root, text="Back", command=back_fun)
    back_btn.place(x=50, y=50)


    #body part buttons
    shoulders_btn = tk.Button(root, text="Shoulders", command=shoulders_fun)
    biceps_btn = tk.Button(root, text="Biceps", command=biceps_fun)
    triceps_btn = tk.Button(root, text="Triceps", command=triceps_fun)
    forearms_btn = tk.Button(root, text="Forearms", command=forearms_fun)
    chest_btn = tk.Button(root, text="Chest", command=chest_fun)
    back_btn = tk.Button(root, text="Back", command=back_fun)
    abs_btn = tk.Button(root, text="Abs", command=abs_fun)
    glutes_btn = tk.Button(root, text="Glutes", command=glutes_fun)
    legs_btn1 = tk.Button(root, text="Legs", command=legs_fun)
    legs_btn2 = tk.Button(root, text="Legs", command=legs_fun)
    calves_btn = tk.Button(root, text="Calves", command=calves_fun)


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








if __name__ == "__main__":
    bodies_buttons()
    # driver.quit()
    root2.mainloop()


