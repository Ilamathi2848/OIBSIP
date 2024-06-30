import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt

# BMI Calculation Functions
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# GUI Application
class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        
        # Create Widgets
        self.create_widgets()
        
        # Load historical data
        self.load_data()

    def create_widgets(self):
        # User Entry
        tk.Label(self.root, text="User Name:").grid(row=0, column=0)
        self.user_entry = tk.Entry(self.root)
        self.user_entry.grid(row=0, column=1)

        # Weight Input
        tk.Label(self.root, text="Weight (kg):").grid(row=1, column=0)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=1, column=1)

        # Height Input
        tk.Label(self.root, text="Height (m):").grid(row=2, column=0)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=2, column=1)

        # Calculate Button
        self.calculate_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        # Clear Button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=4, column=0, columnspan=2)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=5, column=0, columnspan=2)

        # Show History Button
        self.history_button = tk.Button(self.root, text="Show History", command=self.show_history)
        self.history_button.grid(row=6, column=0, columnspan=2)

    def calculate_bmi(self):
        try:
            user = self.user_entry.get().strip()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter numeric values for weight and height, and a valid user name.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        self.result_label.config(text=f"User: {user}\nYour BMI is: {bmi:.2f}\nCategory: {category}")
        
        # Save to history
        self.save_data(user, weight, height, bmi, category)

    def save_data(self, user, weight, height, bmi, category):
        data = {
            "user": user,
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "category": category
        }

        # Load existing data
        if os.path.exists("bmi_history.json"):
            with open("bmi_history.json", "r") as file:
                try:
                    file_data = json.load(file)
                except json.JSONDecodeError:
                    file_data = []
        else:
            file_data = []

        # Append new data
        file_data.append(data)

        # Write updated data back to the file
        with open("bmi_history.json", "w") as file:
            json.dump(file_data, file, indent=4)

    def load_data(self):
        self.history = []
        if os.path.exists("bmi_history.json"):
            with open("bmi_history.json", "r") as file:
                try:
                    self.history = json.load(file)
                except json.JSONDecodeError:
                    self.history = []

    def show_history(self):
        if not self.history:
            messagebox.showinfo("No Data", "No historical data available.")
            return
        
        user_data = {}
        
        # Organize data by user
        for entry in self.history:
            user = entry['user']
            if user not in user_data:
                user_data[user] = {'weights': [], 'heights': [], 'bmis': []}
            user_data[user]['weights'].append(entry['weight'])
            user_data[user]['heights'].append(entry['height'])
            user_data[user]['bmis'].append(entry['bmi'])
        
        # Debug: Print organized user data
        print("User Data:", user_data)
        
        # Plotting the data
        plt.figure()
        markers = ['o', 's', 'D', '^', 'v', '>', '<', 'p', '*', 'h']
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
        marker_index = 0
        
        for user, data in user_data.items():
            if data['bmis']:  # Check if there are BMI values to plot
                plt.plot(data['bmis'], label=f"{user}'s BMI over time", marker=markers[marker_index % len(markers)], color=colors[marker_index % len(colors)])
                marker_index += 1
        
        # Adding labels and title
        plt.xlabel("Entry")
        plt.ylabel("BMI")
        plt.title("BMI History")
        
        # Adding a legend to differentiate users
        plt.legend()
        
        # Display the plot
        plt.show()

    def clear_fields(self):
        self.user_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
   
