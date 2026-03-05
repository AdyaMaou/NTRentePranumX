import streamlit as st

# Pengaturan Judul Aplikasi
st.set_page_config(page_title="Kalkulator Rente Pranumerando", page_icon="💰", initial_sidebar_state="expanded")


st.title("💰 Kalkulator Nilai Tunai Rente Pranumerando")
st.write("Aplikasi simpel untuk menghitung nilai tunai dari modal yang dibayarkan di setiap awal periode.")

# Sidebar untuk input
st.sidebar.header("Input Parameter")

modal = st.sidebar.number_input("Besar Angsuran (a):", min_value=0.0, value=1000000.0, step=50000.0)
bunga_persen = st.sidebar.number_input("Suku Bunga per Periode (%):", min_value=0.0, value=5.0, step=0.1)
periode = st.sidebar.number_input("Jumlah Periode (n):", min_value=1, value=10, step=1)

# Perhitungan
i = bunga_persen / 100

if st.button("Hitung Nilai Tunai"):
    if i > 0:
        # Rumus Rente Pranumerando
        nilai_tunai = modal * ((1 - (1 + i)**-periode) / i) * (1 + i)
        
        # Tampilan Hasil
        st.success(f"### Hasil Perhitungan")
        st.metric(label="Total Nilai Tunai", value=f"Rp {nilai_tunai:,.2f}")
        
        with st.expander("Lihat Rincian Parameter"):
            st.write(f"- Modal per periode: **Rp {modal:,.2f}**")
            st.write(f"- Suku bunga: **{bunga_persen}%**")
            st.write(f"- Durasi: **{periode} periode**")
    else:
        st.error("Suku bunga harus lebih besar dari 0.")

st.info("Catatan: Pastikan satuan bunga dan periode sudah sinkron (misal: bunga per tahun dan durasi dalam tahun).")

st.sidebar.markdown("---")
with st.sidebar.expander("✨ Dibuat oleh Kelompok 3"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("Adyanur Yahya (1)")
        st.caption("Anastasya Putri (5)")
    with col2:
        st.caption("Angga Saputra (6)")
        st.caption("Desvita Putri (10)")
    with col3:
        st.caption("M. Daffin H. (21)")
        st.caption("Shafira Citra (31)")
