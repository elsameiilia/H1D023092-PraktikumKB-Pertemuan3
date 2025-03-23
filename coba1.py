#ini adalah komentar satu baris
print("Hello world!") #Ini juga komentar

'''
Ini adalah komentar multi baris
bagian ini tidak akan dieksekusi oleh program
'''

x = 11

name = input("Masukkan nama kamu: ")
print("Nama:", name)

universitas = "Unsoed"
print("Saya berkuliah di", universitas)
print(f"Saya berkuliah di {universitas}")
print("Saya berkuliah di {}.".format(universitas))

umur = int(input("Masukkan umur:" ))

if umur>=15:
    print ("Nama saya", name)
else:
    print ("Nama saya bukan", name)

nim = ["H1D023026", "H1D023086", "H1D023088", "H1D023092"] 
for i in nim:
    print(i)

countdown = 1
while countdown <= umur:
    if countdown == 18:
        print(name, "sudah dewasa!")
        break    
    print(countdown)
    countdown +=1
    