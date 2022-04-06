import sqlite3

class Schema:
    def __init__ (self):
        self.conn = sqlite3.connect('lab3.db')
        self.create_student_table()
        self.create_class_table()
        self.create_student_class_table()
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_student_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT,
            phone_number TEXT,
            email TEXT,
            created_on Date default CURRENT_DATE
        );
        """

        self.conn.execute(query)

    def create_class_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS class (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            created_on Date DEFAULT CURRENT_DATE
        );
        """

        self.conn.execute(query)

    def create_student_class_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS student_class (
            id INTEGER PRIMARY KEY,
            student_id INTEGER FOREIGNKEY REFERENCES student(id),
            class_id INTEGER FOREIGNKEY REFERENCES class(id),
            created_on Date DEFAULT CURRENT_DATE,
            UNIQUE(student_id, class_id)
        );
        """

        self.conn.execute(query)