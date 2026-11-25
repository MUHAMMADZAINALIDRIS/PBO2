"""Kalkulator AAZAIN: proyek akhir praktikum operator dan aritmatika (Python + Flask)."""
import math

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'ganti-kunci-ini-saat-deploy'  # dibutuhkan Flask untuk session (riwayat)

# kode: (simbol operator Python, nama, fungsi hitung)
OPERATOR = {
    'tambah': ('+', 'Tambah', lambda a, b: a + b),
    'kurang': ('-', 'Kurang', lambda a, b: a - b),
    'kali': ('*', 'Kali', lambda a, b: a * b),
    'bagi': ('/', 'Bagi', lambda a, b: a / b),
    'bagi_bulat': ('//', 'Bagi bulat', lambda a, b: a // b),
    'sisa': ('%', 'Sisa bagi', lambda a, b: a % b),
    'pangkat': ('**', 'Pangkat', lambda a, b: a ** b),
}
DAFTAR_OPERATOR = [
    {'kode': kode, 'simbol': data[0], 'nama': data[1]} for kode, data in OPERATOR.items()
]


# ---------------------------------------------------------------- fungsi bantu
def format_id(nilai, desimal=0):
    """Format angka gaya Indonesia: titik untuk ribuan, koma untuk desimal."""
    teks = f'{nilai:,.{desimal}f}'
    return teks.replace(',', '#').replace('.', ',').replace('#', '.')


def format_hasil(nilai):
    """Bilangan bulat tampil tanpa desimal; selain itu maksimal 6 angka di belakang koma."""
    if float(nilai).is_integer():
        return format_id(nilai, 0)
    if abs(nilai) < 1e-6:
        return f'{nilai:.3e}'
    return format_id(nilai, 6).rstrip('0').rstrip(',')


def ke_angka(teks):
    """Ubah teks input menjadi float. Koma desimal gaya Indonesia diterima."""
    try:
        angka = float(teks.strip().replace(',', '.'))
    except ValueError:
        raise ValueError('Masukkan angka yang valid.') from None
    if not math.isfinite(angka):
        raise ValueError('Masukkan angka yang valid.')
    return angka


def catat_riwayat(teks):
    riwayat = session.get('riwayat', [])
    session['riwayat'] = ([teks] + riwayat)[:8]  # simpan 8 perhitungan terakhir


@app.template_filter('rupiah')
def rupiah(nilai):
    return 'Rp ' + format_id(nilai, 0)


@app.template_filter('angka')
def angka(nilai, desimal=0):
    return format_id(nilai, desimal)


def hitung_cicilan(pinjaman, bunga, tenor, metode):
    """Hitung angsuran bulanan dengan metode bunga flat atau anuitas."""
    r = bunga / 100 / 12  # bunga per bulan

    if metode == 'flat':
        bunga_total = pinjaman * (bunga / 100) * (tenor / 12)
        angsuran = (pinjaman + bunga_total) / tenor
    else:
        if r == 0:
            angsuran = pinjaman / tenor
        else:
            angsuran = pinjaman * r / (1 - (1 + r) ** -tenor)
        bunga_total = angsuran * tenor - pinjaman

    jadwal = []
    sisa = pinjaman
    for bulan in range(1, min(tenor, 12) + 1):
        if metode == 'flat':
            bunga_bulan = bunga_total / tenor
            pokok = pinjaman / tenor
        else:
            bunga_bulan = sisa * r
            pokok = angsuran - bunga_bulan
        sisa -= pokok
        jadwal.append({'bulan': bulan, 'pokok': pokok, 'bunga': bunga_bulan, 'sisa': max(sisa, 0)})

    return {
        'angsuran': angsuran,
        'bunga_total': bunga_total,
        'total_bayar': pinjaman + bunga_total,
        'pinjaman': pinjaman,
        'tenor': tenor,
        'bunga': bunga,
        'metode': 'Bunga flat' if metode == 'flat' else 'Anuitas (bunga efektif)',
        'jadwal': jadwal,
    }


# --------------------------------------------------------------------- halaman
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    form = {'a': '', 'b': '', 'op': 'tambah'}
    hasil = ekspresi = error = None

    if request.method == 'POST':
        form = {kunci: request.form.get(kunci, awal) for kunci, awal in form.items()}
        try:
            a = ke_angka(form['a'])
            b = ke_angka(form['b'])
            simbol, _, fungsi = OPERATOR[form['op']]
            nilai = fungsi(a, b)
            if isinstance(nilai, complex):
                raise ValueError('Hasilnya bukan bilangan real.')
            ekspresi = f'{format_hasil(a)} {simbol} {format_hasil(b)}'
            hasil = format_hasil(nilai)
            catat_riwayat(f'{ekspresi} = {hasil}')
        except KeyError:
            error = 'Operator tidak dikenal.'
        except ZeroDivisionError:
            error = 'Tidak bisa membagi dengan nol.'
        except OverflowError:
            error = 'Hasil terlalu besar untuk dihitung.'
        except ValueError as e:
            error = str(e)

    return render_template(
        'kalkulator.html', form=form, hasil=hasil, ekspresi=ekspresi, error=error,
        riwayat=session.get('riwayat', []), daftar_operator=DAFTAR_OPERATOR,
    )


@app.route('/riwayat/hapus', methods=['POST'])
def hapus_riwayat():
    session.pop('riwayat', None)
    return redirect(url_for('kalkulator'))


@app.route('/cicilan', methods=['GET', 'POST'])
def cicilan():
    form = {'pinjaman': '50000000', 'bunga': '12', 'tenor': '24', 'metode': 'flat'}
    hasil = error = None

    if request.method == 'POST':
        form = {kunci: request.form.get(kunci, awal) for kunci, awal in form.items()}
        try:
            pinjaman = ke_angka(form['pinjaman'])
            bunga = ke_angka(form['bunga'])
            tenor = int(ke_angka(form['tenor']))
            if not 0 < pinjaman <= 1e13:
                raise ValueError('Jumlah pinjaman harus lebih dari 0 dan maksimal Rp 10 triliun.')
            if not 0 <= bunga <= 100:
                raise ValueError('Bunga harus di antara 0 dan 100 persen per tahun.')
            if not 1 <= tenor <= 360:
                raise ValueError('Tenor harus di antara 1 dan 360 bulan.')
            hasil = hitung_cicilan(pinjaman, bunga, tenor, form['metode'])
        except ValueError as e:
            error = str(e)

    return render_template('cicilan.html', form=form, hasil=hasil, error=error)


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    form = {'berat': '', 'tinggi': ''}
    hasil = error = None

    if request.method == 'POST':
        form = {kunci: request.form.get(kunci, awal) for kunci, awal in form.items()}
        try:
            berat = ke_angka(form['berat'])
            tinggi_cm = ke_angka(form['tinggi'])
            if not 20 <= berat <= 300:
                raise ValueError('Berat badan harus di antara 20 dan 300 kg.')
            if not 100 <= tinggi_cm <= 250:
                raise ValueError('Tinggi badan harus di antara 100 dan 250 cm.')

            tinggi = tinggi_cm / 100  # cm menjadi meter
            nilai = berat / tinggi ** 2

            if nilai < 18.5:
                kategori, nada = 'Berat badan kurang', 'kurang'
            elif nilai < 25:
                kategori, nada = 'Normal', 'normal'
            elif nilai < 30:
                kategori, nada = 'Berat badan berlebih', 'lebih'
            else:
                kategori, nada = 'Obesitas', 'obesitas'

            hasil = {
                'nilai': format_id(nilai, 1),
                'kategori': kategori,
                'nada': nada,
                'posisi': min(max((nilai - 15) / (40 - 15) * 100, 0), 100),  # skala 15 sampai 40
                'ideal_min': format_id(18.5 * tinggi ** 2, 1),
                'ideal_maks': format_id(24.9 * tinggi ** 2, 1),
            }
        except ValueError as e:
            error = str(e)

    return render_template('bmi.html', form=form, hasil=hasil, error=error)


if __name__ == '__main__':
    app.run(debug=True)
