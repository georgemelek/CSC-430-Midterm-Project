import sqlite3
from models.functions import _get_query_results

class ClassModel:
    TABLE_NAME = 'class'

    def __init__ (self):
        self.conn = sqlite3.connect('lab3.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create(self, params : dict):
        p = ( params.get('title', '') , params.get('description', '') )
        query = f'INSERT INTO class (title, description) values (?, ?);'

        cur = self.conn.cursor()
        cur.execute(query, p)

        class_data = self.get_class({'id': cur.lastrowid})
        
        return class_data

    def get_all_classes(self):
        query = 'SELECT * FROM class;'

        result_set = self.conn.execute(query).fetchall()
        result = _get_query_results(result_set)
        
        return result

    # Assumes that the row exists
    def get_class(self, params : dict):
        p = (str(params['id']))
        query = 'SELECT * FROM class WHERE id = ?;'

        result_set = self.conn.execute(query, p).fetchall()
        result = _get_query_results(result_set)
        
        return result[0]
