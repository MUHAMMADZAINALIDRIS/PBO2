"""Data profil untuk halaman portofolio.

Ganti isi PROFIL dengan data Anda sendiri. Seluruh halaman ikut berubah
karena template hanya membaca data dari sini.
"""

PROFIL = {
    'nama': 'Muhammad Zainal Idris',
    'inisial': 'MZI',
    'peran': ['Full-Stack Web Developer', 'IoT & Robotics Enthusiast', 'Graphic & UI Designer'],  # teks mesin ketik
    'tagline': 'Menggabungkan rekayasa perangkat lunak terstruktur dengan estetika visual yang presisi.',
    'tentang': [
        'Saya mahasiswa Teknik Informatika di STIKOM Poltek Cirebon yang fokus membangun solusi digital fungsional, mulai dari aplikasi web full-stack berbasis PHP/Python & MySQL hingga sistem pakar berbasis logika fuzzy dan prototipe IoT.',
        'Selain pengembangan perangkat lunak, saya aktif di bidang desain grafis (vektor & mockup) serta melatih kepemimpinan dan kedisiplinan tim melalui organisasi kepaskibraan.',
    ],
    'info': [
        ('Lokasi', 'Majalengka, Jawa Barat, Indonesia'),
        ('Email', 'idrszainal11@gmail.com'),
        ('Status', 'Terbuka untuk peluang kerja, magang, & kolaborasi proyek'),
    ],
    'email': 'idrszainal11@gmail.com',
    'statistik': [
        {'angka': 10, 'label': 'Proyek dikembangkan'},
        {'angka': 4, 'label': 'Tahun eksplorasi IT'},
        {'angka': 3, 'label': 'Bidang keahlian utama'},
        {'angka': 5, 'label': 'Kolaborasi tim inti'},
    ],
    'skill': [
        {'nama': 'PHP & MySQL', 'nilai': 90},
        {'nama': 'Python', 'nilai': 85},
        {'nama': 'HTML, CSS & JS', 'nilai': 88},
        {'nama': 'Android (Kotlin)', 'nilai': 75},
        {'nama': 'IoT & Sistem Pakar', 'nilai': 82},
        {'nama': 'Desain Grafis (CorelDRAW)', 'nilai': 88},
    ],
    'teknologi': [
        'PHP', 'Python', 'MySQL', 'Kotlin', 'HTML/CSS', 
        'Fuzzy Logic', 'IoT', 'MATLAB', 'Railway', 'Git', 'CorelDRAW'
    ],
    'proyek': [
        {
            'judul': 'Sistem Pakar Deteksi Dini',
            'deskripsi': 'Aplikasi sistem pakar menggunakan metode Fuzzy Mamdani untuk asesmen dini risiko eksploitasi digital pada remaja.',
            'tag': 'AI / Sistem Pakar', 'ikon': 'Σ', 'hue': 232, 'tautan': '#'
        },
        {
            'judul': 'Sistem Manajemen & Absensi Paskibra',
            'deskripsi': 'Aplikasi web pendataan anggota dan presensi dengan autentikasi NIA menggunakan PHP, MySQL, dan cloud deployment Railway.',
            'tag': 'Web', 'ikon': '</>', 'hue': 160, 'tautan': '#'
        },
        {
            'judul': 'Inkubator Otomatis Berbasis IoT',
            'deskripsi': 'Prototipe perangkat keras dan sistem pemantauan suhu serta kelembapan otomatis berbasis Internet of Things.',
            'tag': 'IoT', 'ikon': '{ }', 'hue': 14, 'tautan': '#'
        },
        {
            'judul': 'Simulasi Kinematika Lengan Robot 3-DOF',
            'deskripsi': 'Pemodelan dan perhitungan Inverse Kinematics untuk konfigurasi sendi RRP dan RPR menggunakan MATLAB.',
            'tag': 'Robotika', 'ikon': '//', 'hue': 285, 'tautan': '#'
        },
        {
            'judul': 'Aplikasi Manajemen Laundry & Reservasi Tiket',
            'deskripsi': 'Sistem informasi berbasis web untuk pengelolaan transaksi operasional laundry dan pemesanan tiket terintegrasi database.',
            'tag': 'Web', 'ikon': '#', 'hue': 38, 'tautan': '#'
        },
        {
            'judul': 'Identitas Visual & Mockup Seragam Taktis',
            'deskripsi': 'Perancangan logo heraldik resmi (BRIDURA & Pandawasha) serta visualisasi mockup 3D seragam lapangan.',
            'tag': 'Desain', 'ikon': 'Aa', 'hue': 200, 'tautan': '#'
        },
    ],
    'pengalaman': [
        {
            'periode': '2026', 'posisi': 'Lead Developer — Sistem Pakar Deteksi Dini (Fuzzy Mamdani)',
            'tempat': 'Proyek Penelitian & Kerja Praktik',
            'uraian': 'Merancang arsitektur basis pengetahuan dan mesin inferensi Fuzzy Mamdani untuk asesmen dini risiko eksploitasi digital pada remaja tingkat SMP.'
        },
        {
            'periode': '2026', 'posisi': 'Full-Stack Web Developer — Sistem Absensi & Manajemen Anggota',
            'tempat': 'Organisasi Paskibra (Pandawasha, BRISAKA & BRIDURA)',
            'uraian': 'Membangun aplikasi web manajemen data anggota dan presensi berbasis autentikasi NIA menggunakan PHP dan MySQL, serta melakukan deployment cloud di Railway.'
        },
        {
            'periode': '2026', 'posisi': 'IoT & Software Developer — Inkubator Otomatis & Sistem Informasi',
            'tempat': 'Proyek Rekayasa Perangkat Keras & Lunak',
            'uraian': 'Mengembangkan sistem kontrol otomatis berbasis IoT untuk inkubator, serta membangun aplikasi web manajemen operasional laundry dan reservasi tiket.'
        },
        {
            'periode': '2025 - Sekarang', 'posisi': 'Founder, Pelatih & Visual Designer',
            'tempat': 'Pandawasha Coach Team & BRISAKA SMPN 1 Sukahaji',
            'uraian': 'Memimpin pembinaan tim inti, menyusun standar latihan organisasi, serta merancang seragam visual (mockup 3D seragam lapangan).'
        },
        {
            'periode': '2025 - Sekarang', 'posisi': 'Founder, Pelatih & Visual Designer',
            'tempat': 'Pandawasha Coach Team & BRIDURA SMPN 2 Rajagaluh',
            'uraian': 'Memimpin pembinaan tim inti, menyusun standar latihan organisasi, serta merancang identitas visual (logo heraldik & mockup 3D seragam lapangan).'
        },
        {
            'periode': '2023 - 2027', 'posisi': 'Mahasiswa Teknik Informatika',
            'tempat': 'STIKOM Poltek Cirebon',
            'uraian': 'Mengembangkan berbagai proyek rekayasa perangkat lunak (Full-Stack Web, Android Kotlin, Basis Data Relasional), kriptografi, hingga robotika.'
        },
    ],
    'sertifikat': [
        {
            'judul': 'Pelatihan & Sertifikasi Pemrograman Web Full-Stack',
            'penerbit': 'Dicoding / Kampus Merdeka',
            'tahun': '2025',
            'kredensial': 'ID: WEB-2025-MZI',
        },
        {
            'judul': 'Dasar Pengembangan Aplikasi Android dengan Kotlin',
            'penerbit': 'Dicoding Indonesia',
            'tahun': '2025',
            'kredensial': 'ID: KTL-2025-MZI',
        },
        {
            'judul': 'Internet of Things (IoT) & Sistem Mikrokontroler',
            'penerbit': 'STIKOM Poltek Cirebon',
            'tahun': '2026',
            'kredensial': 'ID: IOT-2026-MZI',
        },
    ],
    'sosial': [
        {'nama': 'GitHub', 'url': 'https://github.com/MUHAMMADZAINALIDRIS'},
        {'nama': 'LinkedIn', 'url': 'https://www.linkedin.com/in/muhammad-zainal-idris-123296450'},
        {'nama': 'Instagram', 'url': 'https://www.instagram.com/zainalidriss'},
    ],
}