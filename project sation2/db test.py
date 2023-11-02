import datetime
import psycopg2


with open('gev stationzeill.txt', 'r') as file:
    text = file.read()


sentences = text.split('|')
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

result = []
dbgoedkeuring = []
moderatorname = input('name ')
moderatoremail = input('email ')

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
        dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}")
        result.append(f'{name}, {place}, {message}, {date}, {time}, {beordeelingT}, {beordeelingD}, {goedkeuring}')

for record in dbgoedkeuring:
    print(record)

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

for record in result:
    query = """INSERT INTO bericht(naam, plaats, bericht, datum, tijd, gktijd, gkdatum, goedkeuring)
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, tuple(record.split(', ')))

    conn.commit()
conn.close()

with open ('gev stationzeill.txt', 'w') as file:
    file.write(' ')