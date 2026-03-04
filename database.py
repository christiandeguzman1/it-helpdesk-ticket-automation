import sqlite3

class HelpdeskDB:
    def __init__(self, db_name='tickets.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                category TEXT,
                priority TEXT,
                status TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def insert_ticket(self, name, description, category, priority, status, timestamp):
        self.cursor.execute("""
            INSERT INTO tickets (name, description, category, priority, status, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, description, category, priority, status, timestamp))
        self.conn.commit()

    def fetch_all_tickets(self):
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tickets")
        return cursor.fetchall()

    def update_ticket_status(self, ticket_id, new_status):
        self.cursor.execute("""
            UPDATE tickets SET status = ? WHERE id = ?
        """, (new_status, ticket_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
