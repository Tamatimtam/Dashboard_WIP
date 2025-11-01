# Brainstorming & Ideation – Versi Ramah Pembaca (Non-Teknis)

Dokumen ini menjelaskan ide besar, langkah kerja sederhana, dan contoh hasil yang akan kita bangun untuk lomba “Financial Generation Z in Indonesia”. Fokusnya: mudah dimengerti oleh siapa pun (bukan hanya orang data), tapi tetap kuat untuk dinilai juri.

Kalau Anda hanya punya 3 menit, baca ringkasan berikut:
- Tujuan: menurunkan “kecemasan finansial” Gen Z lewat edukasi sederhana dan fitur interaktif yang langsung bisa dipraktikkan.
- Cara menang: tampilkan insight yang jelas, visual yang rapi, dan interaksi yang terasa “berguna sekarang juga”.
- Apa yang kami bangun: dashboard interaktif dengan 3 area utama—(1) gambaran besar, (2) pembanding antar kelompok, (3) peta + rekomendasi tindakan.
- Kenapa ini tepat: sesuai data (profil Gen Z didominasi pelajar/mahasiswa), relevan kebiasaan digital, dan mudah dipakai universitas/komunitas/industri.

Di bawah ini versi lengkapnya (bahasa mudah, langkah demi langkah).P

## 1. Pendahuluan (Kenapa dan Untuk Siapa)

Generasi Z (Gen Z) tengah memasuki fase kehidupan dewasa muda, dengan tantangan keuangan yang unik: transisi pendidikan-ke-kerja, kemandirian finansial, dan paparan intens terhadap layanan digital (fintech, e-wallet, paylater, dsb.). Dashboard yang efektif untuk Gen Z Indonesia harus mampu:

- Menyatukan indikator literasi keuangan, perilaku konsumen, dan konteks makro daerah.
- Mengidentifikasi segmen yang membutuhkan intervensi (edukasi, fitur produk, atau kebijakan lokal).
- Menawarkan interaktivitas yang memandu tindakan (call-to-action) dan rekomendasi yang relevan dengan persona pengguna.

Sasaran dashboard: memberi gambaran menyeluruh tentang “kondisi finansial sehari-hari” Gen Z lintas provinsi—mengaitkan literasi, kebiasaan belanja/menabung, serta risiko kecemasan finansial—untuk membantu pembuat kebijakan, kampus, serta pelaku industri (bank/fintech) merancang program yang tepat sasaran.

Kenapa ide ini cocok (alasan singkat):
- Fokus Gen Z: segmen dominan pada data (83,8% pelajar/mahasiswa) menuntut narasi edukasi yang kuat.
- Dampak sosial: kecemasan finansial (financial anxiety) berpotensi memengaruhi produktivitas belajar/kerja.
- Kebermanfaatan lintas pemangku kepentingan: dashboard menyajikan insight untuk regulator, kampus, dan industri.

Cara kita memenangkan lomba (7 langkah sederhana):
1) Tampilkan masalah utama (kecemasan finansial) dengan angka ringkas dan tampilan bersih.
2) Tunjukkan faktor pemicu yang paling berdampak (mis. impulsif, perencanaan) dengan heatmap yang mudah dibaca.
3) Bandingkan antar kelompok (pekerjaan, tempat tinggal, pendidikan) agar juri melihat “cerita” yang jelas.
4) Peta provinsi untuk konteks daerah—lengkapi catatan bias sampel (jujur, transparan).
5) Panel aksi: rekomendasi singkat + simulator kecil (mis. target tabungan mingguan).
6) Bahasa sederhana: setiap visual ada cerita 1–2 kalimat “so what?”
7) Kepatuhan booklet: format, deadline, dan sumber data sesuai aturan.

Ringkasan kepatuhan booklet (detail di Lampiran):
- Deadline pengumpulan: 15 November 2025, 23.59 WIB. Format PDF A4, TNR 12, spasi 1.5, justify.
- Penilaian: Visualisasi (25), Insight & analisis (30), Interaktivitas (25), Struktur & kerapian (20).
- Larangan: hanya dataset dari panitia yang boleh digunakan; pastikan tautan hasil dapat diakses.

## 2. Dasar Pemikiran (Bahasa Sederhana)

2.1. Literasi dan Perilaku Keuangan Gen Z
- Dalam literatur keuangan personal, literasi keuangan (kemampuan memahami konsep keuangan dasar hingga lanjutan) berkorelasi dengan perilaku pengelolaan uang: budgeting, tabungan, dan pengambilan keputusan investasi.
- Gen Z secara global memiliki eksposur tinggi ke kanal digital (e-wallet, paylater, investasi ritel), yang dapat mempercepat adopsi keuangan digital sekaligus meningkatkan risiko perilaku impulsif.

2.2. Financial Anxiety (Kecemasan Finansial)
- Financial anxiety adalah kondisi emosi negatif terkait keadaan keuangan—ditandai dengan kekhawatiran, rasa tidak kontrol, hingga kesulitan menikmati hidup. Dalam riset perilaku, skor kecemasan sering dipengaruhi oleh pendapatan, pengeluaran, hutang, dan keterampilan finansial.
- Di konteks dashboard ini, kami memanfaatkan beberapa butir pernyataan Likert yang menggambarkan dimensi kecemasan finansial, dan menyusunnya menjadi indeks sederhana (rata-rata item terkait; semakin tinggi semakin “cemas”).

2.3. Konteks Regional
- Indikator ekonomi daerah (PDRB, urbanisasi, aktivitas pinjaman, kualitas risiko TWP 90%) memengaruhi akses dan perilaku keuangan. Provinsi yang lebih urban/tinggi PDRB cenderung punya penetrasi fintech lebih tinggi, dengan dinamika risiko (utang) yang berbeda.

Kenapa pendekatan ini logis:
- Dashboard harus mengaitkan level individu (literasi, sikap, perilaku) dengan faktor regional—agar rekomendasi kebijakan/produk tidak seragam (one-size-fits-all).
- Indeks kecemasan finansial sebagai fokus outcome (dependent variable) memudahkan penceritaan dampak.

## 3. Metodologi (Singkat & Mudah Dipahami)

1) Rapikan data & definisikan variabel
- Parsing CSV menggunakan delimiter semikolon (;) dan normalisasi encoding.
- Membersihkan kolom uang (pendapatan/pengeluaran) menjadi numerik jika memungkinkan; bila tidak, kami buat catatan keterbatasan.
- Menyusun indeks “financial_anxiety_score” dari 5 item Likert negatif (rata-rata skor 1–4).

2) Eksplorasi Data (EDA) terarah
- Deskriptif numerik (mean, median, std, min–max, quantile) dan kategorikal (proporsi top-10 kategori).
- Korelasi variabel utama; inspeksi outlier (IQR) dan potensi data leakage.
- Uji hipotesis non-parametrik (Kruskal-Wallis, Mann-Whitney) dan korelasi Spearman (p<0,05) sesuai karakter data Likert.

3) Storytelling & desain interaktif
- Merumuskan persona dan narasi “dari data ke aksi” (call-to-action).
- Mendesain layout dashboard (KPI – segmentasi – peta – rekomendasi), interaksi filter, dan simulator skenario.

Catatan istilah (versi santai):
- Likert scale: skala persetujuan 1–4 (semakin tinggi semakin setuju).
- IQR (Interquartile Range): rentang Q3–Q1; outlier sering didefinisikan di luar [Q1-1,5*IQR, Q3+1,5*IQR].
- Uji non-parametrik (Mann-Whitney/Kruskal-Wallis): alternatif uji beda rata-rata tanpa asumsi distribusi normal.
- Spearman: korelasi peringkat untuk hubungan monotonic.

## 4. Hasil & Pembahasan (Intinya Apa?)

4.1. Ringkasan Dataset & Kualitas Data
- GenZ_Financial_Literacy_Survey.csv
  - Ukuran: 1.652 baris × 58 kolom (demografi + item Likert literasi/perilaku/emosi finansial).
  - Missing utama: “Gender” (~6,9%), “Est. Monthly Income” (~7,1%), “Est. Monthly Expenditure” (~7,0%).
  - Skala Likert 1–4, mayoritas item lengkap (>99%).
- GenZ_Financial_Profile.csv
  - Ukuran: 1.652 baris × 59 kolom. Struktur kolom identik/serupa dengan survei; ini menunjukkan kedua file merekam informasi yang sangat mirip (kemungkinan penggandaan/turunan). Terdapat kolom kosong “Unnamed: 58”.
  - Kesimpulan: untuk EDA awal, satu tabel utama (profil/survei) cukup mewakili; kolom duplikat/nameless perlu di-drop saat produksi.
- Regional_Economic_Indicators.csv
  - Ukuran: 38 baris × 16 kolom (provinsi). Beberapa kolom “Unnamed” kosong (100% NA). PDRB bertipe numerik; kolom lain masih bertipe teks dan perlu parsing angka.

4.2. Variabel Kunci & Definisi (bahasa awam)
- Gender, Province of Origin, Residence Status, Last Education, Job, Year of Birth.
- Indikator sikap/kompetensi: puluhan item Likert terkait kemampuan memahami angka, perencanaan, negosiasi, kesadaran risiko fintech, dll.
- Finansial dasar (objek teks): Est. Monthly Income, Est. Monthly Expenditure. Catatan: kolom ini berformat string yang tidak standar, sehingga konversi ke numerik gagal untuk mayoritas baris; kami gunakan variabel turunan saat memungkinkan.
- Indeks financial_anxiety_score (1–4): rata-rata dari 5 butir negatif (semakin tinggi = makin cemas).
- Turunan saving_rate: (income − expense) / income (dengan validasi pembagi > 0). Karena income/expense tidak numerik di banyak baris, indikator ini terbatas.

4.3. Statistik Deskriptif (cuplikan)
- Ukuran sampel: n = 1.652.
- Distribusi pendidikan: SMA (62,1%), S1/D4 (21,6%), Diploma (14,0%), Pasca (1,1%).
- Pekerjaan: Student (83,8%), Private Employee (6,0%), Others (4,5%), Not Working (2,5%).
- Status tempat tinggal: Parent’s House (50,2%), Rental House (30,8%), Family House (8,9%).
- Skor rata-rata financial_anxiety_score = 2,62 (sd 0,52) pada skala 1–4.

4.4. Komposisi Kategori (gambaran cepat)
- Gender tampak heterogen (beberapa penamaan “Female/F/Wanita” dan “Male/M/Pria”); ini akan distandarkan pada tahap cleaning.
- Provinsi terkonsentrasi di West Sumatera (47,0%) lalu North Sumatera (12,2%), DKI Jakarta (11,5%), Central Java (11,6%). Ini menunjukkan bias sampling regional yang harus diakui dalam keterbatasan.

4.5. Korelasi Variabel Utama (hubungan antar variabel)
- Korelasi Pearson di antara [financial_anxiety_score, income_num, expense_num, saving_rate] tidak konklusif (NA) karena income/expense gagal menjadi numerik pada mayoritas baris.
- Rekomendasi: mapping income/expense yang berbentuk kategori/rentang ke nilai tengah rentang (bin-centroid) agar dapat dianalisis secara kuantitatif.

4.6. Nilai Ekstrem & Potensi Data “Bocor”
- Outlier pada income/expense tidak dapat dihitung reliabel (data numerik kosong). Namun item Likert memiliki rentang 1–4 sehingga tidak ekstrem.
- Potensi data leakage: keberadaan kolom duplikat/Unnamed, redundansi antara dua file profil/survei. Cleaning: drop kolom kosong, pilih satu sumber “master”.

4.7. 10 Insight Actionable (dengan bahasa sederhana)
1) Mayoritas responden masih pelajar/mahasiswa (83,8%).
   - Dampak: kanal edukasi finansial melalui kampus sangat relevan.
   - Aksi: modul micro-learning literasi & budgeting di dashboard untuk kelas/UKM kampus.
2) Skor kecemasan finansial berada pada level sedang (mean 2,62/4).
   - Dampak: ruang intervensi untuk menurunkan kecemasan (edukasi risiko, fitur kontrol).
   - Aksi: panel “Anxiety Drivers” yang memetakan butir penyebab utama (mis. “my finances control my life”).
3) Perilaku pengambilan keputusan cukup rasional (banyak item pada 2,9–3,1).
   - Dampak: penguatan tools perbandingan harga, tracking promosi dapat memperkuat saving behavior.
   - Aksi: integrasi tips “negotiation & discount tracking” sebagai quick-win.
4) Konsentrasi provinsi di Sumatera Barat dan beberapa provinsi Jawa.
   - Dampak: insight wilayah harus dibaca dengan bias sampling; rencana re-sampling/weighting jika data tambahan tersedia.
   - Aksi: peta choropleth dengan peringatan bias; filter “Provinsi dengan n≥30” untuk stabilitas.
5) “I am impulsive” rata-rata 2,53/4.
   - Dampak: still moderate; modul anti-impulsive purchase (cooling-off timer) berpotensi menurunkan kecemasan.
   - Aksi: simulator “delay 24 jam vs checkout sekarang” pada dashboard.
6) Partisipasi dalam perencanaan pengeluaran domestik relatif tinggi (mean 2,72/4).
   - Dampak: leverage budaya keluarga untuk edukasi finansial kolektif.
   - Aksi: fitur “home budgeting checklist” untuk mahasiswa rantau.
7) Kesadaran risiko fintech cukup baik (mean 2,86/4), namun pengalaman produk pinjaman/investasi lebih rendah (2,63–2,67/4).
   - Dampak: gap antara awareness dan pengalaman; perlu literasi praktik (sandbox aman).
   - Aksi: konten “simulasi investasi sederhana” + “biaya pinjaman total cost”.
8) Item “I keep an eye on promotions and discounts” tinggi (3,13/4).
   - Dampak: promosi bisa diarahkan ke instrumen menabung (e.g., bonus top-up tabungan) alih-alih konsumsi.
   - Aksi: rekomendasi “promo saving” berbasis event kampus/gaji.
9) Item “I like to think thoroughly before deciding to buy” tinggi (3,12/4).
   - Dampak: penguatan fitur pembanding harga/biaya jangka panjang.
   - Aksi: panel “total cost of ownership” untuk pembelian besar (gadget/kontrak kost).
10) Uji hipotesis awal menunjukkan tidak ada perbedaan signifikan skor kecemasan antar status pekerjaan (p≈0,309) dan korelasi dengan usia sangat kecil (ρ≈0,008; p≈0,738).
   - Dampak: variabilitas kecemasan lebih dipengaruhi faktor lain (misal kondisi rumah tangga, beban tanggungan, atau pengalaman utang) ketimbang usia/pekerjaan pada sampel ini.
   - Aksi: perlu eksplorasi segmentasi tambahan (status tinggal, provinsi, dan kebiasaan impulsif).

4.8. Visualisasi Utama yang Akan Dibuat (apa dan kenapa)
- KPI strip (top row): skor kecemasan (mean, distribusi), proporsi pendidikan, proporsi status tinggal, dan coverage provinsi.
- Heatmap korelasi item “driver” dengan kecemasan (Spearman antar butir terpilih) – prioritas tinggi.
- Bar chart perbandingan skor anxiety per segmen (job/residence/province cluster) – prioritas tinggi.
- Peta choropleth: median skor anxiety per provinsi (hanya provinsi dengan n≥30) – prioritas tinggi.
- Scatter (jika income numerik telah dipetakan): income vs anxiety dengan garis tren – prioritas menengah (butuh cleaning lanjutan).

4.9. Narasi + Persona (untuk siapa fitur ini)
- Narasi: “Menjelang kemandirian finansial, Gen Z Indonesia menghadapi kecemasan yang bersumber dari kendali finansial sehari-hari. Dashboard membantu mengenali pemicu, menguji skenario, dan mendapatkan rekomendasi langkah sederhana untuk memperbaiki keseharian finansial.”

Persona 1 – Rani (20, Padang, Mahasiswi)
- Masalah: sering checkout impulsif saat flash sale; cemas ketika saldo menipis sebelum kiriman bulanan.
- Goal: menjaga pengeluaran tetap di bawah batas mingguan; mulai menabung darurat.
- Insight terkait data: skor impulsif rata-rata cukup tinggi; promosi sering menarik (mean promo 3,13/4).
- Rekomendasi produk: Reminder anggaran mingguan + timer “cooling-off”; kartu skor anxiety harian.

Persona 2 – Dimas (23, Jakarta, Pegawai Swasta Junior)
- Masalah: bingung memulai investasi; takut biaya pinjaman/paylater.
- Goal: menabung rutin 10% dan mencoba instrumen investasi risiko rendah.
- Insight: pengalaman investasi/pinjaman lebih rendah (2,63–2,67/4).
- Rekomendasi: panel “simulasi total cost” dan “simulasi reksadana pasar uang” dengan auto-debit gaji.

Persona 3 – Sari (21, Yogyakarta, Mahasiswi Rantau)
- Masalah: biaya kost dan makan sering membengkak; cemas saat akhir bulan.
- Goal: disiplin budget kategori (makanan, transport, hiburan) dan mengurangi impulsif.
- Insight: saving behavior bisa dikuatkan dengan perencanaan domestik (mean 2,72/4).
- Rekomendasi: template “anggaran kost” + tips hemat lokal; panel “cek tren harian vs target”.

4.10. Pembersihan dan Transformasi Data yang Disarankan (biar grafik/angka makin akurat)
- Income/Expense: saat ini berupa teks non-standar. Solusi: deteksi pola rentang nominal (mis. “1–3 juta”), map ke nilai tengah rentang (2 juta), konversi ke IDR float. Untuk teks bebas, gunakan regex untuk menangkap digit dan satuan “ribu/juta”.
- Standarisasi Gender: map {“F”, “Female”, “Wanita”}→Female; {“M”, “Male”, “Pria”}→Male.
- Drop kolom kosong (“Unnamed: 58”) dan kolom duplikat.
- Cohorts: Year of Birth → cohort (SMA akhir, kuliah awal, lulus baru) untuk analisis segmentasi.

## 5. Kesimpulan & Saran (Langkah Praktis)

Kesimpulan utama:
- Kecemasan finansial Gen Z pada tingkat sedang; bukan ekstrem, namun cukup bermakna untuk intervensi edukasi dan fitur kontrol perilaku konsumsi.
- Perilaku rasional (pertimbangan sebelum membeli, pantau diskon) relatif kuat—momentum untuk mengarahkan “promosi” ke perilaku menabung dan pengelolaan risiko.
- Tidak ditemukan perbedaan signifikan kecemasan berdasarkan status pekerjaan dan usia—memperkuat dugaan bahwa konteks rumah tangga/tempat tinggal dan kebiasaan belanja lebih berpengaruh.

Saran tindak lanjut:
- Perbaiki parsing income/expense agar metrik saving_rate dan korelasi menjadi andal.
- Perluas analisis ke per-provinsi dengan bobot sampel, mengingat bias besar di Sumatera Barat.
- Bangun modul rekomendasi adaptif berbasis persona (edukasi + aksi), dengan evaluasi metrik pasca-intervensi.

Keterbatasan (jujur & jelas):
- Bias sampel provinsi; variabel income/expense tidak numerik – membatasi analisis finansial kuantitatif langsung.
- Data self-reported: potensi bias desirability dan recall.

Langkah pengembangan berikutnya (roadmap ringan):
- Penstandaran variabel, imputasi berbasis median/rentang, dan pengayaan indikator perilaku (skor impulsif, negosiasi, perencanaan).
- Integrasi indikator ekonomi regional setelah standardisasi nama provinsi.

---

## Lampiran A – EDA Ringkas (berdasarkan notebook)
- n = 1.652; 58–59 kolom (profil/survei). Banyak item Likert skala 1–4 lengkap.
- financial_anxiety_score (mean 2,62; sd 0,52). Income/expense perlu pemetaan rentang→nilai.
- Distribusi kategori utama (persen di atas) – lihat bagian 4.3–4.4.
- Korelasi utama saat ini tidak konklusif untuk variabel uang (butuh cleaning lanjutan).

## Lampiran B – 8+ KPI/Dashboard Metrics (dengan prioritas)
- Financial Anxiety Score (High)
- Impulsivity Score (komposit 3 item: impulsif, berpikir tanpa pertimbangan, berkata tanpa pikir) (High)
- Domestic Expense Planning Participation (High)
- Promo/Discount Monitoring Score (Medium)
- Negotiation Tendency Score (Medium)
- Digital Risk Awareness (fintech legality/fee awareness) (High)
- Investment/Loan Experience Score (Medium)
- Education Level Distribution (Medium)
- Residence Status Mix (Medium)
- Province Coverage & n (High)
- Saving Rate (jika income/expense berhasil dinumerisasi) (High)

## Lampiran C – Hypothesis-driven Analysis
Hipotesis dan hasil singkat (p<0,05 sebagai threshold):
- H1 (gender): tidak dilakukan karena label gender tidak konsisten untuk uji 2-kelompok sederhana (perlu standardisasi terlebih dahulu).
- H2 (status pekerjaan): Kruskal-Wallis p≈0,309 (tidak signifikan). Efek relatif kecil, perlu segmen lain.
- H3 (impulsivitas vs saving_rate): butuh income numerik; sementara menggunakan proksi, temuan belum konklusif.
- H4 (anxiety vs saving_rate): korelasi Spearman perlu data saving_rate yang andal.
- H5 (anxiety vs usia): ρ≈0,008; p≈0,738 (tidak signifikan).

Decision rationale:
- Mengutamakan uji non-parametrik karena data Likert dan asumsi normalitas lemah.
- Menunda uji income terkait sampai cleaning selesai.

## Lampiran D – Rekomendasi Desain Dashboard (versi non-teknis)
- Pengelompokan panel (untuk UI/UX):
   - Satu div: KPI (Anxiety, Impulsivity, Risk Awareness) + tombol “Clear filters”.
   - Satu div: Perbandingan antar segmen (bar/box) + heatmap “drivers”.
   - Satu div: Peta provinsi + daftar rekomendasi adaptif + simulator target tabungan.
- Contoh alur pakai: lihat skor anxiety → klik segmen “Mahasiswa Rantau” → lihat driver yang paling kuat → baca rekomendasi → uji skenario tabungan mingguan.
- Layout:
  - Top row (Overview KPI): Anxiety, Impulsivity, Risk Awareness, Coverage.
  - Middle: Segmentasi (job, residence, cohort) + komparasi skor.
  - Bottom: Peta provinsi + panel rekomendasi dan simulator.
- 10 Visual (judul, jenis, why, data, interaksi) beserta prioritas – dipaparkan di dokumen panel terpisah.
- Warna & tipografi: gunakan palet kontras tinggi; alternatif ramah aksesibilitas disediakan.

## Lampiran E – Rekomendasi Kebijakan/Produk (5 poin)
1) Program literasi finansial modular di kampus (High)
   - Manfaat: menurunkan anxiety; meningkatkan risk awareness.
   - Target: mayoritas sampel (pelajar/mahasiswa, ~84%).
   - Metrik: pre/post anxiety score; completion rate modul.
2) Fitur “cooling-off” + target tabungan mingguan (High)
   - Manfaat: menekan impulsif; meningkatkan saving habit.
   - Target: pengguna dengan impulsivity score tinggi.
   - Metrik: penurunan transaksi impulsif; peningkatan saving streak.
3) Simulasi “total cost” & “sandbox investasi pemula” (Medium)
   - Manfaat: mengurangi mispersepsi biaya dan risiko.
   - Target: pengguna dengan pengalaman investasi/pinjaman rendah.
   - Metrik: CTR modul; peningkatan literasi/evaluasi risiko.
4) Promo diarahkan ke tabungan (Medium)
   - Manfaat: alihkan minat promosi ke perilaku keuangan sehat.
   - Target: segmen yang tinggi pada “promo monitoring”.
   - Metrik: jumlah top-up tabungan saat promo; retensi.
5) Kemitraan daerah untuk edukasi berbasis provinsi (Medium)
   - Manfaat: konteks lokal; menjangkau daerah dominan sampel.
   - Target: provinsi dengan n terbesar (Sumatera Barat, DKI, Jateng).
   - Metrik: jangkauan peserta; perubahan skor literasi.

## Lampiran F – Pertimbangan Etika & Keterbatasan
- Sampling bias: dominasi provinsi tertentu; tidak dapat digeneralisasi nasional tanpa pembobotan.
- Self-report bias: potensi over/under-report perilaku.
- Data income/expense: tidak numerik; perlu transparansi asumsi mapping.
- Privasi: hindari identifikasi individu; hanya tampilkan agregat/anonymized.

## Lampiran G – Aturan Kompetisi (ringkas)
- Periode pengerjaan: 1–15 Nov 2025; deadline 15 Nov 2025 23.59 WIB.
- Hanya dataset panitia; tautan hasil harus dapat diakses.
- Output PDF A4, TNR 12, spasi 1.5, rata kanan-kiri. Nama file: DA2025_NamaTim_NamaKetua.pdf.
- Penilaian total 100: Visual (25), Insight (30), Interaktivitas (25), Struktur (20). Sanksi terlambat: -2 poin/jam.

