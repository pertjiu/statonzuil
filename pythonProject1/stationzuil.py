import time
import datetime
import random

while True:
    message = str(input("would you like to leave a message. if so please type yes "))
    if message != str('yes'):
        print('have a nice day')
        time.sleep(3)
        continue
    else:
        time.sleep(1)
        name = str(input('what is your name? if the name that is chosen is N it will become anonymous '))
    nee = ('n', 'N')
    user = [name]
    if name in nee:
        user[0] = "anonymous"
    else:
        user[0] = str(name)
    while True:
        time.sleep(1)
        true_message = str(input('than please leave a massage of max 140 letters '))
        if len(true_message) > 140:
            print('that is more than 140 letters')
            time.sleep(1)
            print("please type it again")
            time.sleep(2)
            continue
        else:
            time.sleep(1)
            print('thanks for leaving a massage and have a nice travel')
            time.sleep(2)
        break

    smassage = ["placeholder"]
    smassage[0] = str(true_message)

    now = datetime.datetime.now()
    cdt = [0]
    cdt[0] = str(now.strftime("%D %T"))
    print(cdt)

    infile = open("C:\\Users\dunca\PycharmProjects\stations.txt", "r")
    content = infile.read()
    infile.close()

    wordlist = content.split()
    station = [0]
    station[0] = str(random.choice(wordlist))

    outfile = open("C:\\Users\dunca\PycharmProjects\gev stationzeill.txt", 'a')
    outfile.write(str(user))
    outfile.write(str(smassage))
    outfile.write(str(cdt))
    outfile.write(str(station) + '\n')
    outfile.close()
    continue

