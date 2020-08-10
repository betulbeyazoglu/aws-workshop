import mysql.connector
from mysql.connector import errorcode


config={
    'user': 'admin',
    'password': '12345678',
    'host':'phonebookapp-db.cdl8izlywybk.us-east-1.rds.amazonaws.com',
    'database':'phonebook',
    'raise_on_warnings':True
}

def init_pb_db(cursor):
    #drop_table='DROP TABLE IF EXISTS phonebook.persons;'
    pb_table="""
    CREATE TABLE persons (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    number varchar(255) NOT NULL,
    PRIMARY KEY (ID)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """
    data = """
    INSERT INTO phonebook.persons(name,number) 
    VALUES 
        ("Ammy Franky", "5714356782" ),
        ("Betty Smart", "5647839201"),
        ("Jhony Drift", "2347654839");
    """
    #cursor.execute(drop_table)
    cursor.execute(pb_table)
    cursor.execute(data)

try:
    cnx=mysql.connector.connect(**config)
    init_pb_db(cnx.cursor(buffered=True))
    cnx.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exits.")
    else:
        print(err)
else:
    print("Phonebook table created and populated successfull")
    cnx.close()