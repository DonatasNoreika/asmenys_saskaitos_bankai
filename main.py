from models import engine, Asmuo, Bankas, Saskaita
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("1 - įveskite vartotoją\n2 - įveskite banką\n3 - įveskite sąskaitą\n"))
    if pasirinkimas == 1:
        vardas = input("Įveskite vardą")
        pavarde = input("Įveskite pavardę")
        asmens_kodas = int(input("Įveskite asmens kodą"))
        el_pastas = input("Įveskite el. pašto adresą")
        asmuo = Asmuo(vardas=vardas, pavarde=pavarde, asmens_kodas=asmens_kodas, el_pastas=el_pastas)
        session.add(asmuo)
        session.commit()
    if pasirinkimas == 2:
        pavadinimas = input("Įveskite banko pavadinimą")
        adresas = input("Įveskite adresą")
        banko_kodas = input("Įveskite banko kodą")
        swift_kodas = input("Įveskite SWIFT kodą")
        bankas = Bankas(pavadinimas=pavadinimas, adresas=adresas, banko_kodas=banko_kodas, swift_kodas=swift_kodas)
        session.add(bankas)
        session.commit()
    if pasirinkimas == 3:
        numeris = input("Įveskite sąskaitos numerį")
        balansas = 0
        vartotojai = session.query(Asmuo).all()
        for vartotojas in vartotojai:
            print(vartotojas)
        vartotojo_id = int(input("Pasirinkite vartotojo ID"))
        bankai = session.query(Bankas).all()
        for vienas in bankai:
            print(vienas)
        banko_id = int(input("Pasirinkite banko ID"))
        saskaita = Saskaita(numeris=numeris, balansas=balansas, asmuo_id=vartotojo_id, bankas_id=banko_id)
        session.add(saskaita)
        session.commit()