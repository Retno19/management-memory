#NAMA KELOMPOK
#5200411450 RETNO PRIHATINI
#5200411122 GRESSENSIA OLIVIA NENO A
#5200411343 PANDU TEJA S
#5200411347 MUHAMMAD SYARIFUDIN

print("----Kelompok 5----")
print("----Management Memory----")
RAM = float (input ("Masukan kapasitas RAM : "))
SisOP = float (input ("Masukan Sistem Operasi : "))
digunakan = float (input ("Masukan memori yang terpakai : "))

tidakterpakai = RAM - (SisOP + digunakan)

print ("RAM yang tak terpakai", tidakterpakai)