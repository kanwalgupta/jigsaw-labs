
def build_from_record(Class, record):
    if not record: return None
    attr = dict(zip(Class.columns, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def find(cursor, Class, id):
    table = Class.__table__
    columns = Class.columns
    query = f'''
            SELECT *
            FROM {table}
            WHERE {columns[0]} = %s
            '''
            #id will be different depending on the schema, but id is always the first column
    cursor.execute(query, (id,))
    record = cursor.fetchone()
    return build_from_record(Class, record)

def find_all(cursor, Class, limit=10):
    table = Class.__table__
    query = f'''
            SELECT *
            FROM {table}
            LIMIT %s
            '''
    cursor.execute(query, (limit,))
    records = cursor.fetchall()
    return [build_from_record(Class, record) for record in records]