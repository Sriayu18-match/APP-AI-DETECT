# 🔑 Secure Login System (Frontend Authentication Interface)

Folder ini berisi subsistem **Gerbang Masuk Autentikasi (Frontend)** yang berfungsi sebagai antarmuka pengguna tempat data interaksi login akan direkam dan dipantau.

## 🛠️ Spesifikasi Teknologi & Desain
- **Framework Utama:** **Streamlit** (Python-based framework).
- **Desain Estetika:** Modifikasi penuh menggunakan injeksi **HTML/CSS** mentah untuk menciptakan tampilan form masuk yang modern, minimalis, dan bernuansa *Dark Theme Tech Studio*.
- **Task Runner:** Dikonfigurasi menggunakan automasi Node.js (`package.json`) untuk memudahkan eksekusi peluncuran server lokal pada port khusus (`port 3000`).

## 📁 Berkas-Berkas Komponen
- `app.py`: Berkas kode utama yang mengatur tampilan form input kredensial pengguna, kustomisasi gaya CSS, dan respons visual status masuk.
- `package.json`: Memuat skrip automasi untuk menjalankan server Streamlit serta dependensi pendukung seperti SDK Google GenAI.

## ⚙️ Skenario Pengujian Sistem (Live Attack Demo)
Subsistem ini dirancang sebagai wadah simulasi pengujian untuk menunjukkan kontras antara perilaku pengguna normal dan serangan siber secara langsung:
1. **Skenario Login Biasa (Manusia):** Pengguna memasukkan kredensial secara manual dengan laju ketukan rendah (`<=10 percobaan / <3 detik`). Pola interaksi ini akan dikategorikan sebagai aktivitas **NORMAL**.
2. **Skenario Serangan (Brute Force):** Gerbang login sengaja akan dibanjiri oleh percobaan masuk secara masif dan cepat dalam jendela waktu singkat (`10+ percobaan / <3 detik`). Pola lonjakan aktivitas ini akan diklasifikasikan sebagai **ANOMALI** (Serangan Brute Force) yang nantinya diteruskan ke pipa data analisis Google AI Studio dan memicu output fisik **Arduino**.
