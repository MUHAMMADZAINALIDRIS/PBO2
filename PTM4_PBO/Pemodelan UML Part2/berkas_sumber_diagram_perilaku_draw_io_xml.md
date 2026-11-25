<mxfile host="app.diagrams.net" modified="2026-11-25T04:58:00.000Z" agent="Gemini" version="24.0.0" type="device">
  <diagram id="act_praktikum" name="1. Activity - Praktikum">
    <mxGraphModel dx="1100" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="pool_p" value="Activity Diagram Pengajuan dan Penyerahan Buku" style="swimlane;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;horizontal=1;startSize=30;horizontalStack=1;html=1;fontStyle=1;fontSize=12;fillColor=#f1f5f9;strokeColor=#1e293b;" vertex="1" parent="1">
          <mxGeometry x="40" y="30" width="740" height="720" as="geometry" />
        </mxCell>
        <mxCell id="lane_mhs" value="Mahasiswa" style="swimlane;html=1;startSize=28;horizontal=1;fillColor=#ffffff;strokeColor=#475569;fontStyle=1;fontSize=11;" vertex="1" parent="pool_p">
          <mxGeometry y="30" width="240" height="690" as="geometry" />
        </mxCell>
        <mxCell id="init_p" value="" style="ellipse;html=1;shape=startState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="lane_mhs">
          <mxGeometry x="105" y="45" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="act_m1" value="Ajukan peminjaman" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_mhs">
          <mxGeometry x="45" y="105" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="act_m2" value="Terima pesan kesalahan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_mhs">
          <mxGeometry x="45" y="195" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="end_m1" value="" style="ellipse;html=1;shape=endState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="lane_mhs">
          <mxGeometry x="105" y="275" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="act_m3" value="Terima buku dan bukti pinjam" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_mhs">
          <mxGeometry x="45" y="555" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="end_m2" value="" style="ellipse;html=1;shape=endState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="lane_mhs">
          <mxGeometry x="105" y="635" width="30" height="30" as="geometry" />
        </mxCell>

        <mxCell id="lane_sys" value="Sistem" style="swimlane;html=1;startSize=28;horizontal=1;fillColor=#ffffff;strokeColor=#475569;fontStyle=1;fontSize=11;" vertex="1" parent="pool_p">
          <mxGeometry x="240" width="260" height="690" as="geometry" />
        </mxCell>
        <mxCell id="act_s1" value="Periksa anggota dan stok" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_sys">
          <mxGeometry x="50" y="105" width="160" height="45" as="geometry" />
        </mxCell>
        <mxCell id="dec_s1" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;" vertex="1" parent="lane_sys">
          <mxGeometry x="105" y="192" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="act_s2" value="Simpan permohonan&#xa;MenungguPersetujuan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_sys">
          <mxGeometry x="45" y="285" width="170" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_s3" value="Simpan status Ditolak&#xa;dan alasan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_sys">
          <mxGeometry x="45" y="375" width="170" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_s4" value="Tampilkan penolakan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_sys">
          <mxGeometry x="45" y="450" width="170" height="42" as="geometry" />
        </mxCell>
        <mxCell id="end_s1" value="" style="ellipse;html=1;shape=endState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="lane_sys">
          <mxGeometry x="115" y="510" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="act_s5" value="Simpan Dipinjam, kurangi stok 1,&#xa;tetapkan jatuh tempo" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=10.5;" vertex="1" parent="lane_sys">
          <mxGeometry x="35" y="553" width="190" height="50" as="geometry" />
        </mxCell>

        <mxCell id="lane_pet" value="Petugas" style="swimlane;html=1;startSize=28;horizontal=1;fillColor=#ffffff;strokeColor=#475569;fontStyle=1;fontSize=11;" vertex="1" parent="pool_p">
          <mxGeometry x="500" width="240" height="690" as="geometry" />
        </mxCell>
        <mxCell id="act_p1" value="Periksa permohonan&#xa;dan stok terkini" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_pet">
          <mxGeometry x="40" y="285" width="160" height="48" as="geometry" />
        </mxCell>
        <mxCell id="dec_p1" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;" vertex="1" parent="lane_pet">
          <mxGeometry x="95" y="374" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="act_p2" value="Konfirmasi penyerahan buku" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontSize=11;" vertex="1" parent="lane_pet">
          <mxGeometry x="40" y="470" width="160" height="48" as="geometry" />
        </mxCell>

        <mxCell id="e1" edge="1" parent="pool_p" source="init_p" target="act_m1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" edge="1" parent="pool_p" source="act_m1" target="act_s1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" edge="1" parent="pool_p" source="act_s1" target="dec_s1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="[tidak]" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" parent="pool_p" source="dec_s1" target="act_m2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" edge="1" parent="pool_p" source="act_m2" target="end_m1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="[ya]" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" parent="pool_p" source="dec_s1" target="act_s2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" edge="1" parent="pool_p" source="act_s2" target="act_p1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" edge="1" parent="pool_p" source="act_p1" target="dec_p1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="[tidak]" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" parent="pool_p" source="dec_p1" target="act_s3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e10" edge="1" parent="pool_p" source="act_s3" target="act_s4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e11" edge="1" parent="pool_p" source="act_s4" target="end_s1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e12" value="[ya]" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" parent="pool_p" source="dec_p1" target="act_p2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e13" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="pool_p" source="act_p2" target="act_s5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e14" edge="1" parent="pool_p" source="act_s5" target="act_m3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e15" edge="1" parent="pool_p" source="act_m3" target="end_m2"><mxGeometry relative="1" as="geometry" /></mxCell>
      </root>
    </mxGraphModel>
  </diagram>

  <diagram id="seq_praktikum" name="2. Sequence - Praktikum">
    <mxGraphModel dx="1100" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="ll_mhs" value="Mahasiswa" style="shape=umlLifeline;participant=umlActor;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;verticalAlign=top;spacingTop=36;outlineConnect=0;size=40;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="30" height="460" as="geometry" />
        </mxCell>
        <mxCell id="ll_form" value="form:FormPinjam" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#eff6ff;strokeColor=#1e293b;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="40" width="120" height="460" as="geometry" />
        </mxCell>
        <mxCell id="ll_lay" value="layanan:LayananPinjam" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#eff6ff;strokeColor=#1e293b;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="410" y="40" width="140" height="460" as="geometry" />
        </mxCell>
        <mxCell id="ll_repo" value="repo:Repositori" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#eff6ff;strokeColor=#1e293b;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="620" y="40" width="120" height="460" as="geometry" />
        </mxCell>
        <mxCell id="alt_frame" value="alt" style="shape=umlFrame;whiteSpace=wrap;html=1;pointerEvents=0;width=45;height=24;fillColor=none;strokeColor=#1e293b;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="230" width="670" height="230" as="geometry" />
        </mxCell>
        <mxCell id="guard_ok" value="[anggota aktif dan stok &gt; 0]" style="text;html=1;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="105" y="233" width="180" height="20" as="geometry" />
        </mxCell>
        <mxCell id="alt_div" value="" style="line;strokeWidth=1;dashed=1;labelPosition=center;verticalLabelPosition=bottom;align=left;verticalAlign=top;spacingLeft=20;spacingTop=4;html=1;strokeColor=#1e293b;" vertex="1" parent="1">
          <mxGeometry x="50" y="365" width="670" height="10" as="geometry" />
        </mxCell>
        <mxCell id="guard_else" value="[else]" style="text;html=1;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="65" y="375" width="60" height="20" as="geometry" />
        </mxCell>
        <mxCell id="m1" value="1: ajukan(idBuku)" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="95" y="115" as="sourcePoint" /><mxPoint x="280" y="115" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m2" value="2: ajukan(idAnggota, idBuku)" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="280" y="145" as="sourcePoint" /><mxPoint x="480" y="145" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m3" value="3: bacaAnggotaDanStok()" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="480" y="175" as="sourcePoint" /><mxPoint x="680" y="175" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m4" value="4: dataAnggota, stok" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="680" y="205" as="sourcePoint" /><mxPoint x="480" y="205" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m5" value="5: simpan(MenungguPersetujuan)" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="480" y="270" as="sourcePoint" /><mxPoint x="680" y="270" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m6" value="6: nomorPermohonan" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="680" y="298" as="sourcePoint" /><mxPoint x="480" y="298" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m7" value="7: nomorPermohonan" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="480" y="325" as="sourcePoint" /><mxPoint x="280" y="325" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m8" value="8: tampilkan nomor permohonan" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="280" y="352" as="sourcePoint" /><mxPoint x="95" y="352" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m9" value="9: pesanKesalahan" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="480" y="405" as="sourcePoint" /><mxPoint x="280" y="405" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="m10" value="10: tampilkan kesalahan" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry"><mxPoint x="280" y="438" as="sourcePoint" /><mxPoint x="95" y="438" as="targetPoint" /></mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>

  <diagram id="stm_mandiri" name="3. Statechart - PengajuanSurat">
    <mxGraphModel dx="1100" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="st_init" value="" style="ellipse;html=1;shape=startState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="1">
          <mxGeometry x="385" y="30" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="st_wait" value="MenungguVerifikasi" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="315" y="95" width="170" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_rev" value="PerluRevisi" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="70" y="195" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_batal" value="Dibatalkan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="70" y="315" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_tolak" value="Ditolak" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="580" y="195" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_proses" value="Diproses" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="325" y="210" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_ttd" value="MenungguTandaTangan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="310" y="315" width="180" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_unduh" value="SiapDiunduh" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="325" y="420" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_selesai" value="Selesai" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#eff6ff;strokeColor=#1e293b;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="325" y="520" width="150" height="45" as="geometry" />
        </mxCell>
        <mxCell id="st_fin_main" value="" style="ellipse;html=1;shape=endState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="1">
          <mxGeometry x="385" y="600" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="st_fin_batal" value="" style="ellipse;html=1;shape=endState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="1">
          <mxGeometry x="130" y="395" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="st_fin_tolak" value="" style="ellipse;html=1;shape=endState;fillColor=#1e293b;strokeColor=#1e293b;" vertex="1" parent="1">
          <mxGeometry x="640" y="280" width="30" height="30" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>