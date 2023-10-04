import builtins
import collections
import sys
import traceback

"""
Programming
Final assignment: Bagagekluizen
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""


def aantal_kluizen_vrij():




def nieuwe_kluis():
    """
    Indien er nog kluizen vrij zijn, moet de gebruiker de mogelijkheid krijgen
    om een kluiscode in te voeren. Deze kluiscode moet uit minimaal 4 tekens bestaan,
    en de puntkomma (';') mag er niet in voorkomen.

    Als de kluiscode ongeldig is, is de returnwaarde van deze functie -1.
    Als er geen vrije kluizen meer zijn, is de returnwaarde van deze functie -2.

    Als er nog vrij kluizen zijn, en de kluiscode is geldig, dan koppelt deze functie
    de kluiscode aan een nog beschikbare kluis, en schrijft deze combinatie weg naar
    een tekstbestand. De returnwaarde van de functie is dan gelijk aan het toegekende
    kluisnummer.

    Returns:
        int: het toegekende kluisnummer of foutcode -1 of -2
    """
    return print('hello')


def kluis_openen():
    """
    Laat de gebruiker een kluisnummer invoeren, en direct daarna de bijbehorende
    kluiscode. Indien deze combinatie voorkomt in het tekstbestand met de kluizen
    die in gebruik zijn, is het resultaat van de functie True, anders False.

    Returns:
        bool: True als de ingevoerde combinatie correct is, anders False
    """
    return


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


def development_code():
    # Breid deze code uit om het keuzemenu te realiseren:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")


def module_runner():
    development_code()  # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()       # Comment deze regel om de HU-tests uit te schakelen


hello = int((input(
        '1 ik wil weten hoeveel kluizen nog vrij zijn \n'
        '2 ik wil een nieuwe kluis \n'
        '3 ik wil even iets uit mijn kluis halen \n'
        '4 ik geef mijn kluis terug \n')))
if hello <= 1:
    aantal_kluizen_vrij()