import sqlite3
from models.functions import _get_query_results

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
        student_data = self.get_student({'username': params['username']})

        return student_data

    def login(self, params : dict):
        p = (params['username'], params['password'])
        query = 'SELECT EXISTS ( SELECT * FROM student WHERE username = ? AND password = ? );'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)

        isValid = [x for x in result[0].values()][0]

        return isValid == 1

    # Assumes that the row exists
    def get_student(self, params : dict):
        p = (params.get('username', ''), params.get('id', ''))
        query = 'SELECT id, username, first_name, last_name, address, phone_number, email FROM student WHERE username = ? OR id = ?;'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)
        
        return result[0]