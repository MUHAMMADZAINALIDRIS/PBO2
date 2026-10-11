from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


class Mahasiswa:
    """Merepresentasikan satu objek mahasiswa."""

    def __init__(self, nim, nama, prodi, semester):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.semester = semester


    def tampilkan_data(self):
        return f"{self.nim} - {self.nama} - {self.prodi} - {self.semester}"


# Penyimpanan sementara di memori (belum menggunakan database)
data_mahasiswa = [
    Mahasiswa("20260001", "Budi Santoso", "Teknik Informatika", 2),
    Mahasiswa("20260002", "Siti Aminah", "Teknik Informatika", 4),
]



@app.route("/", methods=["GET", "POST"])
def index():
    pesan = None

    if request.method == "POST":
        nim = request.form.get("nim", "").strip()
        nama = request.form.get("nama", "").strip()
        prodi = request.form.get("prodi", "").strip()
        semester = request.form.get("semester", "").strip()


        if not nim or not nama or not prodi or not semester:
            pesan = "Semua field wajib diisi."
        elif any(m.nim == nim for m in data_mahasiswa):
            pesan = "NIM sudah terdaftar."
        else:
            mahasiswa = Mahasiswa(nim, nama, prodi, semester)
            data_mahasiswa.append(mahasiswa)
            return redirect(url_for("index"))

    return render_template("index.html", mahasiswa=data_mahasiswa, pesan=pesan)


@app.route("/hapus/<nim>", methods=["POST"])
def hapus(nim):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m.nim != nim]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
