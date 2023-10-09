# infile = open("kluisgegeven.txt", "r")
# content = infile.read()
# textcontent = content.split('\n')
# infile.close()

def aantal_kluizen_vrij():
    infile = open('kluisgegeven.txt', 'r')
    kluisregels = len(infile.readlines())
    vrij = 12 - kluisregels
    return vrij


def nieuwe_kluis():
    kluizen = [i for i in range(1, 13)]
    # print(kluizen)
    with open('kluisgegeven.txt', 'r') as file:
        # content = file.readlines()
        for line in file:
            kluis = int(line.strip().split(';')[0])
            if kluis in kluizen:
                kluizen.remove(kluis)

    if kluizen:
        beschikbaar = kluizen[0]
        # print(beschikbaar)
    else:
        return int(-2)

    ww = input('wachtword van minimaal 4 tekens ')
    if len(ww) < 4 or ";" in ww:
        return int(-1)
    file.close()

    with open('kluisgegeven.txt', 'a') as file:
        gegevens = f'{beschikbaar};{ww}' + '\n'
        file.write(gegevens)
        return beschikbaar


def kluis_openen():
    f = open('kluisgegeven.txt', 'r')
    content = f.readlines()
    f.close()
    juistecode = False
    kluisnummer = int(input("Voer je kluisnummer in:"))
    kluiscode = int(input("Voer je kluiscode in:"))

    for line in content:
        if (str(kluisnummer)) + ";" + (str(kluiscode)) + "\n" == line:
            juistecode = True
    if juistecode == 1:
        print("Kluis is geopend")
    else:
        print("Je hebt verkeerde code ingevoerd")
        return
    return True


def kluis_teruggeven():
    """
    Laat de gebruiker een kluisnummer invoeren, en direct daarna de bijbehorende
    kluiscode. Indien deze combinatie voorkomt in het tekstbestand met de kluizen
    die in gebruik zijn, moet deze combinatie/regel uit het tekstbestand verwijderd
    worden.

    Als het lukt om de combinatie te vinden en te verwijderen, is het resultaat
    van de functie True, anders False.

    Returns:
        bool: True als er een kluiscombinatie verwijderd werd, anders False
    """
    return


hello = int((input(
    '1 ik wil weten hoeveel kluizen nog vrij zijn \n'
    '2 ik wil een nieuwe kluis \n'
    '3 ik wil even iets uit mijn kluis halen \n'
    '4 ik geef mijn kluis terug \n')))
if hello == 1:
    aantal_kluizen_vrij()
elif hello == 2:
    nieuwe_kluis()
elif hello == 3:
    kluis_openen()
elif hello == 4:
    pass
else:
    print("ERROR")
