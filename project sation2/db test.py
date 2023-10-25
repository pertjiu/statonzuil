import psycopg2.extras

# connection_string = "host= '127.0.0.1',database='module 2.1',user='postgres',password='FD1ns81g02!',port='5050'"

conn = psycopg2.connect(
    host="127.0.0.1",
    database='module 2.1',
    user='postgres',
    password="FD1ns81g02!",
    # port='5050'
)
cursor = conn.cursor()

query = """ insert into moderator
            values ('anonymous','Gouda', '10:04','10-23-23', 'TRUE');   
            insert into zuiltext 
            values ('anonymous','Gouda','hi', '10-23-23', '10:04'); """

cursor.execute(query)
conn.commit()
conn.close()



