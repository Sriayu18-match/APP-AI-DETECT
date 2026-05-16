# 🛡️ AI Cybersecurity Defense Dashboard (Streamlit Engine)

Folder ini merupakan subsistem **Dashboard Pemantauan Utama** yang berfungsi sebagai pusat kendali visual (*Command Center*) untuk mendeteksi serangan siber secara real-time. 

## 🛠️ Spesifikasi Teknologi & Desain Antarmuka
- **Framework Utama:** **Streamlit** (Python-based data application framework).
- **Desain Estetika:** Kustomisasi visual tingkat lanjut menggunakan injeksi **HTML/CSS** mentah untuk menciptakan tampilan bernuansa *Dark-Mode Cyber Defense Command Center*.
- **Manajemen Data:** Menggunakan pustaka `pandas` untuk pelacakan riwayat fluktuasi jaringan (*Ingress Velocity*) secara berkala.

## 📁 Penjelasan Berkas Utama
- `app.py`: Berkas kode utama yang memuat konfigurasi halaman, gaya antarmuka, logika metrik, dan grafik pemantauan real-time.
- `requirements.txt`: Daftar pustaka Python wajib (mengandalkan `streamlit` dan `pandas`).

## ⚙️ Mekanisme & Logika Deteksi AI (Rate Limiting)
Sistem ini memantau aktivitas berdasarkan algoritma *Rate Limiting* yang dirancang untuk mendeteksi serangan klasifikasi perilaku login secara real-time:
1. **Kategori NORMAL:** Jika frekuensi login **kurang dari atau sama dengan 10 kali percobaan** dalam kurun waktu **di bawah 3 detik** (`<=10 / <3s`).
2. **Kategori ANOMALI (Brute Force):** Jika terdeteksi aktivitas mencurigakan berupa **lebih dari 10 kali percobaan** dalam kurun waktu **di bawah 3 detik** (`10+ / <3s`). Sistem akan langsung melabelinya sebagai serangan Siber (*Cyber Attack*), memicu status **SYSTEM ATTACK**, mengubah warna indikator menjadi merah menyala, menurunkan skor kesehatan global, dan menampilkan bar peringatan bahaya (*Status Alert Bar*).

## 📡 Rencana Integrasi Tahap Akhir (Google AI Studio & Arduino)
Modul simulasi data ini akan digantikan dengan pipa komunikasi data riil yang terintegrasi penuh:
1. **Analisis AI via Google AI Studio:** Dashboard akan membaca status deteksi keamanan cerdas yang diproses oleh AI Engine luar menggunakan pemrosesan bahasa alami dari **Gemini API (Google AI Studio)** untuk mengenali perilaku serangan *Brute Force*.
2. **Koneksi Arduino (Hardware Trigger):** Kode di `app.py` dashboard ini akan diintegrasikan dengan pustaka `pyserial`. Begitu Gemini AI mengembalikan keputusan status `ATTACK/ANOMALI`, Python akan langsung menembakkan sinyal byte `'A'` lewat kabel USB untuk mengaktifkan **LED merah dan alarm Buzzer fisik** pada papan **Arduino**.

## 🕹️ Skenario Demonstrasi Serangan (Live Demo Plan)
Proyek ini dipersiapkan untuk mendemonstrasikan dua skenario perilaku interaksi pada Gerbang Login secara kontras:
1. **Skenario Manusia (Normal Behavior):** Interaksi login manual oleh pengguna dengan laju request rendah, menghasilkan status **SYSTEM NORMAL** pada dashboard.
2. **Skenario Serangan (Brute Force Simulation):** Simulasi serangan siber menggunakan script otomatisasi yang membanjiri gerbang login dengan laju ketukan tinggi (`10+ request / <3 detik`). Pola anomali ini akan memicu alarm pada dashboard dan mengaktifkan output fisik **Arduino** secara instan.
