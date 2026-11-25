<mxfile host="app.diagrams.net" modified="2026-11-24T00:00:00.000Z" agent="UML Generator" version="21.0.0" type="device">
  <!-- DIAGRAM 1: Use Case Diagram Praktikum Perpustakaan -->
  <diagram id="diag-praktikum-uc" name="Praktikum - Use Case Diagram">
    <mxGraphModel dx="1000" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- System Boundary -->
        <mxCell id="sys_bound_1" value="Sistem Peminjaman Perpustakaan" style="shape=rect;html=1;verticalAlign=top;align=center;whiteSpace=wrap;fillColor=#f8fafc;strokeColor=#475569;strokeWidth=1.5;fontStyle=1;fontSize=14;fontColor=#0f172a;" vertex="1" parent="1">
          <mxGeometry x="180" y="40" width="460" height="420" as="geometry" />
        </mxCell>

        <!-- Aktor -->
        <mxCell id="actor_mhs" value="Mahasiswa" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="210" width="40" height="80" as="geometry" />
        </mxCell>
        <mxCell id="actor_petugas" value="Petugas Perpustakaan" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="700" y="240" width="40" height="80" as="geometry" />
        </mxCell>

        <!-- Use Cases -->
        <mxCell id="uc_cari" value="Cari Buku" style="ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="80" width="140" height="50" as="geometry" />
        </mxCell>
        <mxCell id="uc_ajukan" value="Ajukan Peminjaman" style="ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="150" width="140" height="50" as="geometry" />
        </mxCell>
        <mxCell id="uc_validasi" value="Validasi Anggota&#xa;dan Stok" style="ellipse;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=1.5;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="460" y="150" width="150" height="50" as="geometry" />
        </mxCell>
        <mxCell id="uc_email" value="Kirim Notifikasi Email" style="ellipse;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=1.5;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="220" y="225" width="140" height="45" as="geometry" />
        </mxCell>
        <mxCell id="uc_batal" value="Batalkan Permohonan" style="ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="290" width="140" height="50" as="geometry" />
        </mxCell>
        <mxCell id="uc_lihat" value="Lihat Status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="360" width="140" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="uc_putus" value="Putuskan Permohonan" style="ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="460" y="240" width="150" height="50" as="geometry" />
        </mxCell>
        <mxCell id="uc_cekstok" value="Periksa Status&#xa;dan Stok Terkini" style="ellipse;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=1.5;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="460" y="320" width="150" height="50" as="geometry" />
        </mxCell>
        <mxCell id="uc_kembali" value="Catat Pengembalian" style="ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="460" y="390" width="150" height="50" as="geometry" />
        </mxCell>

        <!-- Asosiasi Mahasiswa -->
        <mxCell id="edge_m1" edge="1" parent="1" source="actor_mhs" target="uc_cari"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="edge_m2" edge="1" parent="1" source="actor_mhs" target="uc_ajukan"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="edge_m3" edge="1" parent="1" source="actor_mhs" target="uc_batal"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="edge_m4" edge="1" parent="1" source="actor_mhs" target="uc_lihat"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Asosiasi Petugas -->
        <mxCell id="edge_p1" edge="1" parent="1" source="actor_petugas" target="uc_putus"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="edge_p2" edge="1" parent="1" source="actor_petugas" target="uc_kembali"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relasi Include & Extend -->
        <mxCell id="edge_inc1" value="«include»" style="endArrow=open;endSize=8;dashed=1;html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="uc_ajukan" target="uc_validasi"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="edge_inc2" value="«include»" style="endArrow=open;endSize=8;dashed=1;html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="uc_putus" target="uc_cekstok"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="edge_ext1" value="«extend»" style="endArrow=open;endSize=8;dashed=1;html=1;verticalAlign=bottom;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="uc_email" target="uc_ajukan"><mxGeometry relative="1" as="geometry" /></mxCell>
      </root>
    </mxGraphModel>
  </diagram>

  <!-- DIAGRAM 2: Class Diagram Praktikum Perpustakaan -->
  <diagram id="diag-praktikum-class" name="Praktikum - Class Diagram">
    <mxGraphModel dx="1000" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Class Mahasiswa -->
        <mxCell id="c_mhs" value="Mahasiswa&#xa;--&#xa;- nim: String&#xa;- nama: String&#xa;- aktif: Boolean&#xa;--&#xa;+ isAktif(): Boolean" style="swipeable=0;html=1;shape=mxgraph.bootstrap.rrect;rSize=5;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;align=center;verticalAlign=top;whiteSpace=wrap;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="60" y="80" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Class PermohonanPeminjaman -->
        <mxCell id="c_permohonan" value="PermohonanPeminjaman&#xa;--&#xa;- idPermohonan: String&#xa;- tglPengajuan: Date&#xa;- status: StatusEnum&#xa;- jatuhTempo: Date [0..1]&#xa;- tglKembali: Date [0..1]&#xa;- alasanPenolakan: String [0..1]&#xa;--&#xa;+ batalkan(): void&#xa;+ tolak(alasan: String): void&#xa;+ setujui(): void&#xa;+ kembalikan(): void" style="swipeable=0;html=1;shape=mxgraph.bootstrap.rrect;rSize=5;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;align=center;verticalAlign=top;whiteSpace=wrap;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="320" y="50" width="220" height="180" as="geometry" />
        </mxCell>

        <!-- Class Buku -->
        <mxCell id="c_buku" value="Buku&#xa;--&#xa;- idBuku: String&#xa;- judul: String&#xa;- stokTersedia: Int&#xa;--&#xa;+ tersedia(): Boolean" style="swipeable=0;html=1;shape=mxgraph.bootstrap.rrect;rSize=5;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;align=center;verticalAlign=top;whiteSpace=wrap;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="60" y="270" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Class Petugas -->
        <mxCell id="c_petugas" value="Petugas&#xa;--&#xa;- idPetugas: String&#xa;- nama: String&#xa;--&#xa;+ verifikasi(): void" style="swipeable=0;html=1;shape=mxgraph.bootstrap.rrect;rSize=5;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;align=center;verticalAlign=top;whiteSpace=wrap;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="350" y="270" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Asosiasi -->
        <mxCell id="rel_mhs_perm" value="diajukan oleh" style="endArrow=none;html=1;fontSize=10;" edge="1" parent="1" source="c_mhs" target="c_permohonan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="mult_mhs" value="1" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontStyle=1;" vertex="1" parent="rel_mhs_perm">
          <mxGeometry x="-0.7" y="-10" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="mult_perm1" value="0..*" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontStyle=1;" vertex="1" parent="rel_mhs_perm">
          <mxGeometry x="0.7" y="-10" width="30" height="20" as="geometry" />
        </mxCell>

        <mxCell id="rel_buku_perm" value="merujuk" style="endArrow=none;html=1;fontSize=10;" edge="1" parent="1" source="c_buku" target="c_permohonan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="rel_petugas_perm" value="diputuskan oleh" style="endArrow=none;html=1;fontSize=10;" edge="1" parent="1" source="c_petugas" target="c_permohonan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="mult_petugas" value="0..1" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontStyle=1;" vertex="1" parent="rel_petugas_perm">
          <mxGeometry x="-0.7" y="-10" width="30" height="20" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>