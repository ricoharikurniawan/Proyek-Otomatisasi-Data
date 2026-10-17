⚙️ Automated Market Data Pipeline

Selamat datang di repositori Automated Market Data Pipeline. Proyek ini adalah demonstrasi sistem otomatisasi data (data automation) ujung-ke-ujung yang dirancang untuk membantu bisnis mengumpulkan, membersihkan, dan menganalisis data produk secara efisien.

📖 Deskripsi Singkat

Di era digital, ketersediaan data yang akurat dan tepat waktu adalah kunci keunggulan kompetitif. Proyek ini menyimulasikan pipeline data e-commerce dengan mengekstrak katalog produk (termasuk harga, ketersediaan stok, dan kategori) dari API publik secara otomatis. Data mentah kemudian ditransformasi menjadi format yang siap digunakan untuk analisis bisnis, memangkas waktu pengerjaan manual dari berjam-jam menjadi hitungan detik.

✨ Fitur Utama

Ekstraksi Data Otomatis: Menarik data produk secara real-time dari sumber eksternal (menggunakan simulasi dari dummyjson.com).

Transformasi & Pembersihan Data: Mengonversi data mentah berformat JSON menjadi struktur tabel (CSV) yang rapi dan mudah dibaca oleh pemangku kepentingan.

Kalkulasi Metrik Bisnis: Menghitung nilai harga final setelah diskon secara otomatis menggunakan logika terprogram.

Sistem Peringatan Dini (Early Warning): Mendeteksi dan melaporkan daftar produk dengan stok menipis untuk segera ditindaklanjuti (tindakan restock).

Orkestrasi Satu Klik: Seluruh proses, dari penarikan data hingga analisis, digabungkan dan dijalankan hanya dengan mengeksekusi satu skrip tunggal.

🛠️ Teknologi yang Digunakan

Proyek otomatisasi ini dibangun menggunakan bahasa pemrograman Python beserta pustaka analisis data standar industri:

requests: Untuk interaksi web dan ekstraksi data dari RESTful API secara stabil.

pandas: Pustaka utama untuk manipulasi, pembersihan, dan kalkulasi data tabular skala besar.

playwright: Infrastruktur tambahan yang disiapkan untuk otomatisasi web dan ekstraksi data dari situs kompleks yang membutuhkan rendering JavaScript (headless browser automation).

🚀 Cara Menjalankan Proyek

Untuk menguji pipeline ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

Kloning repositori ini:

git clone https://github.com/ricoharikurniawan/Portofolio-Otomatisasi.git
cd Portofolio-Otomatisasi


Instal dependensi yang dibutuhkan:

pip install pandas requests playwright


Jalankan skrip utama:

python main.py


Periksa hasilnya: Buka folder data/ yang dihasilkan secara otomatis untuk melihat raw_umkm_data.json (data mentah) dan clean_umkm_data.csv (data bersih). Ringkasan wawasan bisnis dan peringatan stok akan tercetak langsung di terminal Anda.

💼 Nilai Bisnis untuk Klien

Sebagai seorang Data Automation Specialist, skrip dan sistem seperti ini dirancang untuk menyelesaikan hambatan operasional nyata di perusahaan Anda:

Efisiensi Waktu & Biaya: Menghilangkan kebutuhan entri data manual yang memakan waktu dan rentan terhadap human error. Tim Anda dapat fokus pada analisis strategi, bukan sekadar memindahkan data.

Keputusan Berbasis Data (Data-Driven): Mendapatkan wawasan harga pasar dan peringatan stok secara instan, memungkinkan bisnis merespons dinamika pasar lebih cepat.

Skalabilitas Tinggi: Sistem arsitektur ini dapat dengan mudah disesuaikan (scale-up) untuk memantau ratusan ribu produk di berbagai platform marketplace sesungguhnya (seperti Amazon, Shopee, Tokopedia, atau situs kompetitor).

Tertarik untuk mengotomatisasi aliran data bisnis Anda agar lebih efisien? Mari terhubung dan diskusikan bagaimana solusi otomatisasi dapat menghemat ribuan jam operasional perusahaan Anda.
