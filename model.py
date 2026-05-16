import time

class AnalisisRealTime:
    def __init__(self):
        self.daftarWaktuKlik = []

    def InputAksiBaru(self):
        waktuSekarang = time.time()
        self.daftarWaktuKlik.append(waktuSekarang)

        self.daftarWaktuKlik = [t for t in self.daftarWaktuKlik if waktuSekarang - t < 3]

        return self.AnalisisPola()
    
    def AnalisisPola(self):
        jumlahAksi = len(self.daftarWaktuKlik)

        if jumlahAksi > 10: 
            return True, f"\u26A0\uFE0F ANOMALI!!! Terdeteksi {jumlahAksi} aksi dalam 3 detik!"
        else:
            return False, f"\u2705 {jumlahAksi} aksi dalam 3 detik"
        
#TES

if __name__ == "__main__":
    otak = AnalisisRealTime()
    print("simulasi, ketik ctrl+c untuk berhenti")

    try:
        while True:
            input("Enter")

            isAnomali, pesan = otak.InputAksiBaru()
            print(pesan) 

    except KeyboardInterrupt:
        print("\nselesai.") 
        