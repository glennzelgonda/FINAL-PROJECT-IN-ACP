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
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT,
                location TEXT NOT NULL,
                selected_emergency TEXT    
            )
        """)

        # Create Emergencies table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Emergencies (
                emergency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                emergency_type TEXT NOT NULL,
                details TEXT,
                reported_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users (user_id)
            )
        """)
        self.conn.commit()

    def save_user(self, name, contact, location, emergency_type):
        self.cursor.execute("INSERT INTO Users (name, contact, location, selected_emergency) VALUES (?, ?, ?, ?)", 
                            (name, contact, location, emergency_type))
        return self.cursor.lastrowid

    def save_emergency(self, emergency_type, details, user_id):
        self.cursor.execute("INSERT INTO Emergencies (emergency_type, details, user_id) VALUES (?, ?, ?)", 
                            (emergency_type, details, user_id))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def fetch_emergency_history(self):
        # Join Users and Emergencies tables to get complete data
        self.cursor.execute("""
            SELECT u.user_id, u.name, e.emergency_type, e.details, u.location, e.reported_time
            FROM Emergencies e
            JOIN Users u ON e.user_id = u.user_id
            ORDER BY e.reported_time DESC
        """)
        return self.cursor.fetchall()