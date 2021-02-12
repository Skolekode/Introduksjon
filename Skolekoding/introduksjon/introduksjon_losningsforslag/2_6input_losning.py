"""
Hittil har vi hovedsaklig sett på å lese tekst fra bruker.
En annen datatype vi bruker mye er heltall, kalt int i Python.

input funksjonen forventer i hovedsak å lese tekst, men vi kan velge
at python skal prøve å lese det som heltall med funksjonen int().

Eksempel:
tall_fra_bruker = int(input("Skriv et heltall"))

Oppgave: Legge sammen
Ta to tall fra en bruker og legg dem sammen.
"""

tall_fra_bruker_en = int(input("Skriv et heltall"))
tall_fra_bruker_to = int(input("Skriv et heltall til"))

print("Sum av heltallene er : ", tall_fra_bruker_en + tall_fra_bruker_to)
