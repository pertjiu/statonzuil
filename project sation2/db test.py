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


eerste_zin = True

stationberichtinfo = []
dbgoedkeuring = []
moderatorname = input('name ')
moderatoremail = input('email ')
for check in checklist:
    goedkeuring = input(f"please type Y/N if this is acceptable: {check} ")
    if goedkeuring == 'Y':
        now = datetime.datetime.now()
        beordeelingD = str(now.strftime("%D"))
        beordeelingT = str(now.strftime("%T"))
        dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}")
        stationberichtinfo.append(f'{beordeelingT}, {beordeelingD}, {goedkeuring}')
        print(dbgoedkeuring)
    elif goedkeuring != 'Y':
        now = datetime.datetime.now()
        beordeelingD = str(now.strftime("%D"))
        beordeelingT = str(now.strftime("%T"))
        dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}")
        stationberichtinfo.append(f'{beordeelingT}, {beordeelingD}, {goedkeuring}')
        print(dbgoedkeuring)








import psycopg2


conn = psycopg2.connect(
        host="20.77.182.19",
        database='stationszuil',
        user='postgres',
        password="FD1ns81g02!!"
    )
cursor = conn.cursor()

for record in dbgoedkeuring:
    query = """ 
                INSERT INTO moderator (naam, E_mail) 
                VALUES (%s, %s);"""
    cursor.execute(query, tuple(record.split(', ')))

    conn.commit()

for record in stationberichtinfo:
    query = """INSERT INTO bericht(naam, plaats, bericht, datum, tijd, gktijd, gkdatum, goedkeuring)
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, tuple(record.split(', ')))

    conn.commit()

conn.close()


