data_nilai = {
    'A': 4.0,
    'A-': 3.75,
    'B+': 3.5,
    'B': 3.0,
    'B-': 2.75,
    'C+': 2.5,
    'C': 2.0,
    'C-': 1.75,
    'D': 1.50,
    'E': 1.25
}

def hitung_rata(data_nilai):
    jumlah_nilai = 0
    jumlah_sks = 0
    while True:
        try:
            bobot = input('Masukkan Nilai: ').upper()
            if bobot == '':
                break
            elif bobot not in data_nilai:
                print('Nilai tidak valid')
                continue
            elif bobot in data_nilai:
                print(f'Nilai {data_nilai[bobot]} berhasil ditambahkan')
                jumlah_nilai += data_nilai[bobot]
                jumlah_sks += 1
        except ValueError:
            print('Terjadi kesalahan, silahkan coba lagi')
            continue

    if jumlah_nilai > 0:
        return jumlah_nilai / jumlah_sks


hasil = hitung_rata(data_nilai)
if hasil != None:
    print('Rata-rata nilai: ', hitung_rata(data_nilai))
