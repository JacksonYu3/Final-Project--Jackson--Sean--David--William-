# TRACKER PAGE 
import tkinter as tk
import csv
from datetime import datetime
from tkinter import messagebox, scrolledtext
from datetime import datetime

log_file = "exercise_log.csv"

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
    exercise = exercise_entry.get()
    weight = weight_entry.get()
    reps = reps_entry.get()
    date = datetime.now().strftime("%m-%d-%Y %I:%M %p")
    
    data.append({"date": date, "exercise": exercise, "weight": weight, "reps": reps})

    save_data(data)
    
    show_past.insert(tk.END, f"\nRecorded {exercise}: {weight} lbs for {reps} reps on {date}\n") 
    
    exercise_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    
data = load_data()

root = tk.Tk()
root.geometry("600x750")
root.title("Past Exercise List")

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

root.mainloop()
