"""
Lag en kort adjektivfortelling som tar imot input fra bruker
Hva er adjektiver?
 - Beskrivende ord, eks. vakre, grønne, barske, stilfulle,

 Eksempel på adjektivhistorie, kilde bursdagsjentene.no:

 Nå sitter vi ved det ………. spisebordet til den ……….
 familien til den ………. Henrik.
 Han har invitert alle de ……….
 vennene sine hit i dag bare fordi han fyller……….10 år.
 Her sitter altså den ………. Erik  og han tror han er en ………. gutt.

hint: du må ha like mange input-variabler som det er markeringer som ....
      husk komma mellom setninger med tødler og variabler i print
"""

#vi må ha 7 inputvariabler

input_en = input("Første adjektiv\n")
input_to = input("andre adjektiv\n")
input_tre = input("Tredje adjektiv\n")
input_fire = input("Fjerde adjektiv\n")
input_fem = input("Femte adjektiv\n")
input_seks = input("Sjette adjektiv\n")
input_syv = input("Syvende adjektiv\n")
print("Nå sitter vi ved det" , input_en ,"spisebordet til den",input_to,
    "familien til den",input_tre, "Henrik.", "Han har invitert alle de", input_fire ,
    "vennene sine hit i dag bare fordi han fyller", input_fem,
     "10 år. Her sitter altså den",input_seks,
     "Erik og han tror han er en", input_syv, "gutt." )
