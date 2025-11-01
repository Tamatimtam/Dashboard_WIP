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

# 📐 Blueprint Dashboard: Membedah Setiap Panel (Versi Lengkap & Mudah Dipahami)

Halo teman-teman! 👋

Selamat datang di "Blueprint Dashboard" kita. Anggap saja dokumen ini adalah denah rumah yang akan kita bangun. Di sini, kita akan membedah setiap "ruangan" (panel) di dashboard kita satu per satu.

Tujuannya? Agar kita semua punya pemahaman yang sama tentang:
*   **🎨 Panel apa saja** yang akan ditampilkan.
*   **❓ Kenapa panel itu penting** dan pertanyaan apa yang dijawabnya.
*   **📁 Dari mana datanya berasal** (dari file CSV yang mana).
*   **👁️ Bagaimana cara membacanya** dan apa interaksi yang bisa dilakukan.

Analogi terbaik untuk dashboard kita adalah seperti **🚗 dashboard mobil**. Ada speedometer (KPI), peta GPS (analisis mendalam), dan buku panduan (rekomendasi). Semua dirancang agar pengemudi (pengguna kita) bisa mengambil keputusan dengan cepat dan tepat.

Mari kita mulai tur-nya! 🚀

---

### 🗺️ Susunan Halaman: Perjalanan Memahami Cerita Data

Dashboard kita akan dibagi menjadi tiga bagian utama yang mengalir seperti sebuah cerita, dari gambaran besar hingga detail yang bisa ditindaklanjuti.

1.  **⬆️ Bagian Atas – Ringkasan Cepat (Speedometer & Indikator Utama)**
    *   *Tujuan:* Memberi gambaran kondisi umum dalam 5 detik. "Apa situasi saat ini?"

2.  **🔍 Bagian Tengah – Analisis Mendalam (Membuka Kap Mesin)**
    *   *Tujuan:* Menemukan akar masalah dan kelompok mana yang paling terdampak. "Kenapa situasinya seperti ini?"

3.  **⬇️ Bagian Bawah – Dari Data ke Aksi (GPS & Buku Panduan)**
    *   *Tujuan:* Memberikan konteks geografis dan rekomendasi praktis. "Di mana ini terjadi dan apa yang bisa kita lakukan?"

---

### 📊 Bagian 1: Ringkasan Cepat (KPI - Key Performance Indicators)

Ini adalah bagian pertama yang akan dilihat pengguna. Angka-angka besar yang langsung menyorot temuan utama kita.

#### **🎯 Panel 1.1: Skor Kecemasan Finansial Rata-Rata**

*   **🎨 Bentuk Visual:** Sebuah kartu besar dengan angka di tengah (misal, **2.62** / 4.00) dan mungkin sebuah *gauge* (meteran) berwarna untuk menunjukkan levelnya (misalnya, kuning untuk "cukup cemas").
*   **❓ Pertanyaan yang Dijawab:** "Secara umum, seberapa cemas Gen Z di Indonesia terkait kondisi keuangan mereka?"
*   **⭐ Kenapa Ini Penting?** Ini adalah **bintang utama** dari cerita kita. Angka ini adalah justifikasi kenapa proyek ini perlu ada. Ini adalah masalah yang ingin kita bantu selesaikan.
*   **📁 Hubungannya dengan Data Kita:**
    *   Skor ini dihitung dari rata-rata jawaban 5 pertanyaan kunci di file `GenZ_Financial_Literacy_Survey.csv`. Pertanyaan-pertanyaan tersebut adalah:
        1.  *"Because of my money situation, I feel I will never have the things I want in life"*
        2.  *"I am behind with my finances"*
        3.  *"My finances control my life"*
        4.  *"Whenever I feel in control of my finances, something happens that sets me back"*
        5.  *"I am unable to enjoy life because I obsess too much about money"*
    *   Setiap jawaban memiliki skala 1 (sangat tidak setuju) hingga 4 (sangat setuju). Semakin tinggi skornya, semakin tinggi tingkat kecemasannya.
*   **📖 Cara Membacanya:** Skor di atas 2.5 menunjukkan adanya tingkat kecemasan yang perlu diperhatikan.

---

### 🔬 Bagian 2: Analisis Mendalam (Menemukan "Kenapa"-nya)

Setelah melihat gambaran besar, pengguna pasti bertanya, "Kenapa skornya segitu? Siapa yang paling terdampak?" Bagian ini menjawab pertanyaan tersebut.

#### **📊 Panel 2.1: Perbandingan Skor Kecemasan antar Segmen**

*   **🎨 Bentuk Visual:** Grafik batang horizontal (*bar chart*). Setiap batang mewakili satu segmen (misalnya, "Mahasiswa", "Pegawai Swasta", "Tinggal di Kost").
*   **❓ Pertanyaan yang Dijawab:** "Kelompok Gen Z mana yang memiliki tingkat kecemasan finansial paling tinggi atau paling rendah?"
*   **⭐ Kenapa Ini Penting?** Panel ini membantu kita **mengidentifikasi kelompok rentan**. Jika ternyata mahasiswa perantau punya skor tertinggi, maka rekomendasi kita harus lebih fokus ke mereka. Ini membuat solusi kita tidak "satu untuk semua".
*   **📁 Hubungannya dengan Data Kita:**
    *   Kita mengambil skor `financial_anxiety_score` yang sudah kita hitung.
    *   Kemudian, kita kelompokkan berdasarkan kolom-kolom demografi dari file `GenZ_Financial_Profile.csv`, seperti:
        *   `Job` (Pekerjaan)
        *   `Residence Status` (Status Tempat Tinggal)
        *   `Last Education` (Pendidikan Terakhir)
*   **📖 Cara Membacanya:** Batang yang lebih panjang menunjukkan skor kecemasan rata-rata yang lebih tinggi untuk segmen tersebut.
*   **🖱️ Interaksi Pengguna:** Ini adalah salah satu fitur interaktif utama. Ketika pengguna **mengklik salah satu batang** (misalnya, batang "Mahasiswa"), semua panel lain di dashboard akan otomatis ter-filter untuk hanya menampilkan data tentang mahasiswa.

#### **🔥 Panel 2.2: Peta Pemicu Kecemasan (Heatmap)**

*   **🎨 Bentuk Visual:** Sebuah tabel berwarna (*heatmap*). Warna di setiap sel menunjukkan "kekuatan hubungan" antara sebuah perilaku dengan tingkat kecemasan.
*   **❓ Pertanyaan yang Dijawab:** "Dari semua kebiasaan finansial yang ada di data, mana yang paling kuat hubungannya dengan kecemasan finansial?"
*   **⭐ Kenapa Ini Penting?** Ini adalah **jantung dari analisis kita**. Panel ini secara langsung menunjukkan akar masalahnya. Jika kita tahu bahwa "sifat impulsif" punya korelasi paling kuat, maka solusi kita harus fokus untuk mengurangi perilaku impulsif.
*   **📁 Hubungannya dengan Data Kita:**
    *   Panel ini tidak menampilkan data mentah, melainkan hasil analisis statistik (korelasi Spearman) antara `financial_anxiety_score` dengan kolom-kolom perilaku lainnya, seperti:
        *   `I am impulsive` (Saya impulsif)
        *   `I am able to plan ahead to avoid impulse spending` (Saya bisa merencanakan agar tidak belanja impulsif)
        *   `I always try to save some money to do things I really like` (Saya selalu mencoba menabung)
        *   `I keep an eye on promotions and discounts` (Saya memantau promosi dan diskon)
*   **📖 Cara Membacanya:**
    *   **🔴 Warna Merah Pekat:** Menunjukkan hubungan positif yang kuat. Artinya, semakin tinggi skor perilaku ini, semakin tinggi pula skor kecemasannya (ini adalah **pemicu/faktor risiko**).
    *   **🔵 Warna Biru Pekat:** Menunjukkan hubungan negatif yang kuat. Artinya, semakin tinggi skor perilaku ini, semakin *rendah* skor kecemasannya (ini adalah **pelindung/faktor positif**).
    *   **⚪ Warna Pudar:** Hubungannya lemah.

---

### 🎯 Bagian 3: Dari Data ke Aksi (Menawarkan Solusi)

Bagian terakhir ini adalah yang paling fungsional. Tujuannya adalah memberikan konteks geografis dan, yang terpenting, rekomendasi yang bisa langsung dipraktikkan.

#### **🗺️ Panel 3.1: Peta Sebaran Kecemasan per Provinsi**

*   **🎨 Bentuk Visual:** Peta Indonesia yang warnanya berbeda-beda di setiap provinsi (*choropleth map*).
*   **❓ Pertanyaan yang Dijawab:** "Di provinsi mana saja tingkat kecemasan finansial Gen Z cenderung lebih tinggi atau lebih rendah?"
*   **⭐ Kenapa Ini Penting?** Memberikan konteks geografis. Mungkin ada hubungannya dengan kondisi ekonomi regional, UMR, atau budaya lokal. Ini sangat berguna untuk pembuat kebijakan di tingkat daerah.
*   **📁 Hubungannya dengan Data Kita:**
    *   Warna setiap provinsi ditentukan oleh skor `financial_anxiety_score` rata-rata dari responden yang berasal dari `Province of Origin` tersebut.
    *   Saat kursor diarahkan ke sebuah provinsi, akan muncul *tooltip* yang menampilkan data tambahan dari file `Regional_Economic_Indicators.csv`, seperti PDRB dan tingkat urbanisasi.
*   **📖 Cara Membacanya:** Warna yang lebih gelap menandakan skor kecemasan yang lebih tinggi.
*   **⚠️ DISCLAIMER PENTING:** Di panel ini, kita **wajib** menampilkan catatan bahwa data kita memiliki bias sampel (sangat banyak dari Sumatera Barat), sehingga peta ini adalah gambaran dari data yang kita punya, bukan representasi akurat seluruh Indonesia.

#### **💡 Panel 3.2: Panel Aksi & Rekomendasi Adaptif**

*   **🎨 Bentuk Visual:** Sebuah kotak teks dinamis yang isinya berubah-ubah.
*   **❓ Pertanyaan yang Dijawab:** "Oke, saya sudah lihat datanya. Sekarang, apa yang harus saya lakukan?"
*   **⭐ Kenapa Ini Penting?** Inilah yang membedakan dashboard kita dari yang lain. Kita tidak hanya "melaporkan" masalah, tapi juga **menawarkan solusi**. Ini adalah jembatan dari *insight* ke *action*.
*   **📁 Hubungannya dengan Data Kita:** Panel ini sangat cerdas. Isinya akan **berubah secara dinamis** berdasarkan filter yang dipilih pengguna di panel lain.
    *   **📌 Contoh 1:** Jika pengguna memfilter segmen "Mahasiswa Perantau" (dari Panel 2.1), rekomendasi yang muncul bisa berupa: *"Tips Cerdas Mengelola Anggaran Kost"* atau *"Cara Menghindari Jebakan Promo Makanan Online."*
    *   **📌 Contoh 2:** Jika data menunjukkan korelasi kuat antara kecemasan dan perilaku impulsif (dari Panel 2.2), rekomendasi yang muncul bisa: *"Terapkan Aturan 24 Jam: Tunda Pembelianmu untuk Menghindari Penyesalan."*
*   **🖱️ Interaksi Pengguna:** Pengguna membaca dan bisa langsung mendapatkan ide praktis yang sesuai dengan profil atau masalah yang sedang mereka lihat.

#### **🎯 Panel 3.3: Mini Simulator Target Tabungan**

*   **🎨 Bentuk Visual:** Beberapa kotak input sederhana di mana pengguna bisa mengetikkan angka.
*   **❓ Pertanyaan yang Dijawab:** "Bagaimana cara saya mencapai target tabungan saya dengan cara yang realistis?"
*   **⭐ Kenapa Ini Penting?** Membuat konsep "menabung" yang abstrak menjadi sesuatu yang **konkret dan terukur**. Ini adalah alat bantu praktis yang memberikan rasa kontrol kepada pengguna.
*   **📁 Hubungannya dengan Data Kita:** Panel ini tidak secara langsung memvisualisasikan data yang ada, tetapi merupakan **fitur solusi** yang dirancang berdasarkan masalah yang kita temukan dalam data (yaitu, kurangnya perencanaan dan kebiasaan menabung).
*   **🔢 Cara Menggunakannya:**
    1.  Pengguna memasukkan: "Saya ingin menabung sebesar..." (misal, `Rp 1.000.000`).
    2.  Pengguna memasukkan: "...dalam waktu" (misal, `3 bulan`).
    3.  Dashboard akan otomatis menghitung: **"Artinya, kamu perlu menyisihkan sekitar Rp 84.000 setiap minggu. Semangat!"** 💪

---

