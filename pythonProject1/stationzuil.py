while True:  # zo lang dit klopt
    message = str(input("would you like to leave a message. if so please type yes "))
    if message != str('yes'):
        # als dit niet gelijk aanelkaar is dan repeat hij de statment daar boven weer  wegens de continue functie
        continue
    else:
        name = str(input('what is your name? if the name that is chosen is NON it will become anonymous '))
    break

true_message = str(input('than please leave a massage '))
# het idee hier is om de naam op te slaan samen met ze uitspraak de message
# alleen daarvoor is waarschijnlijk een database handig
#  nee = ('non', 'NON')
#  if name == str(nee)
# save the name anonymous
#  else :
# save the name input
# save massage next to the name
