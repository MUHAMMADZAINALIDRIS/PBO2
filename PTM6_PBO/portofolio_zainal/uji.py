"""Pengujian otomatis route, proteksi session, keamanan CSRF, dan error 404."""
import re
from app import app

c = app.test_client()

# 1. Uji proteksi halaman tanpa login (harus redirect 302 ke /login)
res_tanpa_login = c.get('/portofolio')
assert res_tanpa_login.status_code == 302, 'Gagal: /portofolio harus terkunci saat belum login'
assert '/login' in res_tanpa_login.headers['Location']

# 2. Ambil token CSRF dari halaman /login
html_login = c.get('/login').get_data(as_text=True)
match = re.search(r'name=["\']csrf["\']\s+value=["\']([0-9a-f]+)["\']', html_login)
assert match is not None, 'Gagal: Token CSRF tidak ditemukan di form login'
token = match.group(1)

# 3. Uji penolakan login jika token CSRF salah/kosong
res_csrf_salah = c.post('/login', data={
    'username': 'mahasiswa',
    'password': 'praktikum123',
    'csrf': 'token-palsu-123'
})
assert res_csrf_salah.status_code == 200
assert 'Formulir kedaluwarsa' in res_csrf_salah.get_data(as_text=True)

# 4. Uji login berhasil + perlindungan Open Redirect (?next=//evil.com)
res_login_ok = c.post('/login?next=//evil.com', data={
    'username': 'mahasiswa',
    'password': 'praktikum123',
    'csrf': token
})
assert res_login_ok.status_code == 302
assert res_login_ok.headers['Location'].endswith('/portofolio'), 'Gagal: Open redirect tidak ditangkal'

# 5. Uji akses /portofolio setelah login (harus 200 OK & Cache-Control: no-store)
res_porto = c.get('/portofolio')
assert res_porto.status_code == 200, 'Gagal: /portofolio tidak terbuka setelah login'
assert res_porto.headers.get('Cache-Control') == 'no-store'

# 6. Uji halaman 404 kustom
res_404 = c.get('/halaman-ngawur-tidak-ada')
assert res_404.status_code == 404, 'Gagal: Handler 404 belum aktif'

print('Semua 6 skenario pengujian otomatis lulus dengan sukses!')