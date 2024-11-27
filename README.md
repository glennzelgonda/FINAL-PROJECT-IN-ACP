![paspas1](https://github.com/user-attachments/assets/e85d75d2-7430-45a7-a041-1ac6f31f06fd)

## I. Project Overview
PASPAS: Emergency Response System is a Python-based application, specifically designed to provide crucial support to individuals amid emergencies. This system connects users to important resources with remarkable speed and efficiency. It empowers users to report a wide array of emergencies, including natural disasters like floods and earthquakes, urgent incidents, fiery blazes, and criminal activities. When users report an emergency, they are promted to provide essential details, such as their name, exact location, and comprehensive description of the situation at hand.

In today's world, especially in our country Philippines, we are experiencing severe calamities, disasters, and crimes or tragedies that cause panic and fear among people. PASPAS is built to address this pressing issue by offering quick assistance during such stressfull moments. This system is created to lessen the stress and confusion often associated with seeking help in crises, particularly for individuals who may be feling panicked or unsure about where to turn for assistance. It effectively addresses commmon challenge of not knowing which emergency hotline to dial, streamlining their path to receiving the help they need without unnecessary delays.

PASPAS goes beyond just reporting emergencies; ut stimulates response procedures. This includes tarcking the user's location in real-time and confirming the rapid deployment of assistance to their location. With its intuitive and user-friendly indterface, along with a highly effective workflow, PASPAS aims to ensure that emergency reporting is accessible to everyone, thereby guaranteeing swift and reliable help during the most critical times.

---

## II. Python Concepts, Libraries, and Features
This project demonstrates the following Python concepts and libraries:

1. **GUI with Tkinter:**
   - `Tkinter` is used to create a user-friendly graphical interface with buttons, labels, entry fields, and pop-ups.
   - Icons and images enhance usability and provide an intuitive experience.
   - Progress bars (`ttk.Progressbar`) simulate tracking.

2. **Threading:**
   - Used for location tracking to prevent the UI from freezing during background processes.

3. **Error Handling and Validation:**
   - Ensures that users provide complete and valid information before proceeding. For example:
     - If a user does not enter both of their **Name** and **Location**, a pop-up warning appears: *Please provide your name and location to assist you.*
     - If a user does not enter their **Name**, a pop-up warning appears: *"Please provide your name to assist you."*
     - If a user does not enter their **Location**, a pop-up warning appears: *"Please provide your location to assist you.* 
     - If the **Emergency Contact** is left blank or contains non-numeric characters, the user is alerted with messages like: *"Emergency contact must contain only numbers."*
     - If a contact number is not exactly 11 digits long, an error message displays: *"Emergency contact must be exactly 11 digits long."*
   - These checks prevent incomplete or invalid data from being processed.

---

## III. Sustainable Development Goal (SDG) Integration
### SDG 11: Sustainable Cities and Communities
The PASPAS system supports SDG 11, which aims to create sustainable and safe cities. It specifically helps improve disaster response and community resilience in the following ways:

1. Improving Emergency Response

 - PASPAS enhances emergency response times by making it easier to report emergencies. When disasters occur, every second counts. PASPAS provides a straightforward interface that helps users select the type of emergency and enter their name, location, and details. This structured approach captures essential information quickly, ensuring that help is dispatched promptly. By automating the reporting process, the system reduces delays and errors that can happen with manual calls.
     
2. Enhancing Disaster Resilience

 - PASPAS helps communities prepare for disasters, whether from nature or human causes. It provides specific reminders on how to act during emergencies. For example, it advises users to find higher ground during floods or to evacuate safely in case of a fire. This readiness helps save lives and lessen the impact of disasters by ensuring that help arrives quickly.
     

3. Promoting Inclusivity

 - A major challenge in emergencies is making sure everyone can access help, regardless of their background or tech skills. PASPAS is designed to be simple and user-friendly, allowing anyone to navigate it easily. This inclusive approach ensures that more people can request assistance during critical times, particularly in areas where emergency services might be harder to reach. By breaking down barriers, PASPAS empowers individuals to act quickly when they need help.
---

## IV. Instructions for Running the Program
### Prerequisites:
- **Python 3.x** installed on your system.
- Required Python libraries (`tkinter`, `ttk` - these come pre-installed with Python).
- Image files for icons and buttons located in `C:\Users\FINAL PROJECT IN ACP\images`.

### Steps to Run:
1. Clone or download the project files.
2. Ensure the image assets (`logo.png`, `paspas.png`, and  `red.png` ) are in the specified directory.
3. Run the Python script:
   ```bash
   python main.py
4. Folder Structure
/project-folder
│
├── /images
│   ├── logo.png              # Application icon
│   ├── paspas.png            # Logo for the application
│   ├── red.png               # Button images for emergency types
│
├── database.py               # Database setup and interaction
├── emergency_response.py     # Main application logic
├── main.py                   # Entry point of the program
├── README.md                 # Documentation (this file)

5. Users Interacting with the GUI
  - Launch the program.
  - Select an Emergency type:
     - Users can click on buttons like "Fire," "Flood," "Medical," "Crime," or "Earthquake" to indicate the type of emergency.
  - Enter user details:
     - After selecting the emergency type, a form appears asking for:
         - Name (required)
         - Location (required)
         - Emergency Contact (required for "Medical" or "Crime" emergencies)
         - Additional Information (optional)
  - Validation of Inputs:
     - If any required fields are missing, users will see warning messages prompting them to complete the form.
  - Submit the Request:
     - Clicking "Submit Request" validates the details and initiates the emergency assistance process.
     - A progress bar and tracking messages simulate real-time location tracking.
  - Receive Confirmation:
     - Users receive confirmation messages like "Location confirmed" and "Help is on the way!"
  - Emergency Reminders:
     - Contextual reminders or tips related to the selected emergency type are shown to guide users on staying safe until help arrives.
  - View History
     - This button allows users to see a detailed record of past emergency reports. It opens a new window displaying the user's name, type of emergency, additional details, location, and the time the emergency was reported.

## Explanation of Functions by their files
*emergency response.py*
Each `def` used in the code plays a specific role in the system. Here's a breakdown:

### 1. `__init__(self, root)`
- Initializes the main application window, sets up the GUI layout, loads images/icons, and sets up connections, including creating an instance of the Database class for handling database operations.

### 2. `create_emergency_buttons(self, frame)`
- Dynamically creates emergency buttons (Fire, Flood, etc.) and links them to their respective handlers.

### 3. `handle_fire(self)`, `handle_flood(self)`, `handle_medical(self)`, `handle_crime(self)`, `handle_earthquake(self)`
- Triggered when a user clicks on a specific emergency button. Each method calls `get_user_info` with the selected emergency type.

### 4. `get_user_info(self, emergency_type)`
- Opens a new window for the user to input their name, location, emergency contact (if applicable), and additional details. Stores the selected emergency type for later use.

### 5. `clear_entries(self)`
- Clears all input fields in the user information window, resetting them to empty.

### 6. `confirm_details(self)`
- Validates the user's input, confirms the details through a pop-up, and starts the alert process if the user agrees.
- **Error Handling Example:**
  - If the user does not provide their name, this block is triggered:
    ```python
    if not name:
        messagebox.showwarning("Incomplete Information", "Please provide your name to assist you.")
        return
    ```
    - This displays a warning pop-up with the message *"Please provide your name to assist you."* and prevents the program from proceeding until the name is entered.
  - Similar validation is done for **Location** and **Emergency Contact**, ensuring input completeness.

### 7. `send_alert(self, name, location, emergency_contact, additional_info)`
- Simulates the process of sending an alert. Opens a tracking window and begins tracking the user's location.

### 8. `animate_tracking(self)`
- Animates the progress bar in the tracking window to simulate location tracking. Updates the UI text dynamically.

### 9. `show_location_confirmed(self)`
- Displays confirmation that the location has been tracked and informs the user that help is on the way.

### 10. `display_emergency_advice(self)`
- Shows emergency-specific advice or reminders based on the selected type.

### 11. `view_history(self)`
- The view_history method creates a new window displaying a table of emergency history records. It retrieves data from the database, formats it into a table with six columns (user ID, name, emergency type, details, location, and timestamp)

**database.py**
- This file defines a Database class responsible for managing the SQLite database used in Emergency Response System. It provides methods to set up the database tables, save user and emergency data, fetch emergency history, and close the connection to the database. Here's a brief description of each method:

### 1. __init__ Method:
- Initializes the database connection and cursor, and calls the setup_tables method to create the necessary tables if they don't already exist.

### 2. setup_tables Method:
- Creates two tables, Users and Emergencies, if they don't exist. The Users table stores user information, while the Emergencies table stores emergency details linked to the users.

### 3. save_user Method:
- Inserts a new user's information (name, contact, location, emergency type) into the Users table and returns the ID of the newly inserted user.

### 4. save_emergency Method:
- Inserts a new emergency record (emergency type, details, user ID) into the Emergencies table.

### 5. close Method:
- Closes the database connection when no longer needed.

### 6. fetch_emergency_history Method:
-  Fetches a complete list of emergency history by joining the Users and Emergencies tables. It retrieves the user's ID, name, emergency type, details, location, and the time the emergency was reported, sorted by the most recent reports.

**main.py**
- This file launches the Emergency Assistance System, acting as the starting point for the program. It creates the main window, initializes the GUI, and runs the application event loop.

---
