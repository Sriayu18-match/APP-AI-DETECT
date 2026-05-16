# 🧠 AI Engine - Real-Time Behavior Pattern Analyzer

Folder ini merupakan jantung dari sistem keamanan siber yang berfungsi sebagai **Mesin Penganalisis Pola Perilaku** secara real-time untuk mengklasifikasikan aktivitas akses pengguna.

## 🛠️ Spesifikasi Teknologi & Algoritma
- **Bahasa Pemrograman:** Python murni (tanpa antarmuka grafis / CLI-based process).
- **Algoritma Utama:** *Sliding Window Rate Limiting* menggunakan pelacakan stempel waktu dinamis (`time.time()`).

## 📁 Penjelasan Berkas Utama
- `main_ai.py` (atau `app.py`): Berkas logika utama yang memuat kelas penganalisis pola ketukan masuk dan simulasi pengujian interaksi lewat baris perintah terminal.

## ⚙️ Logika Kerja Algoritma (Sliding Window)
Mesin ini bekerja dengan metode pemantauan dinamis berbasis jendela waktu 3 detik:
1. **Perekaman Stempel Waktu (Timestamping):** Setiap kali ada aksi masuk (klik tombol login), sistem akan mencatat waktu presisi dalam milidetik dan memasukkannya ke dalam daftar riwayat aktivitas (`daftarWaktuKlik`).
2. **Pembersihan Data Kedaluwarsa:** Sistem secara otomatis menghapus semua stempel waktu yang usianya sudah lebih lama dari 3 detik dari waktu saat ini agar penggunaan memori tetap efisien.
3. **Klasifikasi Pola:**
   - **NORMAL (False):** Jika jumlah stempel waktu aktif di dalam daftar masih berada di bawah atau sama dengan 10 kali percobaan.
   - **ANOMALI/BRUTE FORCE (True):** Jika jumlah stempel waktu aktif menembus angka di atas 10 kali dalam kurun waktu 3 detik (`jumlahAksi > 10`).

## 📡 Rencana Penerapan Google AI Studio & Komunikasi Data
Pada tahap integrasi akhir, fungsi pengujian berbasis ketukan tombol Enter (`input("Enter")`) ini akan ditingkatkan menjadi sistem otomasi cerdas:
1. **Penerimaan Data:** Modul ini akan bertindak sebagai *background service* yang terus memantau pipa data (SQLite) dari Folder Login Site.
2. **Pengayaan Analisis via Gemini API:** Selain hitungan matematika laju ketukan ini, data teks log akan diteruskan ke **Google AI Studio (Gemini API)** untuk mendapatkan analisis kontekstual yang lebih mendalam mengenai tingkat bahaya serangan.
3. **Penyebaran Status:** Hasil keputusan klasifikasi dari mesin ini akan ditulis kembali ke database agar dashboard admin dapat membaca status terbaru dan memicu alarm **Arduino**.
