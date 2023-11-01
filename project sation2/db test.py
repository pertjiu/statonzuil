import re
import datetime

with open('gev stationzeill.txt', 'r') as file:
    text = file.read()

pattern = r'-(.*?)-'
sentences = re.findall(pattern, text)

checklist = []
checklist.append(sentences)







stationberichtinfo = []

stationberichtinfo.append(sentences)


flattened_list = [item for sublist in stationberichtinfo for item in sublist]

dbgoedkeuring = []
moderatorname = input('name ')
moderatoremail = input('email ')

goedkeuring = input(f"please type Y/N if this is acceptable: {checklist} ")
if goedkeuring == 'Y':
    now = datetime.datetime.now()
    beordeelingD = str(now.strftime("%D"))
    beordeelingT = str(now.strftime("%T"))
    dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}")
    flattened_list.append(f'{beordeelingT}, {beordeelingD}, {goedkeuring}')
    print(dbgoedkeuring)
    print(flattened_list)
elif goedkeuring != 'Y':
    now = datetime.datetime.now()
    beordeelingD = str(now.strftime("%D"))
    beordeelingT = str(now.strftime("%T"))
    dbgoedkeuring.append(f"{moderatorname}, {moderatoremail}")
    flattened_list.append(f'{beordeelingT}, {beordeelingD}, {goedkeuring}')
    print(dbgoedkeuring)
    print(flattened_list)

result = [', '.join(flattened_list)]

# Print the result
print(result)




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




for record in result:
    query = """INSERT INTO bericht(naam, plaats, bericht, datum, tijd, gktijd, gkdatum, goedkeuring)
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, tuple(record.split(', ')))

    conn.commit()

conn.close()
with open('gev stationzeill.txt', 'w') as file:
    file.write('')