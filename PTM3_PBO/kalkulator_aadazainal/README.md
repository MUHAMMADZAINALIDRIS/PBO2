# Kalkulator Hub

Proyek akhir praktikum **Python + Flask: operator dan aritmatika**.
Aplikasi web multi-halaman dengan tampilan responsif (HTML + CSS murni, tanpa framework CSS).

## Menjalankan

```bash
python -m venv venv
# Windows (CMD): venv\Scripts\activate    |   Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Buka http://127.0.0.1:5000

## Halaman dan operator yang dilatih

| Halaman | Operator | Fitur |
|---|---|---|
| /kalkulator | `+ - * / // % **` | validasi input, penanganan error, riwayat (session) |
| /cicilan | `* / **` | bunga flat dan anuitas, jadwal angsuran |
| /bmi | `/ **`, perbandingan berantai | BMI, kategori, rentang berat ideal |

## Struktur

```
app.py                 logika dan route Flask
templates/base.html    kerangka bersama (navbar, footer)
templates/*.html       halaman (mewarisi base.html)
static/css/style.css   seluruh gaya antarmuka
```

## Ide pengembangan

1. Tambahkan halaman Konversi Suhu (Celsius, Fahrenheit, Kelvin).
2. Simpan riwayat ke berkas JSON atau SQLite.
3. Tambahkan pengujian dengan `pytest` dan `app.test_client()`.
