import os
import random
import string

data = dict()

while True:
    os.system("cls")  
    print("DATA CUACA".center(50, '🌤'))
    print("=" * 97)

    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(5))
    tanggal = input("Tanggal\t\t: ")
    kota = input("Kota\t\t: ")
    cuaca = input("Cuaca\t\t: ")
    suhu_tertinggi = input("Suhu Tertinggi\t: ")
    suhu_terendah = input("Suhu Terendah\t: ")

    data[keyFinal] = {
        'tanggalkey': tanggal,
        'kotakey': kota,
        'cuacakey': cuaca,
        'suhutertinggikey': suhu_tertinggi,
        'suhuterendahkey': suhu_terendah
    }

    opsi = input("Input data lagi (y/t) : ").lower()
    if opsi == 't':
        break

print("-" * 97)
print(f"{'Key':<7} {'Tanggal':<20} {'Kota':<15} {'Cuaca':<15} {'Suhu Tertinggi':<20} {'Suhu Terendah':<15} ")
print("-" * 97)

for key, value in data.items():
    print(f"{key:<7} {value['tanggalkey']:<20} {value['kotakey']:<15} {value['cuacakey']:<15} {value['suhutertinggikey']:<20} {value ['suhuterendahkey']:<15}")