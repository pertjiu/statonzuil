import random
# infile = open("kluisgegeven.txt", "r")
# content = infile.read()
# textcontent = content.split('\n')
# infile.close()

user = str(input('kluisnummer '))
ww = str(input('wachtwoord '))


with open("kluisgegeven.txt", "r") as file:
    content = file.readlines()

klnr = []
for line in content:
    klnr.append(line.strip().split(';'))


print(klnr)

for check in klnr:
    if check[0] == user and check[1] == ww:
        print(check[0] == user and check[1] == ww) # hier return true

for check2 in klnr:
    if check2[0] == user and check2[1] == ww:
      return print(check2[0] != user and check2[1] != ww)










