import math # nepieciesams, lai veiktu matematiskas darbibas

def tapesu_izmaksa(cena, tapesu_dati, telpas_dati):                                 # define funkciju
    sienu_laukums = 2 * (telpas_dati['platums'] + telpas_dati['garums']) * 2.5      # aprekina sienas laukumu
    
    rulli_skaits = 0
    for rullis in tapesu_dati:
        rulla_laukums = rullis[0] * rullis[1]                                       # aprekina rulla laukumu
        rulli_skaits += math.ceil(sienu_laukums / rulla_laukums)                    # mainigais ‘rulli skaits’ vajadzigs, lai aprekinatu izmaksu
    
    izmaksa = rulli_skaits * cena                                                   # aprekina izmaksu 
    return izmaksa

# Saraksts ar tapesu datiem
 
tapesu_dati = [
    [float(input("Ievadi pirma tapesu rulla garumu (metri): ")), float(input("Ievadi  pirma tapesu rulla platumu (metri): "))],    # pieprasa ievadit mainigajiem skaitu 
    [float(input("Ievadi otra tapesu rulla garumu (metri): ")), float(input("Ievadi otra tapesu rulla platumu (metri): "))]
]

# Vardnica telpas datiem 

telpas_dati = {
    'platums': float(input("Ievadi telpas platumu (metri): ")),
    'garums': float(input("Ievadi telpas garumu (metri): "))
}

cena = float(input("Ievadi tapesu rulla cenu: "))

print("Kopejas tapesu izmaksas:")
print(f"{tapesu_izmaksa(cena, tapesu_dati, telpas_dati):.2f} EUR")              # izvada izmaksu pec ievaditajiem datiem