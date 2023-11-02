from tkinter import *
import psycopg2


conn = psycopg2.connect(
        host="20.77.182.19",
        database='stationszuil',
        user='postgres',
        password="FD1ns81g02!!"
    )
cursor = conn.cursor()

query = """ SELECT bericht
            FROM bericht ORDER BY bericht_id DESC
            LIMIT 5; """
cursor.execute(query)
rows = cursor.fetchall()


for row in rows:
    print(row[0])
conn.close()










root = Tk()

root.geometry("500x500")
for row in rows:
    label = Label(master=root, text=f'{row[0]}', font= ('NS Sans Regular', 60),
                foreground='#003082')
    label.pack()
root.mainloop()