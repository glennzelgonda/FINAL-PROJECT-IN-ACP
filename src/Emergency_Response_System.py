from tkinter import *
from tkinter import messagebox, ttk
import threading

# EmergencyAssistanceApp class handles the GUI and user interaction for the Emergency Response System
class EmergencyResponse:
    
    # Constructor - Initializes the main window and sets up the GUI elements
    def __init__(self, root):
        self.root = root
        self.root.geometry("450x450")
        self.root.title("Paspas: Emergency Response System")
        self.root.config(background="white")

        # Set application icon
        icon = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\logo.png')
        self.root.iconphoto(True, icon)

        # Display the logo image
        logo = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\paspas.png').subsample(5, 5)
        logo_label = Label(root, image=logo, background="#b4b9bf", bd=0)
        logo_label.photo = logo  
        logo_label.pack()

        # Frame to hold emergency type buttons
        button_frame = Frame(self.root, background="#ffffff")
        button_frame.pack(pady=20, fill=BOTH, expand=True)

        # Create buttons for different emergency types
        self.create_emergency_buttons(button_frame)

    # Method to create the buttons for emergency types
    def create_emergency_buttons(self, frame):
        # Configure rows and columns to expand in the frame
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Load images for the buttons (Encapsulation used for grouping emergency button images)
        self.fire_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.flood_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.medic_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.crime_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.earthquake_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)

        # Buttons for emergency types (Polymorphism used for handling different emergencies with the same method)
        Button(frame, text="Fire", image=self.fire_img, compound="center", command=self.handle_fire, font="Impact 16", fg="white", bd=0).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Flood", image=self.flood_img, compound="center", command=self.handle_flood, font="Impact 16", fg="white", bd=0).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Medic", image=self.medic_img, compound="center", command=self.handle_medical, font="Impact 16", fg="white", bd=0).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Crime", image=self.crime_img, compound="center", command=self.handle_crime, font="Impact 16", fg="white", bd=0).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        Button(frame, text="Earthquake", image=self.earthquake_img, compound="center", command=self.handle_earthquake, font="Impact 16", fg="white", bd=0).grid(row=2, column=0, columnspan=2, padx=5, pady=(10, 0), sticky="nsew")

    # Handler methods for each emergency type (Polymorphism: same method for different emergencies)
    def handle_fire(self):
        self.get_user_info("Fire")

    def handle_flood(self):
        self.get_user_info("Flood")

    def handle_earthquake(self):
        self.get_user_info("Earthquake")

    def handle_medical(self):
        self.get_user_info("Medical")

    def handle_crime(self):
        self.get_user_info("Crime")

    # Method to collect user information for emergencies
    def get_user_info(self, emergency_type):
        self.emergency_type = emergency_type  # Store the emergency type (Encapsulation)

        # Create a new window to input user information
        self.user_info_window = Toplevel(self.root)
        self.user_info_window.title(f"{emergency_type} Emergency - Enter Your Information")
        self.user_info_window.geometry("335x190")

        # Create fields for name, location, and additional info
        Label(self.user_info_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
        self.name_entry = Entry(self.user_info_window, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.user_info_window, text="Location:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.location_entry = Entry(self.user_info_window, width=30)
        self.location_entry.grid(row=1, column=1, padx=10, pady=5)

        if emergency_type in ["Medical", "Crime"]:
            Label(self.user_info_window, text="Emergency Contact:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
            self.contact_entry = Entry(self.user_info_window, width=30)
            self.contact_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.user_info_window, text="Additional Info:").grid(row=3, column=0, padx=10, pady=5, sticky=E)
        self.additional_info_entry = Entry(self.user_info_window, width=30)
        self.additional_info_entry.grid(row=3, column=1, padx=10, pady=5)

        # Frame for buttons (Abstraction used to simplify button creation)
        button_frame = Frame(self.user_info_window)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        # Buttons for submitting or clearing the entries
        submit_button = Button(button_frame, text="Submit Request", command=self.confirm_details, width=15)
        submit_button.pack(side=LEFT, padx=5)

        clear_button = Button(button_frame, text="Clear", command=self.clear_entries, width=15)
        clear_button.pack(side=LEFT, padx=5)

    # Method to clear user input fields
    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.location_entry.delete(0, END)
        if hasattr(self, 'contact_entry'):
            self.contact_entry.delete(0, END)
        self.additional_info_entry.delete(0, END)

    # Method to confirm the details entered by the user
    def confirm_details(self):
        name = self.name_entry.get().strip()
        location = self.location_entry.get().strip()
        additional_info = self.additional_info_entry.get().strip()
        emergency_contact = self.contact_entry.get().strip() if self.emergency_type in ["Medical", "Crime"] else "N/A"

        # Validate the fields and ensure they are filled correctly (Abstraction used to hide complexity of validation)
        if not name and (not location or location.lower() == "location"):
            messagebox.showwarning("Incomplete Information", "Please provide your name and location to assist you.")
            return
        if not name:
            messagebox.showwarning("Incomplete Information", "Please provide your name to assist you.")
            return
        if not location or location.lower() == "location":
            messagebox.showwarning("Incomplete Information", "Please provide you exact location to assist you.")
            return
        
        if self.emergency_type in ["Medical", "Crime"]:
            if not emergency_contact:
                messagebox.showwarning("Incomplete Information", "Emergency contact number is required.")
                return
            if not emergency_contact.isdigit():
                messagebox.showwarning("Invalid Input", "Emergency contact must contain only numbers.")
                return
            if len(emergency_contact) != 11:  # Check for exactly 11 digits
                messagebox.showwarning("Invalid Input", "Emergency contact must be exactly 11 digits long.")
                return

        # Confirm details before sending request
        confirm_message = (f"Please confirm your details:\n\n"
                           f"Name: {name}\n"
                           f"Location: {location}\n"
                           f"Emergency Contact: {emergency_contact}\n"
                           f"Additional Info: {additional_info}\n\n"
                           f"Is this information correct?")
        if messagebox.askyesno("Confirm Details", confirm_message):
            self.user_info_window.destroy()
            threading.Thread(target=self.send_alert, args=(name, location, emergency_contact, additional_info)).start()

# Method to handle sending alerts with tracking (Abstraction, Polymorphism)
    def send_alert(self, name, location, emergency_contact, additional_info):
        # Create a new window for tracking (Encapsulation)
        self.tracking_window = Toplevel(self.root)
        self.tracking_window.title("Tracking")
        self.tracking_window.geometry("300x150")

        # Display tracking message
        self.tracking_label = Label(self.tracking_window, text="Tracking Location", font=("Impact", 14))
        self.tracking_label.pack(pady=10)

        # Progress bar to show location tracking (Encapsulation)
        self.progress = ttk.Progressbar(self.tracking_window, orient=HORIZONTAL, length=250, mode='determinate')
        self.progress.pack(pady=10)

        # Start tracking animation
        self.animate_tracking()

    # Animate tracking progress (Abstraction)
    def animate_tracking(self):
        current_value = self.progress['value']

        # Animation to show progress and change text dynamically
        if hasattr(self, 'dot_count'):
            self.dot_count = (self.dot_count + 1) % 4
        else:
            self.dot_count = 1
        self.tracking_label.config(text=f"Tracking Location{'.' * self.dot_count}")

        # Increment progress bar and check if it's complete
        if current_value < 100:
            self.progress['value'] += 10  # Increase progress by 10%
            self.tracking_window.after(400, self.animate_tracking)  # Repeat after 400ms
        else:
            self.show_location_confirmed()

    # Method to show location confirmation (Polymorphism)
    def show_location_confirmed(self):
        # Close the tracking window
        self.tracking_window.destroy()

        # Display location confirmation and help on the way
        messagebox.showinfo("Location Confirmed", "Location confirmed.")
        messagebox.showinfo("Assistance", "Help is on the way! Estimated arrival: 10-15 minutes.")
        self.display_emergency_advice()

    # Display emergency advice based on the selected type (Abstraction)
    def display_emergency_advice(self):
        # Dictionary of emergency advice
        reminder = {
            "Flood": "Move to higher ground immediately. Avoid walking or driving through flood waters. Please stay calm.",
            "Earthquake": "Drop, cover, and hold on. Stay away from windows and heavy objects. Please stay calm.",
            "Crime": "Find a safe location. Ensure your safety first; do not intervene if it puts you at risk. If safe, observe and remember details about the suspects and the situation. Stay calm.",
            "Medical": "Administer first aid if trained to do so. Stay calm and wait for the ambulance.",
            "Fire": "Evacuate the building and avoid inhaling smoke. Stay low to the ground if there's heavy smoke."
        }
        
        # Show advice for the selected emergency type
        messagebox.showinfo(f"{self.emergency_type} Reminder", reminder[self.emergency_type])

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = EmergencyResponse(root)
    root.mainloop()