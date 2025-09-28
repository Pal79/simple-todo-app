import sqlite3
from models.tasks import Tasks

class TodoDatabase:
    def __init__(self, db_name='todo.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.create_table()
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            description TEXT,
            deadline DATE,
            status BOOLEAN
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def list_todo(self):
        query = 'SELECT * FROM todo ORDER BY id'
        row = self.conn.execute(query).fetchall()
        return [Tasks(row['id'], row['task_name'], row['description'], row['deadline'], row['status']) for row in row]
    
    def add_todo(self, task_name, description, deadline, status):
        query = """
        INSERT INTO todo (task_name, description, deadline, status)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (task_name, description, deadline, status))
        self.conn.commit()
    
    def update_todo(self):
        query = """
        UPDATE todo 
        """

    def delete_todo(self, id):
        cursor = self.conn.execute('DELETE FROM todo WHERE id=?', (id,))
        self.conn.commit()
        return cursor.rowcount
    
    def update_todo(self, id, field, new_value):
        if field not in ("task_name", "description", "deadline", "status"):
            return False
        
        query = f"UPDATE todo SET {field}=? WHERE id=?"
        self.conn.execute(query, (new_value, id))
        self.conn.commit()
        return True