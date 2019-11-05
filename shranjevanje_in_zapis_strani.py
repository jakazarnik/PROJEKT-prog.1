import json
import re
import requests
import orodja

url = 'https://www.studentska-prehrana.si/sl/restaurant'

def shrani_stran():
    orodja.shrani_spletno_stran(url, 'restavracije.html')

def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, 'r', encoding='utf-8') as r:
        return r.read()

def restavracije_loceno(ime_datoteke):
    vsebina_strani = vsebina_datoteke(ime_datoteke)
    vzorec = r'<div class="row restaurant-row.*">$'
    return re.findall(vzorec, vsebina_strani, flags=re.DOTALL)
