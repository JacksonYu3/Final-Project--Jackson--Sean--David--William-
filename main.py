import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence
import os
import time
import csv
import matplotlib.pyplot as plt
from tkinter import ttk
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

path = r"C:\Users\billy\OneDrive\Documents\GitHub\Final-Project--Jackson--Sean--David--William-\bodies.webp"

def show_gif(gifurl):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    request = requests.get(gifurl, headers = headers)
    if request.status_code == 200:
        with open("fluidimage.gif", 'wb') as f:
            for chunk in request.iter_content(1024):
                f.write(chunk)
    '''Trying to use urllib kept not working. I looked online for why this was the case, and couldn't
    get an exact answer. But I did hear people saying that I should solve this by not using urllib
    and instead using requests directly. They also said to use a Mozilla User-Agent
    https://stackoverflow.com/questions/42441211/python-urllib-error-httperror-http-error-404-not-found
    I used this to help me generate image from requests:
    https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests

    canvas = tk.Canvas(tertiary)
    tertiary.geometry("890x686")
    image = Image.open("fluidimage.gif")
    photo = ImageTk.PhotoImage(image, master = tertiary)
    canvas.create_image(600,600, anchor = "center", image=photo)
    canvas.image = photo
    canvas.pack()'''
    #This was not working, I had to look online for ways to display a gif in python
    #I found this guide 
    #https://www.blog.pythonlibrary.org/2023/12/05/viewing-an-animated-gif-with-python/
    #this is the source for the following code
    gif_filename = "fluidimage.gif"
    layout = [[sg.Image(key='-IMAGE-')]]
    window = sg.Window('Window', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)
    interframe_duration = Image.open(gif_filename).info['duration']
    while True:
        for frame in ImageSequence.Iterator(Image.open(gif_filename)):
            event, values = window.read(timeout=interframe_duration)
            if event == sg.WIN_CLOSED:
                exit(0)
            window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )

def byName(name):
    df_withname = df.loc[df['Name'].str.contains(name, na = False)]
    secondary = tk.Toplevel(root)
    secondary.geometry("890x686")
    exframe = ctk.CTkScrollableFrame(secondary, width = 890, height = 686, fg_color = "white")
    exframe.pack()
    for i, r in df_withname.iterrows():
        tk.Label(exframe, text = f"name: {r['Name']}\nPrimary Muscles: {r['primary']}\nSecondary Muscles: {r['secondary']}", bg = "white").pack()
        tk.Button(exframe, text = "       GIF       ", command = lambda r=r: show_gif(r["GIF url"])).pack()
    #See the sources for this in the documentation for byMusc function


def byMusc(muscle):
    df_muscle = df.loc[df['primary'].str.contains(muscle, na = False)]
    #I used this https://www.geeksforgeeks.org/select-rows-that-contain-specific-text-using-pandas/
    #and this https://stackoverflow.com/questions/66536221/getting-cannot-mask-with-non-boolean-array-containing-na-nan-values-but-the
    #when I was getting errors
    secondary = tk.Toplevel(root)
    secondary.geometry("890x686")
    exframe = ctk.CTkScrollableFrame(secondary, width = 890, height = 686, fg_color = "white")
    #learned about this from here https://www.youtube.com/watch?v=Envp9yHb2Ho 
    #https://github.com/TomSchimansky/CustomTkinter/wiki/CTkScrollableFrame
    exframe.pack()
    for i, r in df_muscle.iterrows():
        tk.Label(exframe, text = f"name: {r['Name']}\nPrimary Muscles: {r['primary']}\nSecondary Muscles: {r['secondary']}", bg = "white").pack()
        tk.Button(exframe, text = "       GIF       ", command = lambda r=r: show_gif(r["GIF url"])).pack()
    #I used this to figure out an issue where the lambda function would call with the most recent row URL
    #https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments 

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


    tracker_button = tk.Button(home_frame, text="Past Exercises", font=50, command=go_to_tracker)
    tracker_button.pack(pady=5)


def go_to_exer():
    bodies_buttons()

def go_to_tracker():
    tracker_button()
    

#back button function
def quit():
    root.destroy()
    root.mainloop()


#body part functions
def shoulders_fun():
    byMusc("Deltoid")
    #root.quit()
def biceps_fun():
    byMusc("Bicep")
    #root.quit()
def triceps_fun():
    byMusc("Tricep")
    #root.quit()
def forearms_fun():
    byMusc("Forearms")
    #root.quit()
def chest_fun():
    byMusc("Chest")
    #root.quit()
def back_fun():
    byMusc("Lat")
    #root.quit()
def abs_fun():
    byMusc("Abs")
    #root.quit()
def glutes_fun():
    byMusc("Glute")
    #root.quit()
def quad_fun():
    byMusc("Quad")
def ham_fun():
    byMusc("Ham")
    #root.quit()
def calves_fun():
    byMusc("Calve")
    #root.quit()

def tracker_button():
    title_text = tk.Label(root, text="Past Exercise List", font=("Arial", 12,"bold"))
    title_text.pack(pady=5)

    label1 = tk.Label(root, text="Your past exercises: ")
    label1.pack(pady=10)

    show_past_button = tk.Button(root, text="Refresh/Show", command=lambda: view_exercises(data))
    show_past_button.pack()

    show_past = scrolledtext.ScrolledText(root, width=70, height=20)
    show_past.pack(pady=10)

    label2 = tk.Label(root, text="Add today's exercise!")
    label2.pack(pady=10)

    exercise_label = tk.Label(root, text="Name of exercise")
    exercise_label.pack()
    exercise_entry = tk.Entry(root, width=30)
    exercise_entry.pack(pady=5)

    weight_label = tk.Label(root, text="lbs")
    weight_label.pack()
    weight_entry = tk.Entry(root, width=30)
    weight_entry.pack(pady=5)

    reps_label = tk.Label(root, text="# of reps")
    reps_label.pack()
    reps_entry = tk.Entry(root, width=30)
    reps_entry.pack(pady=5)

    add_exercise_button = tk.Button(root, text="Add exercise!", command=lambda: add_exercise(data))
    add_exercise_button.pack(pady=10)

    view_progress_button = tk.Button(root, text="View Progress", command=open_popup_window1)
    view_progress_button.pack(pady=10)

def bodies_buttons():
    #creates the image of the human bodies
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    global image
    image = ImageTk.PhotoImage(Image.open(path))
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
    exit_btn = tk.Button(exer_frame, text="Back", command=quit)
    exit_btn.place(x=50, y=50) #this should not lead to "back function" -- 
    #that function refers to back muscles, not returning to home page.


    #body part buttons
    shoulders_btn = tk.Button(exer_frame, text="Shoulders", command=shoulders_fun)
    biceps_btn = tk.Button(exer_frame, text="Biceps", command=biceps_fun)
    triceps_btn = tk.Button(exer_frame, text="Triceps", command=triceps_fun)
    forearms_btn = tk.Button(exer_frame, text="Forearms", command=forearms_fun)
    chest_btn = tk.Button(exer_frame, text="Chest", command=chest_fun)
    back_btn = tk.Button(exer_frame, text="Back", command=back_fun)
    abs_btn = tk.Button(exer_frame, text="Abs", command=abs_fun)
    glutes_btn = tk.Button(exer_frame, text="Glutes", command=glutes_fun)
    legs_btn1 = tk.Button(exer_frame, text="Hamstrings", command=ham_fun)
    legs_btn2 = tk.Button(exer_frame, text="Quads", command=quad_fun)
    calves_btn = tk.Button(exer_frame, text="Calves", command=calves_fun)
    exername = tk.StringVar() 
    exername.set("")
    searchbar = tk.Entry(root, textvariable = exername)
    enter = tk.Button(root, text = "Search", command=lambda: byName(exername.get()))


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
    searchbar.place(x=150, y = 500, anchor = "e")
    enter.place(x=100, y=550, anchor = "e")

def load_data():
    data = []
    
    with open(log_file, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader) 
    return data

def save_data(data):
    with open(log_file, mode="w", newline='') as file:
        fieldnames = ["date", "exercise", "weight", "reps"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  
        writer.writerows(data) 
        
def view_exercises(data):
    show_past.delete("1.0", tk.END)
    if not data:
        print("No exercise logs found.")
        return
    
    show_past.insert(tk.END, "Exercise Log:\n")
    for entry in data:
        show_past.insert(tk.END, f"Date: {entry['date']}, Exercise: {entry['exercise']}, "
              f"Weight: {entry['weight']} lbs, Reps: {entry['reps']}\n")
        
def add_exercise(data):
    exercise = exercise_entry.get().lower()
    weight = weight_entry.get()
    reps = reps_entry.get()
    date = datetime.now().strftime("%m-%d-%Y %I:%M %p")
    
    data.append({"date": date, "exercise": exercise, "weight": weight, "reps": reps})

    save_data(data)
    
    show_past.insert(tk.END, f"\nRecorded {exercise}: {weight} lbs for {reps} reps on {date}\n") 
    
    exercise_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    
def view_progress(data):
    tracker_temp_df = pd.read_csv(log_file)
    
    # Filter the data for the selected exercise
    exercise_data = data[data["exercise"] == selected_exercise]
    
    if exercise_data.empty:
        messagebox.showinfo("No Data", f"No data found for exercise: {selected_exercise}")
        return

    plt.plot(tracker_temp_df["date"], tracker_temp_df["weight"])
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    
    plt.show()
    
def open_popup_window1():
    popup = tk.Toplevel()
    popup.title("Select Exercise to Plot")
    popup.geometry("400x200")

    # Instruction label
    instruction_label = tk.Label(popup, text="Select an exercise to view its progress:", font=("Arial", 12))
    instruction_label.pack(pady=10)

    # Dropdown menu for exercise selection
    progress_data = load_data()

    # Converts the progress_data into a dataframe for the unique exercise and into a list
    progress_df = pd.DataFrame(progress_data)
    if "exercise" in progress_df.columns:
        unique_exercises = progress_df["exercise"].unique().tolist()
    else:
        unique_exercises = []

    exercise_combobox = ttk.Combobox(popup, values=unique_exercises, state="readonly", width=30)
    exercise_combobox.pack(pady=5)

    def on_plot_button_click():
        selected_exercise = exercise_combobox.get()
        if not selected_exercise:
            messagebox.showwarning("Input Error", "Please select an exercise.")
        else:
            plot_selected_exercise(selected_exercise)

    # Button to generate the graph
    plot_button = tk.Button(popup, text="Plot Exercise Progress", command=on_plot_button_click)
    plot_button.pack(pady=10)
    
def open_popup_window2():
    popup2 = tk.Toplevel()
    popup2.title(f"Progress for {selected_exercise}")
    popup2.geometry("900x600")

    # Embed the Matplotlib figure in the Tkinter popup window
    canvas = FigureCanvasTkAgg(fig, master=popup2)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    
data = load_data()


home_page()






root.mainloop()
