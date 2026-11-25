"""Simulasi evaluasi reservasi laboratorium untuk praktikum percabangan."""

from flask import Flask, render_template, request

app = Flask(__name__)


def kapasitas_lab(lab):
    """match-case memilih satu kapasitas menurut pilihan laboratorium."""
    match lab:
        case "komputer":
            return 30
        case "jaringan":
            return 20
        case "iot":
            return 15
        case "multimedia":
            return 25
        case _:
            return None


def evaluasi(lab, kegiatan, peserta, durasi, pendamping):
    kapasitas = kapasitas_lab(lab)
    alasan = []

    if kapasitas is None:
        alasan.append("Pilihan laboratorium tidak dikenal.")

    if kegiatan not in ("praktikum", "penelitian", "pelatihan"):
        alasan.append("Jenis kegiatan tidak dikenal.")

    # if-elif-else: klasifikasi jumlah peserta terhadap kapasitas.
    if peserta <= 0:
        status_peserta = "Jumlah tidak valid"
        alasan.append("Jumlah peserta harus lebih dari nol.")
    elif kapasitas is None:
        status_peserta = "Kapasitas belum diketahui"
    elif peserta > kapasitas:
        status_peserta = "Melebihi kapasitas"
        alasan.append(f"Jumlah peserta melebihi kapasitas {kapasitas} orang.")
    else:
        status_peserta = "Sesuai kapasitas"

    # if-else: batas durasi simulasi 1 sampai 4 jam.
    if 1 <= durasi <= 4:
        durasi_valid = True
    else:
        durasi_valid = False
        alasan.append("Durasi harus antara 1 dan 4 jam.")

    # Kondisi majemuk dengan tanda kurung eksplisit:
    # Praktikum ATAU penggunaan Lab IoT ATAU (Pelatihan dengan peserta > 20) memerlukan pendamping.
    perlu_pendamping = (
        (kegiatan == "praktikum")
        or (lab == "iot")
        or (kegiatan == "pelatihan" and peserta > 20)
    )
    if perlu_pendamping and not pendamping:
        alasan.append("Kegiatan ini memerlukan pendamping dosen.")

    memenuhi = len(alasan) == 0 and durasi_valid
    return {
        "status": "Memenuhi syarat simulasi" if memenuhi else "Belum memenuhi syarat",
        "memenuhi": memenuhi,
        "kapasitas": kapasitas,
        "status_peserta": status_peserta,
        "perlu_pendamping": perlu_pendamping,
        "alasan": alasan,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    data = {"lab": "", "kegiatan": "", "peserta": "", "durasi": "",
            "pendamping": "tidak"}
    hasil = None
    error = None

    if request.method == "POST":
        data = {k: request.form.get(k, "").strip().lower() for k in data}
        try:
            peserta = int(data["peserta"])
            durasi = int(data["durasi"])
        except ValueError:
            error = "Jumlah peserta dan durasi harus berupa bilangan bulat."
        else:
            if data["pendamping"] not in ("ya", "tidak"):
                error = "Pilihan pendamping tidak dikenal."
            else:
                hasil = evaluasi(data["lab"], data["kegiatan"], peserta,
                                 durasi, data["pendamping"] == "ya")

    return render_template("index.html", data=data, hasil=hasil, error=error)


if __name__ == "__main__":
    app.run(debug=True)