from tkinter import *
from tkinter import messagebox, ttk, simpledialog
from database import Database

class EmergencyResponse:
    def __init__(self, root):
        # Initialize the root window
        self.root = root
        self.root.geometry("480x600")
        self.root.title("Paspas: Emergency Response System")
        self.root.config(background="white")

        # Initialize the database
        self.db = Database()

        # Set application icon
        try:
            icon = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\logo.png')
            self.root.iconphoto(True, icon)
        except Exception as e:
            print(f"Icon not loaded: {e}")

        # Display the logo image
        try:
            logo = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\paspas.png').subsample(5, 5)
            logo_label = Label(root, image=logo, background="#b4b9bf", bd=0)
            logo_label.photo = logo  
            logo_label.pack()
        except Exception as e:
            print(f"Logo not loaded: {e}")

        # Frame to hold emergency type buttons
        button_frame = Frame(self.root, background="#ffffff")
        button_frame.pack(pady=20, fill=BOTH, expand=True)

        # Create buttons for different emergency types
        self.create_emergency_buttons(button_frame)

        # Replace the Button with a Label that looks like a clickable link
        view_history_label = Label(self.root, text="View History", font=("Helvetica", 12, "underline"), fg="#383838", cursor="hand2", background="white")
        view_history_label.pack(pady=(10, 5), padx=0)

        # Bind the click event to open the history
        view_history_label.bind("<Button-1>", lambda e: self.view_history())


    # Method to create the buttons for emergency types
    def create_emergency_buttons(self, frame):
        # Configure rows and columns to expand in the frame
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Load images for the buttons (grouped using encapsulation)
        self.fire_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.flood_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.medic_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.crime_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png').subsample(5, 5)
        self.earthquake_img = PhotoImage(file=r'C:\Users\FINAL PROJECT IN ACP\images\red.png ').subsample(3, 3)

        # Buttons for emergency types (use polymorphism for handling different emergencies)
        Button(frame, text="Fire", image=self.fire_img, compound="center", command=self.handle_fire, font="Impact 20", fg="white", bd=0, width=12, height=4).grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
        Button(frame, text="Flood", image=self.flood_img, compound="center", command=self.handle_flood, font="Impact 20", fg="white", bd=0, width=12, height=4).grid(row=0, column=1, padx=2, pady=5, sticky="nsew")
        Button(frame, text="Medic", image=self.medic_img, compound="center", command=self.handle_medical, font="Impact 20", fg="white", bd=0, width=12, height=4).grid(row=1, column=0, padx=2, pady=5, sticky="nsew")
        Button(frame, text="Crime", image=self.crime_img, compound="center", command=self.handle_crime, font="Impact 20", fg="white", bd=0, width=12, height=4).grid(row=1, column=1, padx=2, pady=5, sticky="nsew")
        Button(frame, text="Earthquake", image=self.earthquake_img, compound="center", command=self.handle_earthquake, font="Impact 20", fg="white", bd=0, width=12, height=4).grid(row=2, column=0, columnspan=2, padx=2, pady=5, sticky="nsew")

    # Handler methods for each emergency type (polymorphism used here)
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

    def get_user_info(self, emergency_type):
        # Open a new window for user input based on the emergency type
        self.emergency_type = emergency_type  # Store the emergency type (encapsulation)

        self.user_info_window = Toplevel(self.root)
        self.user_info_window.title(f"{emergency_type} Emergency - Enter Your Information")
        self.user_info_window.geometry("335x190")

        # User input fields
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

        # Buttons for submission and clearing inputs
        button_frame = Frame(self.user_info_window)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        Button(button_frame, text="Submit Request", command=self.confirm_details, width=15).pack(side=LEFT, padx=5)
        Button(button_frame, text="Clear", command=self.clear_entries, width=15).pack(side=LEFT, padx=5)

    def clear_entries(self):
        # Clear all input fields
        self.name_entry.delete(0, END)
        self.location_entry.delete(0, END)
        if hasattr(self, "contact_entry"):
            self.contact_entry.delete(0, END)
        self.additional_info_entry.delete(0, END)

    def confirm_details(self):
         # Validate and save user input details
        name = self.name_entry.get().strip()
        location = self.location_entry.get().strip()
        contact = self.contact_entry.get().strip() if hasattr(self, "contact_entry") else None
        additional_info = self.additional_info_entry.get().strip()

         # Validation checks
        if not name and not location:
             messagebox.showwarning("Incomplete Information", "Please provide your name and location to assist you.")
             return
    
        if not name:
             messagebox.showwarning("Incomplete Information", "Please provide your name to assist you.")
             return
    
        if not location:
             messagebox.showwarning("Incomplete Information", "Please provide your location to assist you.")
             return
    
        if self.emergency_type in ["Medical", "Crime"]:
             if not contact:
                 messagebox.showwarning("Emergency Contact Needed", "Please enter your emergency contact so we can notify your family immediately.")
                 return
             if not contact.isdigit():
                 messagebox.showwarning("Invalid Emergency Contact", "Emergency contact number must contain only digits.")
                 return
             if len(contact) != 11:
                 messagebox.showwarning("Invalid Emergency Contact", "Emergency contact number must be exactly 11 digits long.")
                 return
        else:
             contact = None

         # Confirmation of entered details
        confirmation_message = f"Please confirm your details:\n\nName: {name}\nLocation: {location}"
        if self.emergency_type in ["Medical", "Crime"]:
             confirmation_message += f"\nContact: {contact}"
        confirmation_message += f"\nAdditional Info: {additional_info if additional_info else 'N/A'}"

         # Show the confirmation dialog
        if not messagebox.askyesno("Confirm Details", confirmation_message):
             # If the user selects 'No', do not proceed
            return

         # Save to database
        user_id = self.db.save_user(name, contact, location, self.emergency_type)
        self.db.save_emergency(self.emergency_type, additional_info, user_id)
    
        # Close the user info window
        self.user_info_window.destroy()
    
        # Send an alert to responders
        self.send_alert(name, location, contact, additional_info)
    
    def send_alert(self, name, location, contact, additional_info):
        # Start tracking progress for responders
        self.tracking_window = Toplevel(self.root)
        self.tracking_window.title("Tracking")
        self.tracking_window.geometry("400x150")

        # Add progress bar for tracking
        self.tracking_label = Label(self.tracking_window, text="Tracking Location...")
        self.tracking_label.pack(pady=10)

        self.progress = ttk.Progressbar(self.tracking_window, length=300, mode="determinate", maximum=100)
        self.progress.pack(pady=10)

        # Start tracking animation
        self.animate_tracking()

    def animate_tracking(self):
        # Simulate tracking progress animation
        current_value = self.progress["value"]
        if not hasattr(self, "dot_count"):
            self.dot_count = 1

        self.dot_count = (self.dot_count + 1) % 4
        self.tracking_label.config(text=f"Tracking Location{'.' * self.dot_count}", font=("Impact", 14))

        if current_value < 100:
            self.progress["value"] += 10
            self.tracking_window.after(400, self.animate_tracking)
        else:
            self.show_location_confirmed()

    def show_location_confirmed(self):
        # Display confirmation that location tracking is complete
        self.tracking_window.destroy()

        responders = {
            "Fire": "The firefighters are on the way. Estimated arrival: 10-15 minutes.",
            "Flood": "Rescue teams are on the way. Estimated arrival: 10-15 minutes.",
            "Medical": "An ambulance is on the way. Estimated arrival: 10-15 minutes.",
            "Crime": "The police are on the way. Estimated arrival: 10-15 minutes.",
            "Earthquake": "Disaster response teams are on the way. Estimated arrival: 10-15 minutes."
        }

        messagebox.showinfo("Location Confirmed", "Location confirmed.")
        messagebox.showinfo("Responder", responders[self.emergency_type])
        self.display_emergency_advice()

    def display_emergency_advice(self):
        # Display emergency-specific advice
        reminders = {
            "Flood": "Move to higher ground immediately. Avoid walking or driving through flood waters.",
            "Earthquake": "Drop, cover, and hold on. Stay away from windows and heavy objects.",
            "Crime": "Find a safe location. Ensure your safety first; do not intervene.",
            "Medical": "Administer first aid if trained to do so. Stay calm and wait for the ambulance.",
            "Fire": "Evacuate the building and avoid inhaling smoke. Stay low to the ground."
        }

        messagebox.showinfo(f"{self.emergency_type} Reminder", reminders[self.emergency_type])

    def view_history(self):
        # Create a new window for viewing history
        history_window = Toplevel(self.root)
        history_window.title("Emergency History")
        history_window.geometry("9000x500")

        history_window.config(bg="black")

        # Create a table using Treeview
        columns = ("emergency_id", "name", "emergency_type", "details", "location", "timestamp", "responder_name")
        tree = ttk.Treeview(history_window, columns=columns, show="headings", height=15)
        tree.pack(fill=BOTH, expand=True)

        # Create a style object for customization
        style = ttk.Style()
        style.theme_use("clam")

        # Configure Treeview background color and text color
        style.configure("Treeview",
                    background="#232323",   
                    foreground="black",   
                    fieldbackground="#232323",  
                    font=("Arial", 10)) 

        # Configure the Treeview Heading
        style.configure("Treeview.Heading",
                    background="#232323",  # Set the background of headings
                    foreground="pink",   # Set the text color of headings
                    font=("Arial", 10, "bold"))  # Optionally set font for heading

        # Set column headings
        tree.heading("emergency_id", text="Emergency_id", anchor="center")
        tree.heading("name", text="Name", anchor="center")
        tree.heading("emergency_type", text="Emergency Type", anchor="center")
        tree.heading("details", text="Additional Info", anchor="center")
        tree.heading("location", text="Location", anchor="center")
        tree.heading("timestamp", text="Reported Time", anchor="center")
        tree.heading("responder_name", text="Responder", anchor="center")

        # Set column widths
        tree.column("emergency_id", width=80, anchor="center")
        tree.column("name", width=100, anchor="center")
        tree.column("emergency_type", width=100, anchor="center")
        tree.column("details", width=150, anchor="center")
        tree.column("location", width=150, anchor="center")
        tree.column("timestamp", width=150, anchor="center")
        tree.column("responder_name", width=150, anchor="center")

        # Set row colors (alternating gray and dark gray)
        tree.tag_configure("gray", background="gray", foreground="black")
        tree.tag_configure("darkgray", background="darkgray", foreground="black")

        # Fetch data from the database
        history_data = self.db.fetch_emergency_history()

        # Populate the Treeview with the data
        for idx, record in enumerate(history_data):
            # Alternate between gray and dark gray for rows
            row_tag = "gray" if idx % 2 == 0 else "darkgray"
            tree.insert("", "end", values=record, tags=(row_tag,))

    # Create Cancel and Update buttons
        button_frame = Frame(history_window, bg="black")
        button_frame.pack(pady=10, fill=X)

        cancel_button = Button(button_frame, text="Cancel Request", command=lambda: self.cancel_request(tree), bg="red", fg="white", width=15)
        cancel_button.pack(side=LEFT, padx=10)

        update_button = Button(button_frame, text="Update Request", command=lambda: self.update_request(tree), bg="orange", fg="white", width=15)
        update_button.pack(side=RIGHT, padx=10)

    def cancel_request(self, tree):
        # Get selected item
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an emergency request to cancel.")
            return

        values = tree.item(selected_item, "values")
        emergency_id = values[0] 
        name = values[1] 

        # Confirm cancellation
        if messagebox.askyesno("Cancel Request", f"Are you sure you want to cancel the request for  {name}?"):
            # Remove from database
            self.db.remove_emergency_request(emergency_id, name)
            messagebox.showinfo("Request Cancelled", "The request has been successfully cancelled.")

            # Refresh the history table
            self.refresh_history(tree)

    def update_request(self, tree):
        # Get selected item
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an emergency request to update.")
            return

        emergency_id = tree.item(selected_item, "values")[0] 

        # Fetch current record details
        current_details = self.db.fetch_user_details(emergency_id)

        # Open a new window to update the details
        self.update_window = Toplevel(self.root)
        self.update_window.title("Update Emergency Details")
        self.update_window.geometry("335x250")

        # User input fields pre-filled with current values
        Label(self.update_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
        self.name_entry = Entry(self.update_window, width=30)
        self.name_entry.insert(0, current_details[1])
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.update_window, text="Location:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.location_entry = Entry(self.update_window, width=30)
        self.location_entry.insert(0, current_details[3])
        self.location_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.update_window, text="Additional Info:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
        self.additional_info_entry = Entry(self.update_window, width=30)
        self.additional_info_entry.insert(0, current_details[4] if current_details[4] else "")
        self.additional_info_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons for submitting the update
        button_frame = Frame(self.update_window)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)

        Button(button_frame, text="Submit Update", command=lambda: self.submit_update(emergency_id, tree), width=15).pack(side=LEFT, padx=5)
        Button(button_frame, text="Cancel", command=self.update_window.destroy, width=15).pack(side=LEFT, padx=5)

    def submit_update(self, emergency_id, tree):
        # Get updated details from the entry fields
        updated_name = self.name_entry.get().strip()
        updated_location = self.location_entry.get().strip()
        updated_additional_info = self.additional_info_entry.get().strip()

        # Validate and update the record in the database
        if not updated_name or not updated_location:
             messagebox.showwarning("Incomplete Information", "Name and location must be provided.")
             return

        self.db.update_emergency_request(emergency_id, updated_name, updated_location, updated_additional_info)

        # Update the treeview (refresh)
        self.refresh_history(tree)

        # Close the update window after submitting
        self.update_window.destroy()

    def refresh_history(self, tree):
        # Clear existing rows in the Treeview
        tree.delete(*tree.get_children())

        # Fetch updated data from the database
        history_data = self.db.fetch_emergency_history()

        # Populate the Treeview with the refreshed data
        for idx, record in enumerate(history_data):
            row_tag = "gray" if idx % 2 == 0 else "darkgray"
            tree.insert("", "end", values=record, tags=(row_tag,))