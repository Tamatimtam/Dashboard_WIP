# Dashboard Panels – Versi Mudah Dipahami (Non-Teknis)

Tujuan: memberi panduan panel apa saja yang perlu ada, kenapa penting, dan bagaimana mereka dikelompokkan di layar agar mudah digunakan. Untuk contoh gambarnya, lihat notebook `notebooks/dashboard_panels_demo.ipynb` (ada contoh visual langsung per panel).

## Susunan Halaman (3 Bagian Besar)
1) Bagian Atas – Ringkasan Cepat (KPI)
  - Tampilkan 3–4 angka penting: Skor Kecemasan, Impulsif, Awareness Risiko Digital, dan jumlah responden aktif (opsional).
  - Kenapa? Supaya pengguna langsung “ngeh” kondisi umum tanpa membaca panjang.

2) Bagian Tengah – Bandingkan Kelompok & Cari Penyebab
  - Grafik batang per segmen (mis. Mahasiswa vs Pegawai; Tinggal dengan Orang Tua vs Kontrakan).
  - Heatmap sederhana yang menunjukkan faktor mana yang paling berhubungan dengan kecemasan.
  - Kenapa? Ini bagian “insight”—kita menemukan apa yang perlu ditindaklanjuti.

3) Bagian Bawah – Peta & Rekomendasi Tindakan
  - Peta provinsi (atau daftar provinsi) + rekomendasi singkat yang berubah sesuai filter.
  - Simulator target tabungan mingguan (sederhana, bisa diisi pengguna).
  - Kenapa? Menghubungkan data dengan aksi nyata.

## Panel Wajib (dan alasannya)
1) KPI: Financial Anxiety (wajib)
  - Alasan: ini “hasil utama” yang ingin diturunkan.
2) KPI: Impulsivity (wajib)
  - Alasan: perilaku impulsif sering jadi pemicu kecemasan.
3) KPI: Digital Risk Awareness (wajib)
  - Alasan: kesiapan menghadapi produk finansial digital.
4) Grafik Batang: Anxiety per Segmen (wajib)
  - Alasan: melihat segmen mana yang “perlu bantuan duluan”.
5) Heatmap: Drivers vs Anxiety (wajib)
  - Alasan: menunjukkan faktor kunci yang harus ditangani.
6) Peta/Daftar Provinsi: Median Anxiety (wajib)
  - Alasan: konteks daerah + catatan jika jumlah responden sedikit.
7) Donut: Komposisi Pendidikan & Tempat Tinggal (pelengkap)
  - Alasan: profil cepat untuk memahami siapa pengguna kita.
8) Scatter: Anxiety vs Income (opsional)
  - Alasan: jika data pendapatan sudah dibersihkan ke numerik.
9) Panel Rekomendasi & CTA (wajib)
  - Alasan: menjembatani dari data ke tindakan sederhana.
10) Mini Simulator Tabungan (pelengkap)
  - Alasan: mempraktekkan langkah kecil yang terukur.

## Pengelompokan Panel (Agar UI terasa “nyambung”)
- Satu div: KPI (Anxiety, Impulsivity, Risk Awareness) + tombol Reset Filter.
- Satu div: Bar “Anxiety per Segmen” berdampingan dengan Heatmap “Drivers”.
- Satu div: Peta/Daftar Provinsi + Rekomendasi + Simulator.

## Catatan Praktis
- Semua panel harus punya kalimat “so what?” satu baris: “Apa artinya bagi saya?”
- Sediakan tooltips simpel (judul, nilai, jumlah responden). Jangan penuh teks kecil.
- Gunakan warna kontras yang mudah dibaca. Hindari hanya membedakan warna merah–hijau tanpa label.

Lihat contoh visual dan kode siap jalan di: `notebooks/dashboard_panels_demo.ipynb`.
