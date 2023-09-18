import time
import datetime


while True:
    message = str(input("would you like to leave a message. if so please type yes "))
    if message != str('yes'):
        print('have a nice day')
        time.sleep(1)
        continue
    else:
        name = str(input('what is your name? if the name that is chosen is N it will become anonymous '))
    nee = ('n', 'N')
    user = [name]
    if name in nee:
        user[0] = "anonymous"
        # print(user)
    else:
        user[0] = str(name)
        print(user)
    while True:
        true_message = str(input('than please leave a massage of max 140 letters '))
        if len(true_message) > 140:
            print('that is more than 140 letters')
            time.sleep(1)
            print("please type it again")
            time.sleep(2)
            continue
        else:
            print('thanks for leaving a massage and have a nice travel')
            time.sleep(2)
        break
    smassage = ["placeholder"]
    smassage[0] = str(true_message)

    now = datetime.datetime.now()
    cdt = [0]
    cdt[0] = str(now.strftime("%H:%M:%S %Y:%m:%d"))
    print(cdt)

    continue

