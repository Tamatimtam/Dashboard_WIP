
---

# Proyek Dashboard Keuangan Gen Z (WIP - Work in Progress)

### Intinya Apa Sih Proyek Ini?

-   **Masalah Utama:** Dari data survei yang kita dapat, Generasi Z di Indonesia ternyata punya tingkat "kecemasan finansial" (*financial anxiety*) yang cukup terasa (rata-rata skor 2.62 dari 4). Mereka sering berhadapan dengan layanan keuangan digital dan godaan belanja impulsif.
-   **Solusi Kita:** Kita akan membangun sebuah **dashboard interaktif**. Dashboard ini bukan cuma menampilkan data, tapi juga memetakan apa saja *pemicu* kecemasan tersebut (misalnya: sifat impulsif, kurangnya perencanaan, atau kesadaran risiko) di berbagai segmen Gen Z (mahasiswa, pekerja, dll.) dan provinsi.
-   **Tujuannya:** Memberikan rekomendasi praktis yang bisa langsung diterapkan untuk membantu Gen Z mengelola keuangan lebih baik dan mengurangi kecemasan mereka.

---

### Panduan Memahami Proyek Ini (Step-by-Step)

Untuk kalian yang baru bergabung dan ingin paham alur pemikiran proyek ini dari awal sampai akhir, ikuti urutan membaca dokumen berikut. Ini cara termudah agar tidak *overwhelm*:

1.  **Baca Aturan Mainnya Dulu:**
    -   Buka file: `BOOKLET_STUDY_CASE_DA.txt`
    -   **Isinya apa?** Ini adalah panduan resmi dari panitia kompetisi. Di sini ada semua aturan, kriteria penilaian, dan batasan yang harus kita patuhi. Wajib dibaca biar kita tidak salah langkah.

2.  **Pahami Ide Besarnya dalam 1 Menit:**
    -   Buka file: `docs/pitch.md`
    -   **Isinya apa?** Ini adalah rangkuman super singkat (elevator pitch) dari proyek kita. Hanya 6-8 poin yang menjelaskan masalah, solusi, dan dampak yang ingin kita capai.

3.  **Selami Logika di Balik Ide Kita (Versi Non-Teknis):**
    -   Buka file: `docs/brainstorming_ideation.md`
    -   **Isinya apa?** Dokumen ini adalah versi lengkap dari *pitch* tadi, tapi ditulis dengan bahasa yang ramah untuk orang awam. Menjelaskan "kenapa" kita memilih ide ini, "siapa" target pengguna kita (persona), dan *insight* awal yang kita temukan dari data. Di sini juga ada penjelasan istilah-istilah teknis dengan bahasa sederhana.

4.  **Lihat Rancangan Dashboardnya:**
    -   Buka file: `docs/dashboard_panels.md`
    -   **Isinya apa?** Setelah tahu idenya, dokumen ini menjelaskan panel-panel apa saja yang akan ada di dashboard kita nanti. Misalnya, akan ada panel Peta Provinsi, Grafik Perbandingan, dll.

5.  **Lihat Contoh Visualisasinya:**
    -   Buka file: `notebooks/dashboard_panels_demo (copy 1).txt`
    -   **Isinya apa?** Ini adalah *notebook* (semacam coretan lab data science) yang berisi contoh visualisasi untuk setiap panel yang kita rancang. Jadi, kalian bisa dapat gambaran visualnya akan seperti apa.

---

### Struktur Folder & Penjelasannya

Berikut adalah peta dari *codebase* ini:

-   `docs/`
    -   Ini adalah **pusat pemikiran dan dokumentasi** proyek kita. Semua ide, analisis mendalam, dan presentasi singkat ada di sini.
-   `DATASET/`
    -   Berisi **data mentah** yang kita gunakan. Ada 3 file utama dari panitia: survei literasi finansial, profil Gen Z, dan indikator ekonomi regional.
-   `notebooks/`
    -   Ini adalah **"dapur" atau "lab"** tempat kita mengolah dan menganalisis data.
    -   `eda_extract.py` & `eda_report.json`: Ini adalah hasil dari **EDA** (dijelaskan di bawah). Intinya, ini adalah laporan "perkenalan" kita dengan data.
    -   `dashboard_panels_demo (copy 1).txt`: Seperti yang dijelaskan di atas, ini adalah demo visualisasi.
-   `index.html`, `styles.css`, `css/`, `js/`
    -   **PENTING:** Semua file ini adalah **template atau placeholder** untuk tampilan dashboard. Isinya **BELUM terhubung dengan data sama sekali**. Ini adalah kerangka antarmuka (UI) yang nanti akan kita isi dengan visualisasi data yang sesungguhnya. Jadi, jangan bingung kalau isinya masih data dummy (contoh).

---

### **PENTING & WAJIB DIBACA! (Disclaimer & Penjelasan Jargon)**

1.  **Apa itu EDA?**
    -   EDA adalah singkatan dari **Exploratory Data Analysis**. Anggap saja ini seperti proses "kenalan" pertama kali dengan data. Kita "intip" isinya, cari tahu ada data apa saja, apakah ada yang aneh (misalnya, data salah ketik), dan mencari pola-pola menarik sebagai bahan analisis lebih lanjut. Laporan hasil kenalan ini ada di `notebooks/eda_report.json`.

2.  **Keterbatasan & "PR" pada Data Kita:**
    -   **Kolom Pendapatan & Pengeluaran Berantakan:** Ini masalah terbesar kita. Data `Est. Monthly Income` dan `Est. Monthly Expenditure` formatnya bukan angka (misalnya, tertulis `< Rp2.000.000` atau `Rp2.000.001 – Rp4.000.000`). Akibatnya, kita belum bisa melakukan perhitungan matematis (seperti rata-rata atau rasio tabungan) secara akurat. Ini adalah PR besar yang harus kita selesaikan.
    -   **Bias Sampel Provinsi:** Data survei kita **tidak merata**. Sekitar 47% responden berasal dari Sumatera Barat. Artinya, *insight* yang kita dapat mungkin lebih mencerminkan kondisi di Sumbar daripada kondisi nasional. Ini harus kita sebutkan sebagai keterbatasan dalam laporan akhir.
    -   **Data Self-Report:** Karena ini data survei, ada kemungkinan jawaban responden tidak 100% akurat (mungkin ada yang menjawab lebih baik dari kenyataan, atau lupa).

3.  **Tampilan Dashboard Masih Placeholder:**
    -   Sekali lagi, `index.html` dan file-file terkaitnya hanyalah **purwarupa visual**. Animasi dan grafiknya belum merepresentasikan data asli kita.

---

### Cara Menjalankan Tampilan Dashboard (Lokal)

Jika kalian ingin melihat *template* visual dashboard di browser, ikuti langkah ini:

1.  Buka terminal atau command prompt.
2.  Arahkan ke folder `Dashboard_WIP`.
3.  Jalankan salah satu perintah berikut:

    ```bash
    # Jika ada Python 3
    python3 -m http.server 5173
    ```
4.  Buka browser dan akses alamat yang muncul di terminal (biasanya `http://localhost:5173`).

Semoga penjelasan ini membantu ya! Semangat