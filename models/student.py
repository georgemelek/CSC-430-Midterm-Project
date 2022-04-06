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
            str(params.get('phone_number', '')), 
            params.get('email', '')
            )
        query = f'INSERT INTO student (username, password, first_name, last_name, ' \
                f'address, phone_number, email) values (?, ?, ?, ?, ?, ?, ?);'

        cur = self.conn.cursor()
        cur.execute(query, p)

        return {'id': cur.lastrowid}

    def login(self, params : dict):
        p = (params['username'], params['password'])
        query = 'SELECT EXISTS ( SELECT * FROM student WHERE username = ? AND password = ? );'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)

        isValid = [x for x in result[0].values()][0]

        return isValid == 1

    def update_info(self, params : dict):
        p = (
            params.get('first_name', ''),
            params.get('last_name', ''),
            params.get('address', ''), 
            str(params.get('phone_number', '')), 
            params.get('email', ''),
            str(params.get('id', '')),
            params.get('username', '')
            )
        query = f'UPDATE student SET first_name = ?, last_name = ?, ' \
                f'address = ?, phone_number = ?, email = ? ' \
                f'WHERE id = ? OR username = ?;'

        cur = self.conn.cursor()
        cur.execute(query, p)

        return cur.rowcount == 1

    # Assumes that the row exists
    def get_student(self, params : dict):
        p = (params.get('username', ''), str(params.get('id', '')))
        query = 'SELECT id, username, first_name, last_name, address, phone_number, email FROM student WHERE username = ? OR id = ?;'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)
        
        return result[0]

    def get_classes(self, params : dict):
        p = (str(params['student_id']))
        query = f'SELECT class.id AS class_id, class.title AS class_title, class.description AS class_description ' \
                f'FROM class INNER JOIN student_class ON class.id = student_class.class_id ' \
                f'WHERE student_class.student_id = ?;'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)

        return result

    def add_class(self, params : dict):
        p = (str(params['student_id']), str(params['class_id']))
        query = f'INSERT INTO student_class (student_id, class_id) values (?, ?);'

        self.conn.execute(query, p)
        student_schedule = self.get_classes({'student_id' : params['student_id']})

        return student_schedule