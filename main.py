from models import engine, Asmuo
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