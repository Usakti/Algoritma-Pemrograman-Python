"""
@Materi: File Handling & File Processing
@Judul: Praktikum 9 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

# Create & Write File
def writeFile(data, file):
    fileWrite = open(file, "w")
    fileWrite.write(data)
    fileWrite.close()

# Read File
def readFile(file):
    fileRead = open(file, "r")
    text = fileRead.read()
    print(text)
    fileRead.close()

# Add Text
def addText(data, file):
    file = open(file, "a")
    file.write(data)
    file.close()

def main():
    F = False
    while(not F):
        banner()
        pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4): "))
        if(pilihan == 1):
            namaFile = input("Masukkan Nama File: ")
            file = namaFile + ".txt"
            nama = input("Masukkan Namamu: ")
            nim = input("Masukkan NIM kamu: ")
            angkatan = input("Masukkan tahun angkatanmu: ")
            text = "Nama: " + nama + "\nNIM: " + nim + "\nAngkatan: " + angkatan
            print("\n")
            writeFile(text, file)
            print("File Berhasil Dibuat")
            print("\n")
        elif(pilihan == 2):
            namaFile = input("Masukkan Nama File: ")
            file = namaFile + ".txt"
            print("\n")
            readFile(file)
            print("\n")
        elif(pilihan == 3):
            namaFile = input("Masukkan Nama File: ")
            file = namaFile + ".txt"
            namaTeman = input("Masukkan Nama Sahabatmu: ")
            catatan = input("Masukkan Catatan Tambahan kamu: ")
            text = "\nNama Sahabat: " + namaTeman + "\nCatatan: " + catatan
            print("\n")
            addText(text, file)
            print("Data Berhasil Ditambahkan")
            print("\n")
        elif(pilihan == 4):
            print("Terima Kasih Sudah Menggunakan Program Saya")
            F = True
        else:
            print("Masukkan Angka yang sesuai dengan yang ada di Menu!")
            print("\n")

def banner():
    print("===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program\n")

main()