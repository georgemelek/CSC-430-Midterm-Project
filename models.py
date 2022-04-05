import sqlite3

def _get_query_results(result_set : list):
    result = [{column: row[i]
                for i, column in enumerate(result_set[0].keys())}
                for row in result_set]

    return result

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

class StudentModel:
    TABLE_NAME = 'student'

    def __init__ (self):
        self.conn = sqlite3.connect('lab3.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    #TODO catch not unique error
    def create(self, params : dict):
        p = (
            params['username'], 
            params['password'], 
            params['first_name'], 
            params['last_name'], 
            params.get('address', ''), 
            params.get('phone_number', ''), 
            params.get('email', '')
            )
        query = f'INSERT INTO student (username, password, first_name, last_name, ' \
                f'address, phone_number, email) values (?, ?, ?, ?, ?, ?, ?);'

        self.conn.execute(query, p)
        
        return {'data': 'Operation Complete'}

    def login(self, params : dict):
        p = (params['username'], params['password'])
        query = 'SELECT EXISTS ( SELECT * FROM student WHERE username = ? AND password = ? );'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)

        isValid = [x for x in result[0].values()][0]

        return isValid == 1

    # Assumes that the row exists
    def _get_info(self, params : dict):
        p = (params.get('username', ''), params.get('id', ''))
        query = 'SELECT id, username, first_name, last_name, address, phone_number, email FROM student WHERE username = ? OR id = ?;'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)
        
        return result[0]