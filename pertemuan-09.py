import streamlit as st


#Ini bagian heading aplikasi Streamlit
st.title("Kuliah Praktikum Big Data")
st.write("Gabriella")
st.write("# Heading 1")

#Kinerja unit
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)
st.metric("Saham", 100, 20)

#Pilihan
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

"""
Ini komentar harusnya
"""

makanan = st.radio('Makanan kesukaan', ['Bakso', 'Nasi goreng', 'Mie ayam'])

st.write(makanan)

minuman = st.selectbox('Pilih minuman yang akan dipesan',['Es teh', 'Kopi', 'Jus'])

st.write(minuman)

bayar = st.multiselect('Bayar pakai', ['Tunai', 'OVO', 'GoPay'])

st.write(bayar)
