# Portofolio Flask

Aplikasi web portofolio dengan alur: **splash screen, beranda, login, lalu halaman portofolio** yang animatif.
Dibuat dengan Python + Flask, HTML, CSS, dan JavaScript murni (tanpa framework CSS atau JS).

## Menjalankan

```bash
python -m venv venv
# Windows (CMD): venv\Scripts\activate    |   Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Buka http://127.0.0.1:5000

Akun demo: **username** `mahasiswa`, **password** `praktikum123`

## Alur halaman

| URL | Fungsi | Perlu login |
|---|---|---|
| `/` | splash screen, otomatis menuju beranda | tidak |
| `/beranda` | halaman sambutan dengan tombol Masuk | tidak |
| `/login` | formulir masuk | tidak |
| `/portofolio` | portofolio lengkap | ya |
| `/logout` | keluar (hanya metode POST) | tidak |

## Mengganti data dengan milik Anda

1. Ubah isi `PROFIL` di `data.py` (nama, peran, skill, proyek, pengalaman, kontak).
2. Ubah warna di `static/css/base.css` pada blok `:root` (`--biru`, `--jingga`, dan seterusnya).
3. Ubah akun di `USERS` pada `app.py`.
4. Untuk penggunaan nyata, isi variabel lingkungan `SECRET_KEY` dengan teks acak yang panjang.

## Struktur

```
app.py                 route, login, session, proteksi halaman
data.py                data profil (satu-satunya tempat mengedit isi)
templates/             base.html, splash, beranda, login, portofolio, _flash.html
static/css/            base.css, splash.css, publik.css, portofolio.css
static/js/             splash.js, ketik.js, login.js, portofolio.js
```
