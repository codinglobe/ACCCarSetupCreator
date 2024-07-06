import tkinter as tk
from tkinter import ttk
import json

class SetupGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ACC Car Setup")

        # Car Setup Attributes
        self.attributes = [
            "Tire Pressure Front Left",
            "Tire Pressure Front Right",
            "Tire Pressure Rear Left",
            "Tire Pressure Rear Right",
            "Camber Front",
            "Camber Rear",
            "Toe Front",
            "Toe Rear",
            "Ride Height Front",
            "Ride Height Rear",
        ]
        
        self.entries = {}

        for idx, attribute in enumerate(self.attributes):
            label = ttk.Label(root, text=attribute)
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="W")
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[attribute] = entry

        # Save Button
        self.save_button = ttk.Button(root, text="Save Setup", command=self.save_setup)
        self.save_button.grid(row=len(self.attributes), column=0, columnspan=2, pady=10)

    def save_setup(self):
        setup_data = {attribute: self.entries[attribute].get() for attribute in self.attributes}
        
        with open("car_setup.json", "w") as f:
            json.dump(setup_data, f, indent=4)
        
        print("Setup saved to car_setup.json")

if __name__ == "__main__":
    root = tk.Tk()
    app = SetupGUI(root)
    root.mainloop()
