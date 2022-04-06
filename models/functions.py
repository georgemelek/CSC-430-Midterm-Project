import sqlite3

def _get_query_results(result_set : list):
    result = [{column: row[i]
                for i, column in enumerate(result_set[0].keys())}
                for row in result_set]

    return result
