from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


class Kendaraan:
    """Merepresentasikan satu objek kendaraan."""

    def __init__(self, nomor_polisi, merk, model, tahun, warna, jenis):
        self.nomor_polisi = nomor_polisi
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.warna = warna
        self.jenis = jenis

    def tampilkan_data(self):
        return (
            f"{self.nomor_polisi} - "
            f"{self.merk} {self.model} - "
            f"{self.tahun} - "
            f"{self.warna} - "
            f"{self.jenis}"
        )


# Penyimpanan sementara di memori
data_kendaraan = [
    Kendaraan(
        "D 3571 GG",
        "BYD",
        "Sport",
        2026,
        "Hitam",
        "Mobil"
    ),
    Kendaraan(
        "D 5678 XYZ",
        "Honda",
        "Ducati",
        2027,
        "Maroon",
        "Motor"
    ),
]


@app.route("/", methods=["GET", "POST"])
def index():
    pesan = None

    if request.method == "POST":
        nomor_polisi = request.form.get("nomor_polisi", "").strip()
        merk = request.form.get("merk", "").strip()
        model = request.form.get("model", "").strip()
        tahun = request.form.get("tahun", "").strip()
        warna = request.form.get("warna", "").strip()
        jenis = request.form.get("jenis", "").strip()

        if not nomor_polisi or not merk or not model or not tahun or not warna or not jenis:
            pesan = "Semua field wajib diisi."

        elif any(
            k.nomor_polisi.lower() == nomor_polisi.lower()
            for k in data_kendaraan
        ):
            pesan = "Nomor polisi sudah terdaftar."

        else:
            kendaraan = Kendaraan(
                nomor_polisi,
                merk,
                model,
                tahun,
                warna,
                jenis
            )

            data_kendaraan.append(kendaraan)

            return redirect(url_for("index"))

    return render_template(
        "index.html",
        kendaraan=data_kendaraan,
        pesan=pesan
    )


@app.route("/hapus/<nomor_polisi>", methods=["POST"])
def hapus(nomor_polisi):
    global data_kendaraan

    data_kendaraan = [
        k for k in data_kendaraan
        if k.nomor_polisi != nomor_polisi
    ]

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
