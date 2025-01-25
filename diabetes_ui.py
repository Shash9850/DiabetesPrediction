import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the model (make sure the model is in the correct location)
model_path = 'E:\\MLProjects\\DiabetesPrediction\\diabetes_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the function to predict
def predict_diabetes():
    inputs = validate_inputs()
    if inputs:
        show_loading()
        result = model.predict([inputs])
        hide_loading()
        if result == 0:
            result_label.config(text="Result: Non-Diabetic", fg="green")
        else:
            result_label.config(text="Result: Diabetic", fg="red")

# Validate user inputs
def validate_inputs():
    try:
        pregnancies = int(pregnancies_entry.get())
        glucose = int(glucose_entry.get())
        blood_pressure = int(bloodpressure_entry.get())
        skin_thickness = int(skinthickness_entry.get())
        insulin = int(insulin_entry.get())
        bmi = float(bmi_entry.get())
        diabetes_pedigree_function = float(diabetespedigreefunction_entry.get())
        age = int(age_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
        return None
    return [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

# Show a loading indicator
def show_loading():
    loading_label = tk.Label(root, text="Predicting...", fg="green", font=("Helvetica", 12, "italic"))
    loading_label.grid(row=10, column=0, columnspan=2)
    root.update()

# Hide loading indicator
def hide_loading():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == "Predicting...":
            widget.destroy()

# Clear form fields
def clear_fields():
    pregnancies_entry.delete(0, tk.END)
    glucose_entry.delete(0, tk.END)
    bloodpressure_entry.delete(0, tk.END)
    skinthickness_entry.delete(0, tk.END)
    insulin_entry.delete(0, tk.END)
    bmi_entry.delete(0, tk.END)
    diabetespedigreefunction_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Diabetes Prediction")
root.geometry("450x500")
root.configure(bg="#f0f8ff")  # Soft light blue color

# Add padding for all elements
padx = 15
pady = 10

# Create the labels and input fields with updated styling
pregnancies_label = tk.Label(root, text="Pregnancies", bg="#f0f8ff", font=("Helvetica", 12))
pregnancies_label.grid(row=0, column=0, padx=padx, pady=pady, sticky="e")
pregnancies_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
pregnancies_entry.grid(row=0, column=1, padx=padx, pady=pady)

glucose_label = tk.Label(root, text="Glucose", bg="#f0f8ff", font=("Helvetica", 12))
glucose_label.grid(row=1, column=0, padx=padx, pady=pady, sticky="e")
glucose_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
glucose_entry.grid(row=1, column=1, padx=padx, pady=pady)

bloodpressure_label = tk.Label(root, text="Blood Pressure", bg="#f0f8ff", font=("Helvetica", 12))
bloodpressure_label.grid(row=2, column=0, padx=padx, pady=pady, sticky="e")
bloodpressure_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
bloodpressure_entry.grid(row=2, column=1, padx=padx, pady=pady)

skinthickness_label = tk.Label(root, text="Skin Thickness", bg="#f0f8ff", font=("Helvetica", 12))
skinthickness_label.grid(row=3, column=0, padx=padx, pady=pady, sticky="e")
skinthickness_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
skinthickness_entry.grid(row=3, column=1, padx=padx, pady=pady)

insulin_label = tk.Label(root, text="Insulin", bg="#f0f8ff", font=("Helvetica", 12))
insulin_label.grid(row=4, column=0, padx=padx, pady=pady, sticky="e")
insulin_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
insulin_entry.grid(row=4, column=1, padx=padx, pady=pady)

bmi_label = tk.Label(root, text="BMI", bg="#f0f8ff", font=("Helvetica", 12))
bmi_label.grid(row=5, column=0, padx=padx, pady=pady, sticky="e")
bmi_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
bmi_entry.grid(row=5, column=1, padx=padx, pady=pady)

diabetespedigreefunction_label = tk.Label(root, text="Diabetes Pedigree Function", bg="#f0f8ff", font=("Helvetica", 12))
diabetespedigreefunction_label.grid(row=6, column=0, padx=padx, pady=pady, sticky="e")
diabetespedigreefunction_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
diabetespedigreefunction_entry.grid(row=6, column=1, padx=padx, pady=pady)

age_label = tk.Label(root, text="Age", bg="#f0f8ff", font=("Helvetica", 12))
age_label.grid(row=7, column=0, padx=padx, pady=pady, sticky="e")
age_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=20)
age_entry.grid(row=7, column=1, padx=padx, pady=pady)

# Create the predict and clear buttons with styling
submit_button = tk.Button(root, text="Predict", command=predict_diabetes, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=20, pady=10)
submit_button.grid(row=8, column=0, columnspan=2, pady=20)

clear_button = tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=20, pady=10)
clear_button.grid(row=9, column=0, columnspan=2)

# Create a label to display the result with more styling
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 14, "bold"), fg="blue", bg="#f0f8ff")
result_label.grid(row=10, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
