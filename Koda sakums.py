import math # nepieciesams, lai veiktu matematiskas darbibas

def tapesu_izmaksa(cena, tapesu_dati, telpas_dati):                                 # define funkciju
    sienu_laukums = 2 * (telpas_dati['platums'] + telpas_dati['garums']) * 2.5      # aprekina sienas laukumu
    
    rulli_skaits = 0
    for rullis in tapesu_dati:
        rulla_laukums = rullis[0] * rullis[1]                                       # aprekina rulla laukumu
        rulli_skaits += math.ceil(sienu_laukums / rulla_laukums)                    # mainigais ‘rulli skaits’ vajadzigs, lai aprekinatu izmaksu
    
    izmaksa = rulli_skaits * cena                                                   # aprekina izmaksu 
    return izmaksa