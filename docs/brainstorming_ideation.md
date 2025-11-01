<style>
:root {
    --md-accent: #1457d2;
    --md-accent-light: #3b82f6;
    --md-text: #1e293b;
    --md-text-light: #475569;
    --md-muted: #64748b;
    --md-bg: #ffffff;
    --md-surface: #f8fafc;
    --md-surface-hover: #f1f5f9;
    --md-border: #e2e8f0;
    --md-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
    --md-shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

html, body {
    background: var(--md-bg);
    color: var(--md-text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    line-height: 1.75;
    font-size: 16px;
}

body {
    max-width: 900px;
    margin: 3rem auto;
    padding: 0 2rem;
}

h1, h2, h3, h4, h5, h6 {
    line-height: 1.3;
    color: #0f172a;
    font-weight: 700;
    letter-spacing: -0.02em;
}

h1 { 
    font-size: 2.5rem; 
    margin-top: 0;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 3px solid var(--md-accent);
}

h2 { 
    font-size: 1.875rem; 
    margin-top: 3rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--md-border); 
}

h3 { 
    font-size: 1.5rem; 
    margin-top: 2rem;
    margin-bottom: 0.75rem;
    color: #334155;
}

h4 {
    font-size: 1.25rem;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
    color: #475569;
}

p { 
    margin: 0.75rem 0 1.25rem; 
    color: var(--md-text-light); 
    font-size: 1.0625rem;
}

ul, ol { 
    padding-left: 1.75rem;
    margin: 1rem 0;
}

li { 
    margin: 0.5rem 0;
    color: var(--md-text-light);
    line-height: 1.7;
}

li::marker {
    color: var(--md-accent);
}

a { 
    color: var(--md-accent); 
    text-decoration: none;
    transition: color 0.2s ease;
    border-bottom: 1px solid transparent;
}

a:hover { 
    color: var(--md-accent-light);
    border-bottom-color: var(--md-accent-light);
}

strong {
    color: var(--md-text);
    font-weight: 600;
}

em {
    color: var(--md-text-light);
}

code {
    font-family: "Fira Code", "Cascadia Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.9em;
    background: #eef2ff;
    color: #5b21b6;
    padding: 0.2rem 0.4rem;
    border-radius: 0.25rem;
    font-weight: 500;
}

pre {
    background: linear-gradient(to bottom, #0f172a, #1e293b);
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
    box-shadow: var(--md-shadow-lg);
    border: 1px solid #334155;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    font-size: 0.9rem;
    font-weight: normal;
}

blockquote {
    margin: 1.5rem 0;
    padding: 1.25rem 1.5rem;
    background: var(--md-surface);
    border-left: 4px solid var(--md-accent);
    color: var(--md-text-light);
    border-radius: 0.25rem;
    box-shadow: var(--md-shadow);
    font-style: italic;
}

blockquote p {
    margin: 0.5rem 0;
}

blockquote p:first-child {
    margin-top: 0;
}

blockquote p:last-child {
    margin-bottom: 0;
}

hr { 
    border: 0; 
    border-top: 2px solid var(--md-border); 
    margin: 3rem 0; 
}

table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    margin: 1.5rem 0;
    border-radius: 0.5rem;
    box-shadow: var(--md-shadow);
    border: 1px solid var(--md-border);
}

th, td { 
    padding: 0.875rem 1rem; 
    text-align: left;
    border-bottom: 1px solid var(--md-border);
}

th { 
    background: linear-gradient(to bottom, #f8fafc, #f1f5f9);
    font-weight: 600;
    color: var(--md-text);
    border-bottom: 2px solid var(--md-border);
    position: sticky;
    top: 0;
}

tr:last-child td {
    border-bottom: none;
}

tbody tr {
    transition: background-color 0.15s ease;
}

tbody tr:hover {
    background-color: var(--md-surface-hover);
}

kbd { 
    background: linear-gradient(to bottom, #334155, #1e293b);
    color: #fff; 
    padding: 0.2rem 0.5rem; 
    border-radius: 0.25rem; 
    font-size: 0.875em;
    font-family: ui-monospace, monospace;
    box-shadow: 0 2px 0 0 #0f172a, 0 3px 0 0 rgba(0,0,0,0.2);
    border: 1px solid #0f172a;
}

.mark { 
    background: linear-gradient(to bottom, #fef08a, #fde047);
    padding: 0.1rem 0.3rem; 
    border-radius: 0.2rem;
    box-shadow: 0 0 0 2px rgba(250, 204, 21, 0.1);
}

.smallcaps { 
    font-variant: small-caps; 
    letter-spacing: 0.05em;
    font-weight: 500;
}

.header-note { 
    font-size: 1rem; 
    color: var(--md-muted); 
    margin-top: 0.5rem;
    font-weight: normal;
}

/* Improve readability for lists inside blockquotes */
blockquote ul, blockquote ol {
    margin-top: 0.75rem;
}

/* Better spacing for nested lists */
li > ul, li > ol {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    body {
        padding: 0 1.5rem;
        margin: 2rem auto;
    }
    
    h1 { font-size: 2rem; }
    h2 { font-size: 1.5rem; }
    h3 { font-size: 1.25rem; }
    
    pre {
        padding: 1rem;
        margin: 1rem -0.5rem;
    }
}
</style>

# 💡 Brainstorming & Ideasi – Panduan Lengkap (Versi Non-Teknis)

Halo teman-teman! 👋

Dokumen ini adalah pemandu wisata untuk proyek kita. Tujuannya sederhana: menjelaskan seluruh ide, data, dan rencana kita dengan bahasa yang mudah dimengerti, bahkan jika kamu belum pernah menyentuh data science sama sekali.

Jangan khawatir dengan istilah-istilah aneh, semua akan dijelaskan di sini.

**⏱️ Kalau kamu hanya punya 3 menit, baca ini:**

*   **🏆 "Harta Karun" kita:** Kita punya data dari 3 file CSV (seperti Excel) yang berisi jawaban survei dari 1.652 anak Gen Z di Indonesia. Isinya tentang kebiasaan finansial, tingkat pemahaman, dan perasaan cemas mereka soal uang.
*   **⚠️ Masalah yang kita temukan:** Angka menunjukkan bahwa Gen Z ini punya tingkat "kecemasan finansial" yang cukup nyata (skor rata-rata 2.62 dari 4). Pemicunya bukan cuma soal besar kecilnya gaji, tapi lebih ke kebiasaan belanja impulsif dan kurangnya perencanaan.
*   **🎯 Solusi yang kita tawarkan:** Sebuah **dashboard interaktif** yang berfungsi seperti "cermin finansial". Dashboard ini akan membantu pengguna (dan pemangku kepentingan seperti kampus atau pemerintah) untuk:
    1.  Melihat gambaran besar kondisi finansial Gen Z.
    2.  Mengidentifikasi apa saja pemicu utama kecemasan mereka.
    3.  Memberikan rekomendasi praktis yang bisa langsung dicoba.
*   **✨ Kenapa ini penting?** Karena kita tidak hanya menyajikan data, tapi mengubah data itu menjadi aksi nyata untuk membantu teman-teman kita mengelola keuangan dengan lebih tenang.

---

### 📦 Bagian 1: Perkenalan dengan "Harta Karun" Kita: Data CSV

Anggap saja tiga file CSV di folder `DATASET/` adalah harta karun kita. Isinya adalah suara dan cerita dari 1.652 anak Gen Z. Tapi seperti harta karun yang baru ditemukan, isinya masih sedikit berantakan dan perlu kita poles.

Mari kita bedah satu per satu:

#### 1. 📄 File: `GenZ_Financial_Literacy_Survey (copy 1).txt` & `GenZ_Financial_Profile (copy 1).txt`

*   **📋 Isinya Apa?**
    Kedua file ini isinya hampir sama persis, seperti fotokopian satu sama lain. Mereka adalah **inti dari proyek kita**. Di dalamnya ada jawaban detail dari 1.652 responden Gen Z tentang:
    *   **👤 Siapa Mereka (Demografi):** Jenis kelamin, asal provinsi, status tempat tinggal (kost, rumah orang tua), pendidikan terakhir, pekerjaan, status pernikahan, dan tahun lahir.
    *   **📚 Pemahaman Finansial Mereka (Literasi):** Pertanyaan seperti, "Apakah kamu bisa mengenali investasi yang bagus?" atau "Apakah kamu paham laporan keuangan?". Jawabannya dalam bentuk skala 1-4.
    *   **🛒 Kebiasaan Mereka (Perilaku):** Pertanyaan tentang kebiasaan sehari-hari, misalnya, "Apakah kamu suka berburu diskon?", "Apakah kamu sering belanja tanpa pikir panjang (impulsif)?", atau "Apakah kamu suka menawar harga?".
    *   **😰 Perasaan Mereka (Psikologi Finansial):** Ini bagian yang paling penting. Ada pertanyaan yang mengukur tingkat kecemasan finansial, seperti: "Apakah kamu merasa keuangan mengontrol hidupmu?" atau "Apakah kamu merasa tidak akan pernah bisa membeli barang yang kamu inginkan?".

*   **🔍 Kualitas Datanya Gimana?**
    *   **✅ Yang Bagus:** Sebagian besar jawaban skala 1-4 terisi lengkap. Ini bagus karena kita bisa mengukur sentimen mereka dengan cukup baik.
    *   **⚠️ Yang Berantakan (Ini PR Besar Kita):**
        1.  **💰 Kolom Gaji dan Pengeluaran Tidak Standar:** Ini masalah utama. Jawaban untuk `Est. Monthly Income` (Perkiraan Gaji Bulanan) dan `Est. Monthly Expenditure` (Perkiraan Pengeluaran Bulanan) ditulis dalam format teks yang berbeda-beda. Ada yang menulis `< Rp2.000.000`, ada yang `Rp2.000.001 – Rp4.000.000`, ada juga yang kosong. Komputer tidak bisa menghitung rata-rata dari teks seperti ini.
        2.  **⚧️ Data Gender Tidak Seragam:** Ada yang menulis "Female", "F", atau "Wanita". Begitu juga untuk "Male", "M", "Pria". Kita perlu menyeragamkannya agar bisa dikelompokkan dengan benar.
        3.  **🗺️ Data Provinsi Tidak Merata (Bias):** Hampir setengah dari responden (sekitar 47%) berasal dari **Sumatera Barat**. Ini artinya, hasil analisis kita mungkin lebih berat mencerminkan kondisi di sana. Kita harus jujur soal ini dan menyampaikannya sebagai keterbatasan.

*   **🧹 Perlu Dibersihkan?**
    **SANGAT PERLU.** Sebelum data ini bisa divisualisasikan dengan benar di dashboard, kita harus "merapikannya" terlebih dahulu. Misalnya, mengubah teks gaji menjadi angka (misalnya, rentang "1-3 juta" kita ambil nilai tengahnya yaitu 2 juta) dan menyeragamkan data gender.

#### 2. 📊 File: `Regional_Economic_Indicators (copy 1).txt`

*   **📋 Isinya Apa?**
    File ini berisi data pelengkap untuk setiap provinsi di Indonesia. Isinya tentang indikator ekonomi, seperti:
    *   Jumlah pinjaman online (pinjol) yang aktif.
    *   PDRB (Produk Domestik Regional Bruto): Sederhananya, ini adalah ukuran "kekayaan" atau "produktivitas ekonomi" suatu daerah.
    *   Tingkat Urbanisasi: Persentase penduduk yang tinggal di perkotaan.

*   **🔍 Kualitas Datanya Gimana?**
    Cukup bagus, tapi beberapa angka masih dalam format teks. Sama seperti file sebelumnya, perlu sedikit dibersihkan agar bisa diolah oleh komputer.

*   **📈 Untuk Apa Data Ini?**
    Data ini akan kita gunakan sebagai **konteks tambahan**. Misalnya, kita bisa membandingkan: "Apakah tingkat kecemasan finansial di provinsi dengan PDRB tinggi berbeda dengan provinsi yang PDRB-nya rendah?"

---

### 🔎 Bagian 2: Menemukan "Masalah Utama" dari Data

Setelah kita "mengobrol" dengan data melalui proses analisis (yang biasa disebut **EDA** atau *Exploratory Data Analysis*), kita menemukan beberapa benang merah yang membentuk **masalah utama**:

**🎯 Masalah Inti: Gen Z Indonesia Mengalami Kecemasan Finansial yang Nyata, dan Pemicunya Bukan Sekadar Uang.**

Mari kita pecah lebih dalam:

1.  **📈 Kecemasan Itu Ada dan Terukur.**
    Dari pertanyaan-pertanyaan yang mengukur perasaan cemas, kita membuat sebuah skor bernama `financial_anxiety_score` (skor kecemasan finansial) dengan skala 1 sampai 4. Rata-rata skor dari 1.652 responden adalah **2.62**.
    *   **💭 Artinya apa?** Skor ini tidak ekstrem, tapi menunjukkan adanya **kegelisahan tingkat sedang**. Mereka tidak panik, tapi juga tidak tenang. Perasaan seperti "gaji cuma numpang lewat" atau "cemas mikirin cicilan" itu nyata.

2.  **🔄 Pemicunya Bukan Cuma Gaji, Tapi Kebiasaan.**
    Awalnya kita mungkin berpikir, "cemas karena gajinya kecil". Tapi data menunjukkan sesuatu yang lebih dalam:
    *   **⚡ Sifat Impulsif:** Skor rata-rata untuk pernyataan "Saya impulsif" adalah **2.53 dari 4**. Ini menunjukkan kecenderungan untuk membuat keputusan belanja secara spontan, yang seringkali berujung pada penyesalan dan kecemasan.
    *   **📚❌ Kesenjangan antara Pengetahuan dan Praktik:** Banyak responden sadar akan risiko fintech (skor rata-rata 2.86), tapi pengalaman mereka dalam berinvestasi atau mengelola pinjaman masih rendah (skor 2.63-2.67). Artinya, mereka "tahu" tapi belum tentu "bisa" menerapkannya.
    *   **🏠💼 Faktor Non-Pekerjaan Lebih Berpengaruh:** Analisis awal kita menunjukkan bahwa tidak ada perbedaan signifikan tingkat kecemasan antara mereka yang masih mahasiswa dengan yang sudah bekerja. Ini menguatkan dugaan bahwa faktor seperti **lingkungan tempat tinggal** (kost vs. rumah orang tua) dan **kebiasaan pribadi** lebih besar pengaruhnya.

3.  **📱 Paparan Dunia Digital yang Serba Cepat.**
    Data juga menunjukkan tingginya penggunaan layanan keuangan digital. Kemudahan akses ke *paylater* atau promo *e-commerce* mempercepat siklus belanja-cemas-belanja lagi.

---

### 🎨 Bagian 3: Solusi Kita - Dashboard Interaktif yang "Ngobrol" dengan Pengguna

Nah, setelah tahu masalahnya, bagaimana cara kita menyelesaikannya? Jawabannya bukan dengan memberi laporan data yang membosankan. Kita akan membangun sebuah **dashboard interaktif** yang punya tiga misi utama:

#### 🗺️ Misi 1: Memetakan Masalah, Bukan Sekadar Menampilkan Angka

Dashboard kita akan berfungsi seperti peta. Pengguna bisa melihat:
*   **📊 Gambaran Umum (KPI Strip):** Angka-angka penting seperti skor kecemasan rata-rata, skor impulsif, dan tingkat kesadaran risiko digital akan ditampilkan di bagian paling atas.
*   **📉 Perbandingan Antar Kelompok (Grafik Batang):** Pengguna bisa membandingkan skor kecemasan antara mahasiswa dan pegawai, atau antara yang tinggal di kost dengan yang di rumah orang tua. Ini membantu kita menemukan segmen mana yang paling rentan.
*   **🔥 Peta Pemicu (Heatmap):** Visualisasi sederhana yang menunjukkan faktor-faktor apa saja (misalnya, impulsif, kurang perencanaan) yang korelasinya paling kuat dengan kecemasan.

#### 🎯 Misi 2: Memberi Rekomendasi yang Relevan (Bukan "Satu untuk Semua")

Dashboard ini akan dilengkapi dengan **rekomendasi yang adaptif** berdasarkan profil pengguna. Kita akan menggunakan *persona* (contoh karakter fiksi) untuk membuat rekomendasi lebih personal:

*   **👩‍🎓 Persona 1: Rani (20 tahun, Mahasiswi di Padang)**
    *   **Masalahnya:** Sering *checkout* impulsif saat *flash sale*, cemas saat saldo menipis sebelum kiriman bulanan datang.
    *   **Solusi dari Dashboard:** Rani bisa menggunakan fitur **simulator target tabungan mingguan** dan membaca rekomendasi tentang cara membuat "jeda" sebelum membeli barang.

*   **👨‍💼 Persona 2: Dimas (23 tahun, Pegawai Junior di Jakarta)**
    *   **Masalahnya:** Gajinya cukup, tapi bingung mau mulai investasi dari mana dan takut dengan biaya tersembunyi *paylater*.
    *   **Solusi dari Dashboard:** Dimas bisa melihat panel yang menjelaskan **simulasi "biaya total"** dari sebuah pinjaman dan membaca panduan sederhana tentang instrumen investasi risiko rendah.

#### 🔄 Misi 3: Mengubah Kebiasaan Lewat Interaksi

Fitur interaktif di dashboard dirancang untuk mendorong perubahan perilaku:
*   **Simulator Target Tabungan:** Pengguna bisa memasukkan target tabungan mereka (misalnya, "Rp 500.000 dalam 2 bulan"), dan dashboard akan memberikan saran alokasi mingguan yang realistis.
*   **Toggle "Cooling-Off":** Sebuah fitur konseptual di panel rekomendasi yang bisa "diaktifkan" untuk memberi pengingat agar menunda pembelian impulsif selama 24 jam.

---

### 🚀 Bagian 4: Strategi Kita untuk Menang (Langkah Sederhana)

Untuk memastikan proyek ini berhasil, kita akan fokus pada 7 langkah strategis:

1.  **Tampilkan Masalah Utama:** Sorot skor "kecemasan finansial" dengan visual yang jelas dan bersih.
2.  **Tunjukkan Pemicunya:** Gunakan *heatmap* atau grafik sederhana untuk menunjukkan faktor-faktor yang paling berpengaruh.
3.  **Bandingkan Antar Kelompok:** Buat perbandingan yang "bercerita", misalnya antara mahasiswa perantau vs. yang tinggal di rumah.
4.  **Sajikan Konteks Daerah:** Gunakan peta provinsi, tapi jangan lupa beri catatan tentang bias data kita. Kejujuran itu penting.
5.  **Buat Panel Aksi yang Berguna:** Rekomendasi harus singkat, praktis, dan dilengkapi simulator kecil.
6.  **Gunakan Bahasa Sederhana:** Setiap grafik harus punya penjelasan 1-2 kalimat: *"So what?"* (Apa artinya ini?).
7.  **Patuhi Aturan:** Pastikan output akhir kita sesuai dengan format dan kriteria dari panitia.

---

### 📖 Lampiran: Kamus Istilah Sederhana

*   **📄 CSV (Comma-Separated Values):** Bayangkan ini seperti file Excel, tapi lebih sederhana. Datanya dipisahkan oleh koma atau titik koma.
*   **🔍 EDA (Exploratory Data Analysis):** Proses "kenalan" atau "investigasi awal" terhadap data untuk menemukan pola, anomali, atau *insight* menarik.
*   **💡 Insight:** Penemuan atau pemahaman mendalam dari data yang tidak terlihat di permukaan. Contoh: "Insight kita adalah kecemasan tidak hanya dipengaruhi gaji, tapi juga kebiasaan."
*   **🗣️ Jargon:** Istilah teknis yang sulit dimengerti orang awam. Kita akan berusaha menghindarinya.
*   **🎭 Persona:** Karakter fiksi yang kita ciptakan berdasarkan data untuk mewakili kelompok pengguna tertentu (misalnya, "mahasiswa perantau"). Ini membantu kita merancang solusi yang lebih empatik.
*   **📝 Placeholder:** Konten sementara atau contoh yang digunakan sebagai kerangka, yang nantinya akan diganti dengan konten asli.

Semoga dengan panduan ini, kalian jadi lebih semangat dan punya gambaran yang jelas tentang apa yang akan kita bangun bersama. Mari kita ubah data ini menjadi sesuatu yang bermanfaat! 🚀