import time
import datetime
import random


while True:
    message = str(input("would you like to leave a message. if so please type yes "))
    if message != str('yes'):
        print('have a nice day')
        continue
    else:
        time.sleep(1)
        name = str(input(f"what is your name? if you give us the name N/n than it will become anonymous "))
    nee = ('n', 'N')
    # user = [name]
    if name in nee:
        name = "anonymous"
        time.sleep(1)
    else:
        time.sleep(1)
    while True:
        true_message = str(input('than please leave a massage of max 140 letters '))
        if len(true_message) > 140:
            print('that is more than 140 letters')
            time.sleep(1)
            print("please type it again")
            time.sleep(2)
            continue
        elif true_message == '-':
            print("please type it again the - symbole is not aloud")
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
    cdt = str(now.strftime("%D %T"))
    datum = str(now.strftime("%D"))
    tijd = str(now.strftime("%T"))
    # print(cdt)

    infile = open("stations.txt", "r")
    content = infile.read()
    infile.close()

    wordlist = content.split()
    station = str(random.choice(wordlist))

    stationberichtinfo = [f"{name}, {station}, {true_message}, {datum}, {tijd}"]

    outfile = open("gev stationzeill.txt", "a")
    hello = f"{name}--{station}--{true_message}--{datum}--{tijd}|" + '\n'
    outfile.write(hello)
    outfile.close()