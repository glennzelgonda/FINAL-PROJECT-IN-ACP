import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("emergency_response.db")
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        # Create Users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                emergency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT,
                location TEXT NOT NULL,
                selected_emergency TEXT    
            )
        """)

        # Create Emergencies table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Emergencies (
                emergency_type TEXT NOT NULL,
                details TEXT,
                reported_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                emergency_id INTEGER,
                FOREIGN KEY (emergency_id) REFERENCES Users (emergency_id)
            )
        """)
        self.conn.commit()

    def save_user(self, name, contact, location, emergency_type):
        self.cursor.execute("INSERT INTO Users (name, contact, location, selected_emergency) VALUES (?, ?, ?, ?)", 
                            (name, contact, location, emergency_type))
        return self.cursor.lastrowid  # This will now return emergency_id

    def save_emergency(self, emergency_type, details, emergency_id):
        self.cursor.execute("INSERT INTO Emergencies (emergency_type, details, emergency_id) VALUES (?, ?, ?)", 
                            (emergency_type, details, emergency_id))
        self.conn.commit()

    def fetch_emergency_history(self):
        # Join Users and Emergencies tables to get complete data
        self.cursor.execute("""
            SELECT u.emergency_id, u.name, e.emergency_type, e.details, u.location, e.reported_time
            FROM Emergencies e
            JOIN Users u ON e.emergency_id = u.emergency_id
            ORDER BY e.reported_time DESC   
        """)
        return self.cursor.fetchall()

    def remove_emergency_request(self, emergency_id):
        # Delete the emergency record from both Users and Emergencies tables
        self.cursor.execute("DELETE FROM Emergencies WHERE emergency_id = ?", (emergency_id,))
        self.cursor.execute("DELETE FROM Users WHERE emergency_id = ?", (emergency_id,))
        self.conn.commit()

    def update_emergency_request(self, emergency_id, name, location, additional_info):
        # Update the emergency record in both Users and Emergencies tables
        self.cursor.execute("""
            UPDATE Users SET name = ?, location = ? WHERE emergency_id = ?
        """, (name, location, emergency_id))

        self.cursor.execute("""
            UPDATE Emergencies SET details = ? WHERE emergency_id = ?
        """, (additional_info, emergency_id))

        self.conn.commit()

    def fetch_user_details(self, emergency_id):
        # Fetch the user's details based on emergency_id
        self.cursor.execute("""
            SELECT u.emergency_id, u.name, u.contact, u.location, e.details
            FROM Users u
            LEFT JOIN Emergencies e ON u.emergency_id = e.emergency_id
            WHERE u.emergency_id = ?
        """, (emergency_id,))
        return self.cursor.fetchone()