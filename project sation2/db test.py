import re
import datetime

with open('gev stationzeill.txt', 'r') as file:
    text = file.read()

pattern = r'-(.*?)-'
sentences = re.findall(pattern, text)

checklist = []
for sentence in sentences:
    checklist = sentences
    print(sentence)

print(checklist)

#for i, item in enumerate(checklist, 1):
 #   print(f"{i}: {item}")

eerste_zin = True

dbgoedkeuring = []
moderatorname = input('name ')
moderatoremail = input('email ')
for check in checklist:
    goedkeuring = input(f"please type Y/N if this is acceptable: {check} ")
    if goedkeuring == 'Y':
        now = datetime.datetime.now()
        beordeelingD = str(now.strftime("%D"))
        beordeelingT = str(now.strftime("%T"))
        dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}, {beordeelingD}, {beordeelingT}, TRUE")
        print(dbgoedkeuring)
    elif goedkeuring != 'Y':
        now = datetime.datetime.now()
        beordeelingD = str(now.strftime("%D"))
        beordeelingT = str(now.strftime("%T"))
        dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}, {beordeelingD}, {beordeelingT}, FALSE")
        print(dbgoedkeuring)















import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='module 2.2',
        user='postgres',
        password="FD1ns81g02!"
    )
    cursor = conn.cursor()

    for record in dbgoedkeuring:
        query = """INSERT INTO moderator (naam, email, dbeordeeld, tbeordeeld, goedkeuring) 
                   VALUES (%s, %s, %s, %s, %s);"""
        cursor.execute(query, tuple(record.split(', ')))

        conn.commit()
except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()



