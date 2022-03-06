#import
from lib2to3.pgen2 import driver
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Person import Person
from Job import Job
from Driver import Driver

#--- isi data ---
#pekerjaan (job)
pekerjaan = []
##
pekerjaan.append(Job("12345", "AirAsia", "Pilot"))
pekerjaan.append(Job("54321", "LionAir", "Pilot"))
pekerjaan.append(Job("13579", "Sriwijaya", "Pilot"))
pekerjaan.append(Job("90876", "Oceania Queen", "Sailor"))
pekerjaan.append(Job("35678", "Samudera", "Sailor"))

#orang (person)
orang = [] #buat array
##isi array
orang.append(Person("123456789", "Lucas", True, pekerjaan[0]))
orang.append(Person("245671222", "Alice", False, pekerjaan[1]))
orang.append(Person("987654321", "Udin", True, pekerjaan[2]))
orang.append(Person("113355667", "Grigori", True, pekerjaan[3]))
orang.append(Person("222244444", "Sri", False, pekerjaan[4]))

#pengendara (driver)
pengendara = [] #buat array
##isi array
pengendara.append(Driver(orang[0], "P123", "10/10/2030", "Airplane"))
pengendara.append(Driver(orang[1], "P222", "1/1/2031", "Airplane"))
pengendara.append(Driver(orang[2], "P765", "3/4/2025", "Airplane"))
pengendara.append(Driver(orang[3], "S234", "6/12/2027", "Ship"))
pengendara.append(Driver(orang[4], "S334", "1/10/2029", "Ship"))

#Kendaraan
kendaraan = [] #buat array
##isi array
kendaraan.append(Vehicle("Aviation Kerosene", 50, pengendara[0]))
kendaraan.append(Vehicle("Aviation Kerosene", 90, pengendara[1]))
kendaraan.append(Vehicle("Aviation Kerosene", 70, pengendara[2]))
kendaraan.append(Vehicle("Marine Diesel Oil", 80, pengendara[3]))
kendaraan.append(Vehicle("Marine Diesel Oil", 120, pengendara[4]))
kendaraan.append(Vehicle("Aviation Kerosene", 80, pengendara[0]))
kendaraan.append(Vehicle("Aviation Kerosene", 75, pengendara[2]))
kendaraan.append(Vehicle("Marine Diesel Oil", 90, pengendara[3]))
kendaraan.append(Vehicle("Marine Diesel Oil", 100, pengendara[4]))
kendaraan.append(Vehicle("Marine Diesel Oil", 100, pengendara[3]))

#pesawat
pesawat = [] #buat array
##isi array
pesawat.append(Airplane(kendaraan[0], "Boeing 747", "2 Years Old", "50 Meter"))
pesawat.append(Airplane(kendaraan[1], "Airbus A350", "3 Years Old", "70 Meter"))
pesawat.append(Airplane(kendaraan[2], "Boeing 767-300F", "2 Years Old", "60 Meter"))
pesawat.append(Airplane(kendaraan[5], "Airbus B100", "3 Years Old", "60 Meter"))
pesawat.append(Airplane(kendaraan[6], "Airbus A12", "4 Years Old", "75 Meter"))

#kapal
kapal = [] #buat array
##isi array
kapal.append(Ship(kendaraan[3], "3 Years Old", "Cruise", "England"))
kapal.append(Ship(kendaraan[4], "4 Years Old", "Ferry", "Indonesia"))
kapal.append(Ship(kendaraan[7], "2 Years Old", "Cruise", "Egypt"))
kapal.append(Ship(kendaraan[8], "2 Years Old", "Cruise", "Indonesia"))
kapal.append(Ship(kendaraan[9], "5 Years Old", "Ferry", "Indonesia"))

#tampilkan
print("===============")
print("===== JOB =====")
for i in range(5):
    print("=== Job " + str(i+1))
    pekerjaan[i].showDetail()
    print("")

print("==================")
print("===== PERSON =====")
for i in range(5):
    print("=== Person " + str(i+1))
    orang[i].showDetail()
    print("")

print("==================")
print("===== DRIVER =====")
for i in range(5):
    print("=== Driver " + str(i+1))
    pengendara[i].showDetail()
    print("")

print("===================")
print("===== VEHICLE =====")
for i in range(5):
    print("=== Vehicle " + str(i+1))
    kendaraan[i].showDetail()
    print("")

print("====================")
print("===== AIRPLANE =====")
for i in range(5):
    print("=== Airplane " + str(i+1))
    pesawat[i].showDetail()
    print("")

print("================")
print("===== SHIP =====")
for i in range(5):
    print("=== Ship " + str(i+1))
    kapal[i].showDetail()
    print("")

print("")
print("== test move and sleep methods ==")
#hasil method move
kendaraan[0].Move()
pesawat[2].Move()
kapal[1].Move()
#hasil method sleep
orang[2].sleep()
pengendara[0].sleep()
