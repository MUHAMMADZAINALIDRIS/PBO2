import re
from app import app

c = app.test_client()
assert c.get('/portofolio').status_code == 302          # terkunci tanpa login

html = c.get('/login').get_data(as_text=True)
token = re.search(r'name=.csrf. value=.([0-9a-f]+)', html).group(1)

data = {'username': 'mahasiswa', 'password': 'praktikum123', 'csrf': token}
assert c.post('/login', data=data).status_code == 302   # berhasil masuk
assert c.get('/portofolio').status_code == 200          # kini terbuka
print('Semua uji lulus')