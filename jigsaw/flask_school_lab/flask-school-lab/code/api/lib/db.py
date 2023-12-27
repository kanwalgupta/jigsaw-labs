
# functions
# - find
# - find_all
# - build_from_record
# - build_from_records
# - save

def find_all(Class, conn):
    cursor = conn.cursor()
    value = Class.__table__
    query = '''
            SELECT *
            FROM teachers
            '''
    cursor.execute(query, (value,))
    records = cursor.fetchall()
    return records

def find(Class, id, conn):
    cursor = conn.cursor()
    value = Class.__table__
    query = '''
            SELECT *
            FROM teachers t
            WHERE t.id = %s
            '''
    cursor.execute(query,(id,))
    teacher_record = cursor.fetchall()
    return teacher_record

def build_from_record(Class, record):
    #use find to get records
    #need to pass in key,value pair as input to the class, so zip together columns and record values
    #record = find(Class, id, conn) 
    attributes = dict(zip(Class.columns, record))
    #result is a tuple, but we need to pass the input as 'key=value'
    #attr_list = []
#     for attribute in attributes:
#         for k,v in attribute:
#             attr_list.append(f"{k}={v}")
#     attr_str = ",".join(attr_list)
    #print(attributes)
    #test_dict = {id:1,name:joe}
    obj = Class()
    obj.__dict__ = attributes
    return obj.__dict__

def build_from_records(Class, records):
    records_list = []
    for record in records:
        #obj = build_from_record(Class, record)
        records_list.append(build_from_record(Class, record))
    return records_list

def save(obj, conn):
    # function is for fixtures, takes an object's attributes as input?
    #connect to db
    #query is insert statement
        #iterate through object's attributes 
    table = obj.__table__

    keys = list(obj.__dict__.keys())
    key_string = ",".join(keys)

    values = list(obj.__dict__.values())
    val_string = ""
    
    if len(values) > 1:
        val_string = ",".join(list(values))
    else:
        val_string = str(values[0])
    s_string = (len(keys)* '%s,')
    #s_string_final = s_string[:-1]
    query = f'''
            INSERT INTO {table} ({key_string}) (
                VALUES ({s_string[:-1]})
            );
            '''
    
    cursor = conn.cursor()
    cursor.execute(query, (val_string,))
    conn.commit()

def clear_table(table, conn):
    cursor = conn.cursor()
    #print(table)
    query = f'DELETE FROM {table}'
    cursor.execute(query)
    conn.commit()

    



