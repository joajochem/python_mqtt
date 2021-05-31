#!/usr/bin/env python3



import mysql.connector

connection = mysql.connector.connect(host='192.168.1.162',
                                        database='test_db',
                                        user='db_user',
                                        password='mqttpassword')

mycursor = connection.cursor()


#mycursor.execute("SELECT * FROM nodes")




nodes_dict = {'Name': 'nodes1', 'Status': 'Online', 'ip_address': '192.168.1.1'}

nodes_dict['Name']


def check_db():
    
    mycursor.execute("""select * from nodes where Name = %s
    """, (nodes_dict['Name'],))
    row = mycursor.fetchone()
    return row 


row = check_db()

if not row:
    print("Doesn't exist")
    print("Adding entry")
    mycursor.execute("""insert into nodes (Name, Status, ip_address) VALUES (%s, %s, %s)""",
    (nodes_dict['Name'], nodes_dict['Status'],))
    connection.commit()

nodes_dict = {'Name': 'nodes1', 'Status': 'online'}

if row:
    print("changing status")
    mycursor.execute("""update nodes set Status = %s WHERE Name = %s""",
    (nodes_dict['Status'], nodes_dict['Name'],))
    connection.commit()
    print(mycursor.rowcount, "record(s) affected")
else:
    print("Nothing to do")



