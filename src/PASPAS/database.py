import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("emergency_response.db")
        self.cursor = self.conn.cursor()
        self.setup_tables()
        self.insert_default_responders()  # Insert responder values on initialization

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

        # Create Responder table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Responder (
                responder_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                responder_type TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_default_responders(self):
        """Insert default responder data if the Responder table is empty."""
        self.cursor.execute("SELECT COUNT(*) FROM Responder")
        if self.cursor.fetchone()[0] == 0:  # Check if table is empty
            responders = [
                ('Bureau of Fire Protection', '911', 'Fire'),
                ('Philippine Coast Guard', '09269629291', 'Flood'),
                ('Philippine Red Cross', '143', 'Medical'),
                ('Philippine National Police', '2920', 'Crime'),
                ('NDRRMC', '(02) 8911-5061', 'Earthquake')
            ]
            self.cursor.executemany("""
                INSERT INTO Responder (name, contact, responder_type) 
                VALUES (?, ?, ?)
            """, responders)
            self.conn.commit()

    def save_user(self, name, contact, location, emergency_type):
        self.cursor.execute("INSERT INTO Users (name, contact, location, selected_emergency) VALUES (?, ?, ?, ?)", 
                            (name, contact, location, emergency_type))
        self.conn.commit()
        return self.cursor.lastrowid  # This will return emergency_id

    def save_emergency(self, emergency_type, details, emergency_id):
        self.cursor.execute("INSERT INTO Emergencies (emergency_type, details, emergency_id) VALUES (?, ?, ?)", 
                            (emergency_type, details, emergency_id))
        self.conn.commit()

    def fetch_emergency_history(self):
        self.cursor.execute("""
            SELECT u.emergency_id, u.name, e.emergency_type, e.details, u.location, e.reported_time, r.name AS responder_name
            FROM Emergencies e
            JOIN Users u ON e.emergency_id = u.emergency_id
            LEFT JOIN Responder r ON e.emergency_type = r.responder_type
            ORDER BY e.reported_time DESC
        """)
        return self.cursor.fetchall()

    def remove_emergency_request(self, emergency_id):
        self.cursor.execute("DELETE FROM Emergencies WHERE emergency_id = ?", (emergency_id,))
        self.cursor.execute("DELETE FROM Users WHERE emergency_id = ?", (emergency_id,))
        self.conn.commit()

    def update_emergency_request(self, emergency_id, name, location, additional_info):
        self.cursor.execute("""
            UPDATE Users SET name = ?, location = ? WHERE emergency_id = ?
        """, (name, location, emergency_id))

        self.cursor.execute("""
            UPDATE Emergencies SET details = ? WHERE emergency_id = ?
        """, (additional_info, emergency_id))
        self.conn.commit()

    def fetch_user_details(self, emergency_id):
        self.cursor.execute("""
            SELECT u.emergency_id, u.name, u.contact, u.location, e.details
            FROM Users u
            LEFT JOIN Emergencies e ON u.emergency_id = e.emergency_id
            WHERE u.emergency_id = ?
        """, (emergency_id,))
        return self.cursor.fetchone()
