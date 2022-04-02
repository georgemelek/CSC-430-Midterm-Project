import sqlite3

class Schema:
    def __init__ (self):
        self.conn = sqlite3.connect('lab3.db')
        self.create_student_table()
        self.create_class_table()
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_student_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Password TEXT NOT NULL,
            Name TEXT NOT NULL,
            CreatedOn Date default CURRENT_DATE
        );
        """

        self.conn.execute(query)

    def create_class_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Class (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            CreatedOn Date DEFAULT CURRENT_DATE
        );
        """

        self.conn.execute(query)

class StudentModel:
    TABLE_NAME = 'Student'

    def __init__ (self):
        self.conn = sqlite3.connect('lab3.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def create(self, params):
        query = f"INSERT INTO {self.TABLE_NAME} " \
                f"(Username, Password, Name) values " \
                f'("{params.get("Username")}", "{params.get("Password")}", ' \
                f'"{params.get("Name")}");'
        
        print(query)
        result = self.conn.execute(query)
        print(result)
        
        return {"data": "Operation Complete"}
