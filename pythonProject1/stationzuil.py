while True:
    message = str(input("would you like to leave a message. if so please type yes "))
    if message != str('yes'):
        continue
    else:
        name = str(input('what is your name? if the name that is chosen is NON it will become anonymously '))
        break
