# Simulasi Reservasi Laboratorium

Proyek latihan percabangan Python dan antarmuka web Flask. Kapasitas dan aturan adalah **simulasi pembelajaran**, bukan kebijakan resmi kampus.

## Windows

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Jika PowerShell menolak aktivasi, gunakan Command Prompt dan jalankan `.venv\Scripts\activate.bat`.

## macOS atau Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Buka `http://127.0.0.1:5000` di browser. Program memerlukan Python 3.10 atau lebih baru untuk sintaks `match-case`. `debug=True` hanya untuk praktik lokal.
