import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter.messagebox import showinfo
from datetime import datetime
import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence
import os
import time
import random
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


path = r"C:\Users\billy\OneDrive\Documents\GitHub\Final-Project--Jackson--Sean--David--William-\bodies.webp"


root = tk.Tk()
root.title("Exercise App")
root.attributes("-fullscreen", True)
root.title("Exercise App")
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.quit())


log_file = "exercise_log.csv"
df = pd.read_csv("exerlist.csv")
secondary = tk.Toplevel(root)
secondary.geometry("890x686")
choose_day_frame = tk.Frame(root)
choose_exer_frame = tk.Frame(root)
home_frame = tk.Frame(root)
exer_frame = tk.Frame(root)
tracker_frame = tk.Frame(root)
exframe = ctk.CTkScrollableFrame(secondary, width = 890, height = 686, fg_color = "white")
#learned about this from here https://www.youtube.com/watch?v=Envp9yHb2Ho
#https://github.com/TomSchimansky/CustomTkinter/wiki/CTkScrollableFrame


global c
cc=0
global d
dc=0
global e
ec=0


exframe.pack()
home_frame.pack()
exer_frame.pack()
choose_day_frame.pack()
choose_exer_frame.pack()
tracker_frame.pack()


CheckButtonChest = tk.IntVar()
CheckButtonTriceps = tk.IntVar()
CheckButtonShoulders = tk.IntVar()
CheckButtonBack = tk.IntVar()
CheckButtonBiceps = tk.IntVar()
CheckButtonForearms = tk.IntVar()
CheckButtonAbs = tk.IntVar()
CheckButtonGlutes = tk.IntVar()
CheckButtonQuads = tk.IntVar()
CheckButtonHamstrings = tk.IntVar()
CheckButtonCalves = tk.IntVar()


CheckButton1st = tk.IntVar()
CheckButton2nd = tk.IntVar()
CheckButton3rd = tk.IntVar()
CheckButton4th = tk.IntVar()
CheckButton5th = tk.IntVar()
CheckButton6th = tk.IntVar()
CheckButton7th = tk.IntVar()
CheckButton8th = tk.IntVar()
CheckButton9th = tk.IntVar()
CheckButton10th = tk.IntVar()
CheckButton11th = tk.IntVar()
CheckButton12th = tk.IntVar()
CheckButton13th = tk.IntVar()
CheckButton14th = tk.IntVar()
CheckButton15th = tk.IntVar()
CheckButton16th = tk.IntVar()


global body_parts_list
body_parts_list = []


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
    i = 0
    while i == 0:
        for frame in ImageSequence.Iterator(Image.open(gif_filename)):
            event, values = window.read(timeout=interframe_duration)
            if event == sg.WIN_CLOSED:
                i = 1
            else:
                window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )


def byName(name):
    df_withname = df.loc[df['Name'].str.contains(name.title(), na = False)]
    #https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string
    #used this to find "title"
    secondary = tk.Toplevel(root)
    secondary.geometry("890x686")
    exframe = ctk.CTkScrollableFrame(secondary, width = 890, height = 686, fg_color = "white")
    exframe.pack()
    for i, r in df_withname.iterrows():
        tk.Label(exframe, text = f"name: {r['Name']}\nPrimary Muscles: {r['primary']}\nSecondary Muscles: {r['secondary']}", bg = "white").pack()
        tk.Button(exframe, text = "       GIF       ", command = lambda r=r: show_gif(r["GIF url"])).pack()




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




def home_page():
    title_text = tk.Label(home_frame, text="Exercise Planner", font=("Arial", 12,"bold"))
    title_text.pack(pady=5)




    exercise_button = tk.Button(home_frame, text="Exercise List", font=50, command=go_to_exer)
    exercise_button.pack(pady=5)




    tracker_button = tk.Button(home_frame, text="Past Exercises", font=50, command=go_to_tracker)
    tracker_button.pack(pady=5)


    planner_button = tk.Button(home_frame, text="Workout Planner", font=50, command=go_to_plan)
    planner_button.pack(pady=5)






def go_to_exer():
    home_frame.pack_forget()
    exer_frame.pack(fill="both", expand=True)
    bodies_buttons()
def go_to_tracker():
    global body_parts_list, exercises_list
    body_parts_list = []
    exercises_list = []
    home_frame.pack_forget()
    tracker_frame.pack(fill="both", expand=True)
    tracker_button_function()
def go_to_plan():
    home_frame.pack_forget()
    choose_day_frame.pack(fill="both", expand=True)
    choose_day()


def backft():
    tracker_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)
def backfp():
    choose_day_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)
def backfe():
    exer_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)


#body part functions
def shoulders_fun():
    byMusc("Deltoid")
def biceps_fun():
    byMusc("Bicep")
def triceps_fun():
    byMusc("Tricep")
def forearms_fun():
    byMusc("Forearm")
def chest_fun():
    byMusc("Chest")
def back_fun():
    byMusc("Lat")
def abs_fun():
    byMusc("Abs")
def glutes_fun():
    byMusc("Glute")
def quad_fun():
    byMusc("Quad")
def ham_fun():
    byMusc("Ham")
def calves_fun():
    byMusc("Calve")




def tracker_button_function():
    global exercise_entry, weight_entry, reps_entry, show_past, exercise_label, current_index
    for widget in tracker_frame.winfo_children():
        widget.destroy()

    for widget in tracker_frame.winfo_children():
        widget.destroy()

    def update_exercise_label():
        """Update the exercise label to show the current element of body_parts_list."""
        if current_index < len(exercises_list):
            exercise_label.config(text=exercises_list[current_index])
            global exercise_entry_string
            exercise_entry_string = exercises_list[current_index]
        else:
            exercise_label.config(text="No more exercises!")
            next_button.config(state="disabled")


    def next_exercise():
        """Go to the next exercise in the list."""
        global current_index
        current_index += 1
        update_exercise_label()


    if not body_parts_list:  # If the list is empty
        # Back button
        back_button = tk.Button(tracker_frame, text="Back", command=backft)
        back_button.place(x=0, y=0)


        # Title and labels
        title_text = tk.Label(tracker_frame, text="Past Exercise List", font=("Arial", 12, "bold"))
        title_text.pack(pady=5)


        label1 = tk.Label(tracker_frame, text="Your past exercises:")
        label1.pack(pady=10)


        # Show past button
        show_past_button = tk.Button(tracker_frame, text="Refresh/Show", command=lambda: view_exercises(data))
        show_past_button.pack()


        show_past = scrolledtext.ScrolledText(tracker_frame, width=70, height=20)
        show_past.pack(pady=10)


        label2 = tk.Label(tracker_frame, text="Add today's exercise!")
        label2.pack(pady=10)


        # Exercise input
        exercise_label = tk.Label(tracker_frame, text="Name of exercise")
        exercise_label.pack()
        exercise_entry = tk.Entry(tracker_frame, width=30)
        exercise_entry.pack(pady=5)


        # Weight input
        weight_label = tk.Label(tracker_frame, text="lbs")
        weight_label.pack()
        weight_entry = tk.Entry(tracker_frame, width=30)
        weight_entry.pack(pady=5)


        # Reps input
        reps_label = tk.Label(tracker_frame, text="# of reps")
        reps_label.pack()
        reps_entry = tk.Entry(tracker_frame, width=30)
        reps_entry.pack(pady=5)


        # Buttons
        add_exercise_button = tk.Button(tracker_frame, text="Add exercise!", command=lambda: add_exercise(data))
        add_exercise_button.pack(pady=10)


        view_progress_button = tk.Button(tracker_frame, text="View Progress", command=open_popup_window1)
        view_progress_button.pack(pady=10)
       
    else:  # If the list is not empty
        current_index = 0  # Start with the first element in the list


        # Back button
        back_button = tk.Button(tracker_frame, text="Back", command=backft)
        back_button.place(x=0, y=0)


        # Title and labels
        title_text = tk.Label(tracker_frame, text="Past Exercise List", font=("Arial", 12, "bold"))
        title_text.pack(pady=5)


        label1 = tk.Label(tracker_frame, text="Your past exercises:")
        label1.pack(pady=10)


        # Show past button
        show_past_button = tk.Button(tracker_frame, text="Refresh/Show", command=lambda: view_exercises(data))
        show_past_button.pack()


        show_past = scrolledtext.ScrolledText(tracker_frame, width=70, height=20)
        show_past.pack(pady=10)


        label2 = tk.Label(tracker_frame, text="Add today's exercise!")
        label2.pack(pady=10)


        # Exercise input with dynamic label
        exercise_label = tk.Label(tracker_frame, text="")
        exercise_label.pack()
        update_exercise_label()  # Initialize the label with the first element


        # Next button to iterate through the list
        next_button = tk.Button(tracker_frame, text="Next Exercise", command=next_exercise)
        next_button.pack(pady=5)


        # Weight input
        weight_label = tk.Label(tracker_frame, text="lbs")
        weight_label.pack()
        weight_entry = tk.Entry(tracker_frame, width=30)
        weight_entry.pack(pady=5)


        # Reps input
        reps_label = tk.Label(tracker_frame, text="# of reps")
        reps_label.pack()
        reps_entry = tk.Entry(tracker_frame, width=30)
        reps_entry.pack(pady=5)


        # Buttons
        add_exercise_button = tk.Button(tracker_frame, text="Add exercise!", command=lambda: add_exercise(data))
        add_exercise_button.pack(pady=10)


        view_progress_button = tk.Button(tracker_frame, text="View Progress", command=open_popup_window1)
        view_progress_button.pack(pady=10)
    tk.Label(tracker_frame, text = " ", height = 300).pack()


def bodies_buttons():
    #creates the image of the human bodies
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    global image

    for widget in exer_frame.winfo_children(): #have to destroy and recreate the frame widgets
        widget.destroy() #or else they get all malfunctional and weird https://stackoverflow.com/questions/24228114/how-to-make-widgets-visible-again-when-using-pack-forget-in-tkinter 

    image = ImageTk.PhotoImage(Image.open(path))
    canvas = tk.Canvas(exer_frame, width=width, height=height)
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
    back_button = tk.Button(exer_frame, text="Back", command=backfe)
    back_button.place(x=0, y=0)




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
    searchbar = tk.Entry(exer_frame, textvariable = exername)
    enter = tk.Button(exer_frame, text = "Search", command=lambda: byName(exername.get()))




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
        show_past.insert(tk.END, "No exercise logs found.\n")
        return
   
    show_past.insert(tk.END, "Exercise Log:\n")
    for entry in data:
        show_past.insert(tk.END, f"Date: {entry['date']}, Exercise: {entry['exercise']}, "
              f"Weight: {entry['weight']} lbs, Reps: {entry['reps']}\n")
       
def add_exercise(data):
    if not body_parts_list:
        exercise = exercise_entry.get().lower()
    else:
        exercise = exercise_entry_string
   
    weight = weight_entry.get()
    reps = reps_entry.get()
    date = datetime.now().strftime("%m-%d-%Y %I:%M %p")
   
    data.append({"date": date, "exercise": exercise, "weight": weight, "reps": reps})


    save_data(data)
   
    show_past.insert(tk.END, f"\nRecorded {exercise}: {weight} lbs for {reps} reps on {date}\n")
   
    exercise_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)


def view_progress(selected_exercise, data):
    # Load the data into a DataFrame
    tracker_temp_df = pd.DataFrame(data)


    # Ensure the necessary columns exist
    if "date" not in tracker_temp_df.columns or "weight" not in tracker_temp_df.columns or "exercise" not in tracker_temp_df.columns:
        messagebox.showerror("Error", "The data is missing required columns: 'date', 'weight', or 'exercise'.")
        return


    # Filter the data for the selected exercise
    exercise_data = tracker_temp_df[tracker_temp_df["exercise"] == selected_exercise]


    if exercise_data.empty:
        messagebox.showinfo("No Data", f"No data found for exercise: {selected_exercise}")
        return


    # Convert the 'date' column to datetime
    exercise_data.loc[:,"date"] = pd.to_datetime(exercise_data["date"], errors="coerce")


    # Drop rows with invalid dates
    exercise_data = exercise_data.dropna(subset=["date"])


    # Sort by date for proper plotting
    exercise_data = exercise_data.sort_values(by="date")


    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(exercise_data["date"], exercise_data["weight"], marker="o", linestyle="-", label="Weight (lbs)")
    plt.title(f"Progress for {selected_exercise}")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
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
        global selected_exercise
        selected_exercise = exercise_combobox.get()
        if not selected_exercise:
            messagebox.showwarning("Input Error", "Please select an exercise.")
        else:
            view_progress(selected_exercise, data)


    # Button to generate the graph
    plot_button = tk.Button(popup, text="Plot Exercise Progress", command=on_plot_button_click)
    plot_button.pack(pady=10)
   
def open_popup_window2():
    popup2 = tk.Toplevel()
    popup2.title(f"Progress for {selected_exercise}")
    popup2.geometry("900x600")


    # Embed the Matplotlib figure in the Tkinter popup window
    canvas = FigureCanvasTkAgg(master=popup2)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)






# checkbuttons from https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/
def choose_day():

    global body_parts_list, exercises_list, bodyparts_lbl, chest_btn, triceps_btn, back_btn, shoulders_btn, forearms_btn, biceps_btn, abs_btn, glutes_btn, quads_btn, hamstrings_btn, calves_btn


    for widget in choose_day_frame.winfo_children():
        widget.destroy()

    body_parts_list = []
    exercises_list = []

    back_button = tk.Button(choose_day_frame, text="Back", command=backfp)
    back_button.place(x=0, y=0)


    bodyparts_lbl = tk.Label(choose_day_frame, text="Choose the body parts you want to workout today:").pack()




    chest_btn = tk.Checkbutton(choose_day_frame, text="Chest", onvalue=1, offvalue=0, variable=CheckButtonChest).pack()
    triceps_btn = tk.Checkbutton(choose_day_frame, text="Triceps", onvalue=1, offvalue=0, variable=CheckButtonTriceps).pack()
    shoulders_btn = tk.Checkbutton(choose_day_frame, text="Shoulders", onvalue=1, offvalue=0, variable=CheckButtonShoulders).pack()
    back_btn = tk.Checkbutton(choose_day_frame, text="Back", onvalue=1, offvalue=0, variable=CheckButtonBack).pack()
    biceps_btn = tk.Checkbutton(choose_day_frame, text="Biceps", onvalue=1, offvalue=0, variable=CheckButtonBiceps).pack()
    forearms_btn = tk.Checkbutton(choose_day_frame, text="Forearms", onvalue=1, offvalue=0, variable=CheckButtonForearms).pack()
    abs_btn = tk.Checkbutton(choose_day_frame, text="Abs", onvalue=1, offvalue=0, variable=CheckButtonAbs).pack()
    glutes_btn = tk.Checkbutton(choose_day_frame, text="Glutes", onvalue=1, offvalue=0, variable=CheckButtonGlutes).pack()
    quads_btn = tk.Checkbutton(choose_day_frame, text="Quads", onvalue=1, offvalue=0, variable=CheckButtonQuads).pack()
    hamstrings_btn = tk.Checkbutton(choose_day_frame, text="Hamstrings", onvalue=1, offvalue=0, variable=CheckButtonHamstrings).pack()
    calves_btn = tk.Checkbutton(choose_day_frame, text="Calves", onvalue=1, offvalue=0, variable=CheckButtonCalves).pack()




    save_parts_btn = tk.Button(choose_day_frame, text="Save parts for the day.", command=save_parts).pack()
    tk.Label(choose_day_frame, text = " ", height = 700).pack()


def backer():
    choose_exer_frame.pack_forget()
    choose_day_frame.pack(expand=True, fill="both")




def save_parts():
    if CheckButtonChest.get() == 1:
        body_parts_list.append("Chest")
    if CheckButtonTriceps.get() == 1:
        body_parts_list.append("Triceps")
    if CheckButtonShoulders.get() == 1:
        body_parts_list.append("Front Deltoid")
        body_parts_list.append("Lateral Deltoid")
    if CheckButtonBack.get() == 1:
        body_parts_list.append("Lats")
        body_parts_list.append("Rear Deltoid")
        body_parts_list.append("Lower Back")
    if CheckButtonBiceps.get() == 1:
        body_parts_list.append("Biceps")
    if CheckButtonForearms.get() == 1:
        body_parts_list.append("Forearm")
    if CheckButtonAbs.get() == 1:
        body_parts_list.append("Obliques")
        body_parts_list.append("Abs")
    if CheckButtonGlutes.get() == 1:
        body_parts_list.append("Glutes")
    if CheckButtonQuads.get() == 1:
        body_parts_list.append("Quads")
    if CheckButtonHamstrings.get() == 1:
        body_parts_list.append("Hamstrings")
    if CheckButtonCalves.get() == 1:
        body_parts_list.append("Calves")




    choose_day_frame.pack_forget()
    choose_exer_frame.pack(fill="both", expand=True)
    choose_exercises()




def choose_exercises():
    for widget in choose_exer_frame.winfo_children():
        widget.destroy()
    temp_list11 = []
    temp_list21 = []
    temp_list31 = []
    temp_list41 = []




    global all_exercises_list
    all_exercises_list = []


    back_button = tk.Button(choose_exer_frame, text="Back", command=backer)
    back_button.place(x=0, y=0)


    c=0




    if len(body_parts_list) == 0:
        #showinfo from https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        showinfo("Exercise App", "You didn't enter any exercises. Retry.")
        choose_exer_frame.pack_forget()
        choose_day_frame.pack(expand=True, fill="both")




    elif len(body_parts_list) == 1:
        for row in body_parts_list:
            df_muscle = df.loc[df['primary'].str.contains(row, na = False)]
            for j in df_muscle["Name"]:
                temp_list11.append(j)




            temp_list1 = random.sample(temp_list11, 6)
   
        exercises_lbl = tk.Label(choose_exer_frame, text="Choose 4 of the below exercises.").pack()




        lbl1 = tk.Label(choose_exer_frame, text=row).pack()




        first_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[0], onvalue=1, offvalue=0, variable=CheckButton1st).pack()
        second_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[1], onvalue=1, offvalue=0, variable=CheckButton2nd).pack()
        third_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[2], onvalue=1, offvalue=0, variable=CheckButton3rd).pack()
        fourth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[3], onvalue=1, offvalue=0, variable=CheckButton4th).pack()
        fifth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[4], onvalue=1, offvalue=0, variable=CheckButton5th).pack()
        sixth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[5], onvalue=1, offvalue=0, variable=CheckButton6th).pack()




        all_exercises_list.append((temp_list1[0], CheckButton1st))
        all_exercises_list.append((temp_list1[1], CheckButton2nd))
        all_exercises_list.append((temp_list1[2], CheckButton3rd))
        all_exercises_list.append((temp_list1[3], CheckButton4th))
        all_exercises_list.append((temp_list1[4], CheckButton5th))
        all_exercises_list.append((temp_list1[5], CheckButton6th))












    elif len(body_parts_list) == 2:
        exercises_lbl = tk.Label(choose_exer_frame, text="Choose 3 exercises for each of the below muscles.").pack()        




        for row in body_parts_list:
            c+=1
            df_muscle = df.loc[df['primary'].str.contains(row, na = False)]
           
            if c == 1:
                for j in df_muscle["Name"]:
                    temp_list11.append(j)
               
                temp_list1 = random.sample(temp_list11, 5)




                lbl1 = tk.Label(choose_exer_frame, text=row).pack()




                first_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[0], onvalue=1, offvalue=0, variable=CheckButton1st).pack()
                second_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[1], onvalue=1, offvalue=0, variable=CheckButton2nd).pack()
                third_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[2], onvalue=1, offvalue=0, variable=CheckButton3rd).pack()
                fourth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[3], onvalue=1, offvalue=0, variable=CheckButton4th).pack()
                fifth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[4], onvalue=1, offvalue=0, variable=CheckButton5th).pack()




                all_exercises_list.append((temp_list1[0], CheckButton1st))
                all_exercises_list.append((temp_list1[1], CheckButton2nd))
                all_exercises_list.append((temp_list1[2], CheckButton3rd))
                all_exercises_list.append((temp_list1[3], CheckButton4th))
                all_exercises_list.append((temp_list1[4], CheckButton5th))
           
           
            if c == 2:
                for j in df_muscle["Name"]:
                    temp_list21.append(j)
               
                temp_list2 = random.sample(temp_list21, 5)




                lbl2 = tk.Label(choose_exer_frame, text=row).pack()




                sixth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[0], onvalue=1, offvalue=0, variable=CheckButton6th).pack()
                seventh_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[1], onvalue=1, offvalue=0, variable=CheckButton7th).pack()
                eighth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[2], onvalue=1, offvalue=0, variable=CheckButton8th).pack()
                nineth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[3], onvalue=1, offvalue=0, variable=CheckButton9th).pack()
                tenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[4], onvalue=1, offvalue=0, variable=CheckButton10th).pack()




                all_exercises_list.append((temp_list2[0], CheckButton6th))
                all_exercises_list.append((temp_list2[1], CheckButton7th))
                all_exercises_list.append((temp_list2[2], CheckButton8th))
                all_exercises_list.append((temp_list2[3], CheckButton9th))
                all_exercises_list.append((temp_list2[4], CheckButton10th))




           
    elif len(body_parts_list) == 3:
        exercises_lbl = tk.Label(choose_exer_frame, text="Choose 2 exercises for each of the below muscles.").pack()
        for row in body_parts_list:
            c+=1
            df_muscle = df.loc[df['primary'].str.contains(row, na = False)]
           
            if c == 1:
                for j in df_muscle["Name"]:
                    temp_list11.append(j)
               
                temp_list1 = random.sample(temp_list11, 5)




                lbl1 = tk.Label(choose_exer_frame, text=row).pack()




                first_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[0], onvalue=1, offvalue=0, variable=CheckButton1st).pack()
                second_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[1], onvalue=1, offvalue=0, variable=CheckButton2nd).pack()
                third_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[2], onvalue=1, offvalue=0, variable=CheckButton3rd).pack()
                fourth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[3], onvalue=1, offvalue=0, variable=CheckButton4th).pack()
                fifth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[4], onvalue=1, offvalue=0, variable=CheckButton5th).pack()




                all_exercises_list.append((temp_list1[0], CheckButton1st))
                all_exercises_list.append((temp_list1[1], CheckButton2nd))
                all_exercises_list.append((temp_list1[2], CheckButton3rd))
                all_exercises_list.append((temp_list1[3], CheckButton4th))
                all_exercises_list.append((temp_list1[4], CheckButton5th))




           
            if c == 2:
                for j in df_muscle["Name"]:
                    temp_list21.append(j)
               
                temp_list2 = random.sample(temp_list21, 5)




                lbl2 = tk.Label(choose_exer_frame, text=row).pack()




                sixth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[0], onvalue=1, offvalue=0, variable=CheckButton6th).pack()
                seventh_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[1], onvalue=1, offvalue=0, variable=CheckButton7th).pack()
                eighth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[2], onvalue=1, offvalue=0, variable=CheckButton8th).pack()
                nineth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[3], onvalue=1, offvalue=0, variable=CheckButton9th).pack()
                tenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[4], onvalue=1, offvalue=0, variable=CheckButton10th).pack()




                all_exercises_list.append((temp_list2[0], CheckButton6th))
                all_exercises_list.append((temp_list2[1], CheckButton7th))
                all_exercises_list.append((temp_list2[2], CheckButton8th))
                all_exercises_list.append((temp_list2[3], CheckButton9th))
                all_exercises_list.append((temp_list2[4], CheckButton10th))




           
            if c == 3:
                for j in df_muscle["Name"]:
                    temp_list31.append(j)
               
                temp_list3 = random.sample(temp_list31, 5)




                lbl3 = tk.Label(choose_exer_frame, text=row).pack()




                eleventh_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[0], onvalue=1, offvalue=0, variable=CheckButton11th).pack()
                twelfth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[1], onvalue=1, offvalue=0, variable=CheckButton12th).pack()
                thirteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[2], onvalue=1, offvalue=0, variable=CheckButton13th).pack()
                fourteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[3], onvalue=1, offvalue=0, variable=CheckButton14th).pack()
                fifteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[4], onvalue=1, offvalue=0, variable=CheckButton15th).pack()




                all_exercises_list.append((temp_list3[0], CheckButton11th))
                all_exercises_list.append((temp_list3[1], CheckButton12th))
                all_exercises_list.append((temp_list3[2], CheckButton13th))
                all_exercises_list.append((temp_list3[3], CheckButton14th))
                all_exercises_list.append((temp_list3[4], CheckButton15th))








    elif len(body_parts_list) == 4:
        exercises_lbl = tk.Label(choose_exer_frame, text="Choose 2 exercises for each of the below muscles.").pack()
        for row in body_parts_list:
            c+=1
            df_muscle = df.loc[df['primary'].str.contains(row, na = False)]
           
            if c == 1:
                for j in df_muscle["Name"]:
                    temp_list11.append(j)
               
                temp_list1 = random.sample(temp_list11, 4)




                lbl1 = tk.Label(choose_exer_frame, text=row).pack()




                first_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[0], onvalue=1, offvalue=0, variable=CheckButton1st).pack()
                second_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[1], onvalue=1, offvalue=0, variable=CheckButton2nd).pack()
                third_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[2], onvalue=1, offvalue=0, variable=CheckButton3rd).pack()
                fourth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list1[3], onvalue=1, offvalue=0, variable=CheckButton4th).pack()




                all_exercises_list.append((temp_list1[0], CheckButton1st))
                all_exercises_list.append((temp_list1[1], CheckButton2nd))
                all_exercises_list.append((temp_list1[2], CheckButton3rd))
                all_exercises_list.append((temp_list1[3], CheckButton4th))
           
           
            if c == 2:
                for j in df_muscle["Name"]:
                    temp_list21.append(j)




                temp_list2 = random.sample(temp_list21, 4)




                lbl2 = tk.Label(choose_exer_frame, text=row).pack()




                fifth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[0], onvalue=1, offvalue=0, variable=CheckButton5th).pack()
                sixth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[1], onvalue=1, offvalue=0, variable=CheckButton6th).pack()
                seventh_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[2], onvalue=1, offvalue=0, variable=CheckButton7th).pack()
                eighth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[3], onvalue=1, offvalue=0, variable=CheckButton8th).pack()




                all_exercises_list.append((temp_list2[0], CheckButton5th))
                all_exercises_list.append((temp_list2[1], CheckButton6th))
                all_exercises_list.append((temp_list2[2], CheckButton7th))
                all_exercises_list.append((temp_list2[3], CheckButton8th))








            if c == 3:
                for j in df_muscle["Name"]:
                    temp_list31.append(j)
               
                temp_list3 = random.sample(temp_list31, 4)




                lbl3 = tk.Label(choose_exer_frame, text=row).pack()




                nineth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[0], onvalue=1, offvalue=0, variable=CheckButton9th).pack()
                tenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list2[1], onvalue=1, offvalue=0, variable=CheckButton10th).pack()
                eleventh_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[2], onvalue=1, offvalue=0, variable=CheckButton11th).pack()
                twelfth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list3[3], onvalue=1, offvalue=0, variable=CheckButton12th).pack()




                all_exercises_list.append((temp_list3[0], CheckButton9th))
                all_exercises_list.append((temp_list3[1], CheckButton10th))
                all_exercises_list.append((temp_list3[2], CheckButton11th))
                all_exercises_list.append((temp_list3[3], CheckButton12th))








            if c == 4:
                for j in df_muscle["Name"]:
                    temp_list41.append(j)




                temp_list4 = random.sample(temp_list41, 5)




                lbl4 = tk.Label(choose_exer_frame, text=row).pack()




                thirteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list4[0], onvalue=1, offvalue=0, variable=CheckButton13th).pack()
                fourteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list4[1], onvalue=1, offvalue=0, variable=CheckButton14th).pack()
                fifteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list4[2], onvalue=1, offvalue=0, variable=CheckButton15th).pack()
                sixteenth_btn = tk.Checkbutton(choose_exer_frame, text=temp_list4[3], onvalue=1, offvalue=0, variable=CheckButton16th).pack()




                all_exercises_list.append((temp_list4[0], CheckButton13th))
                all_exercises_list.append((temp_list4[1], CheckButton14th))
                all_exercises_list.append((temp_list4[2], CheckButton15th))
                all_exercises_list.append((temp_list4[3], CheckButton16th))


   
    elif len(body_parts_list) >= 5:
        #showinfo from https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        showinfo("Exercise App", "You entered a lot of different muscle groups. Try focusing your workout by exercising less of them.")
        choose_exer_frame.pack_forget()
        choose_day_frame.pack(expand=True, fill="both")




    exercises_btn = tk.Button(choose_exer_frame, text="Start Workout", command=save_exercises).pack()
    tk.Label(choose_exer_frame, text = " ", height = 700).pack()




        #I used this https://www.geeksforgeeks.org/select-rows-that-contain-specific-text-using-pandas/
        #and this https://stackoverflow.com/questions/66536221/getting-cannot-mask-with-non-boolean-array-containing-na-nan-values-but-the
        #when I was getting errors
        # for i, r in df_muscle.iterrows():
        #     print(f"name: {r['Name']}")#\nPrimary Muscles: {r['primary']}")#\nSecondary Muscles: {r['secondary']}")




def save_exercises():
    choose_exer_frame.pack_forget()
    global exercises_list
    exercises_list = []




    for exercise, var in all_exercises_list:
        if var.get()==1:
            exercises_list.append(exercise)
    tracker_frame.pack()
    tracker_button_function()






data = load_data()




home_page()


root.mainloop()


# print(body_parts_list)
# print(exercises_list)





