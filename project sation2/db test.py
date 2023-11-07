import datetime
import psycopg2

"""hier ord er gecheckt naar het bericht of het goedgekeurd mag worden. eerst word het txt bestand weer geopend
 en wordt de informatie gesplit en gestript zodat het makkelijker word om uittelezen en of te bewerken. dan wordt er 
 een funcite gedaan die vraagt naar de moderator naam en email waarbij eisen zijn en word er direct gecheckt in de database
 of deze email al bestaat bestaat hij niet word er een nieuwe id toegekent bestaat hij al wel word de oude opgehaald
 dan word het bericht verder uitgelezen en een voor een gedisplayed waarbij de moderator y/n kan type voor goedkeuring
 en als alle berichten zijn geweest word het weggeschreven naar de database en het txt berstand geleegt"""



with open('gev stationzeill.txt', 'r') as file:
    text = file.read()


sentences = text.split('|')
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

result = []
dbgoedkeuring = []

moderatorname = input('name ')
moderatoremail = input('email ')
while moderatorname == '':
    moderatorname = input('name ')
while moderatoremail == '' or "@" not in moderatoremail:
    moderatoremail = input('email ')


dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}")

for record in dbgoedkeuring:
    pass

conn = psycopg2.connect(
    host="20.77.182.19",
    database='stationszuil',
    user='postgres',
    password="FD1ns81g02!!"
)
cursor = conn.cursor()

query = """SELECT moderator_id, E_mail
               FROM moderator;"""
cursor.execute(query)
rows = cursor.fetchall()

email_list = [email for _, email in rows]

conn.close()

conn = psycopg2.connect(
            host="20.77.182.19",
            database='stationszuil',
            user='postgres',
            password="FD1ns81g02!!"
        )
if moderatoremail in email_list:
    pass
else:
    for record in dbgoedkeuring:
        cursor = conn.cursor()
        query = """
            INSERT INTO moderator (naam, E_mail)
            VALUES (%s, %s);"""
        cursor.execute(query, tuple(record.split(', ')))
    conn.commit()
    conn.close()


conn = psycopg2.connect(
    host="20.77.182.19",
    database='stationszuil',
    user='postgres',
    password="FD1ns81g02!!"
)
cursor = conn.cursor()

query = """SELECT moderator_id, E_mail
           FROM moderator;"""
cursor.execute(query)
rows = cursor.fetchall()


email_to_moderator_id = {email: moderator_id for moderator_id, email in rows}

if moderatoremail in email_to_moderator_id:
    moderator_id = email_to_moderator_id[moderatoremail]
    print(f"your Moderator ID is: {moderator_id}")
else:
    pass

conn.close()

for sentence in sentences:
    parts = sentence.split('--')
    if len(parts) == 5:
        name, place, message, date, time = parts
        print(f"Sentence:")
        print(f"Name: {name}")
        print(f"Place: {place}")
        print(f"Message: {message}")
        print(f"Date: {date}")
        print(f"Time: {time}")


        goedkeuring = input(f"Please type Y/N if this is acceptable: ")


        now = datetime.datetime.now()
        beordeelingD = now.strftime("%D")
        beordeelingT = now.strftime("%T")
        result.append(f'{name}, {place}, {message}, {date}, {time}, {beordeelingT}, {beordeelingD}, {goedkeuring}, {moderator_id}')

conn = psycopg2.connect(
    host="20.77.182.19",
    database='stationszuil',
    user='postgres',
    password="FD1ns81g02!!"
)
cursor = conn.cursor()

for record in result:
    query = """INSERT INTO bericht(naam, plaats, bericht, datum, tijd, gktijd, gkdatum, goedkeuring, moderator_id)
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, tuple(record.split(', ')))

    conn.commit()
conn.close()

with open ('gev stationzeill.txt', 'w') as file:
    file.write(' ')
