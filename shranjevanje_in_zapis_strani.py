import json
import re
import requests
import orodja

url = 'https://www.studentska-prehrana.si/sl/restaurant'

def shrani_stran(n):
    orodja.shrani_spletno_stran(url, 'restavracije.html')

ime_datoteke='restavracije.html'

def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, 'r', encoding='utf-8') as r:
        return r.read()

def restavracije_loceno(ime_datoteke):
    vsebina_strani = vsebina_datoteke(ime_datoteke)
    vzorec = (r'<div class="row restaurant-row(.*?)<div class="pull-right margin-right-10">')
    return re.findall(vzorec, vsebina_strani, flags=re.DOTALL)

vzorec_podatkov = re.compile(
    r'<div class="row restaurant-row'
    r'.*?data-naslov="(?P<Naslov>.*?)"'
    r'.*?data-cena="(?P<Cena>.*?)"'
    r'.*?data-doplacilo="(?P<Doplacilo>.*?)"'
    r'.*?data-posid="(?P<Posta>.*?)"'
    r'.*?data-lokal="(?P<Ime_lokala>.*?)"'
    r'.*?data-city="(?P<Mesto>.*?)"'
    #r'(.*?<input checked="checked".*?value="(?P<Ocena>.*?)")?'
    ,re.DOTALL
    )
vzorec_ocene = re.compile(r'checked="checked".*?value="(?P<ocena>.+?)".*?',
                          re.DOTALL)


def iskanje_podatkov_za_restavracije(ime_datoteke):
    seznam_ponudb = vsebina_datoteke(ime_datoteke)
    slovar_iskanih_podatkov = []
    stevec = 0
    for zadetek in re.finditer(vzorec_podatkov, seznam_ponudb):
        slovar_iskanih_podatkov.append(zadetek.groupdict())
        stevec +=1

    orodja.zapisi_csv(slovar_iskanih_podatkov, ['Naslov', 'Mesto', 'Doplacilo', 'Posta', 'Cena', 'Ime_lokala'], 'restavracije.csv')
    print(slovar_iskanih_podatkov)
    print(stevec)