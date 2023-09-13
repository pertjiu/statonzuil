import time

while True:  # zo lang dit klopt
    message = str(input("would you like to leave a message. if so please type yes "))
    if message != str('yes'):
        # als dit niet gelijk aanelkaar is dan repeat hij de statment daar boven weer  wegens de continue functie
        print('have a nice day')
        time.sleep(1)
        continue
    else:
        name = str(input('what is your name? if the name that is chosen is N it will become anonymous '))
    nee = ('n', 'N')
    # if name == nee :
    # save name als anonymous
    # else:
    # save given name
    while True:
        true_message = str(input('than please leave a massage of max 140 letters '))
        if len(true_message) > 10:
            print('that is more than 140 letters')
            time.sleep(1)
            print("please type it again")
            time.sleep(2)
            continue
        else:
            print('thanks for leaving a massage and have a nice travel')
            time.sleep(2)
        break
    continue
# het idee hier is om de naam op te slaan samen met ze uitspraak de message plus de tijd en datum van de message
    # alleen daarvoor is waarschijnlijk een database handig

# dit vertraagt het moment van de print functie naar de continue functi


