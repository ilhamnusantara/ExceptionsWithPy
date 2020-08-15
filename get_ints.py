import sys
def getInt(prompt):
    while True:
        try:
            angka = int(input(prompt))
            return angka
        # exception untuk inputan jika angka
        except ValueError:
            print("Anda memasukan bukan angka, coba kembali")
         # ecxeption bila di masuk ctrl + d / lainnya
        except EOFError:
            sys.exit(0)
        finally:
            print("Data yang dimasukkan benar dan dijalankan")
angka_awal = getInt("Masukan angka pertama = ")
angka_kedua = getInt("Masukan angka kedua = ")

try:
    print("{} dibagi dengan {} menjadi {}".format(angka_awal,angka_kedua, angka_awal / angka_kedua))
except ZeroDivisionError:
    print("Tidak bisa kamu bagi dengan nol")
    sys.exit(2)
else:
    print("pembagian yang dilakukan sukses")