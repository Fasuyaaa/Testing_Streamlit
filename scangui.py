import streamlit as st
import base64
import bcrypt

ADMIN_PASSWORD_ENCODED = b'MTIz'  

# Function untuk mendecode password admin
def decode_password(encoded_password):
    return base64.b64decode(encoded_password).decode()

# Function untuk mengenkripsi password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

# Function untuk memverifikasi password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)

def main():
    st.title("Aplikasi Kirim Pesan dengan Panel Admin")
    
    # Create a sidebar
    st.sidebar.title("Menu")
    menu_selection = st.sidebar.radio("Pilih Halaman:", ("Kirim Pesan", "Panel Admin"))

    if menu_selection == "Panel Admin":
        # Check if the user is the admin
        password_input = st.text_input("Masukkan kata sandi:", type="password")
        if verify_password(password_input, hash_admin_password):
            st.subheader("Panel Admin")
            with open("messages.txt", "r") as file:
                messages = file.read()
            st.text_area("Pesan yang Dikirim", messages, height=200)
        elif password_input:
            st.sidebar.warning("Kata sandi salah. Panel Admin tidak dapat diakses.")
    elif menu_selection == "Kirim Pesan":
        st.subheader("Kirim Pesan")
        sender_name = st.text_input("Nama Pengirim:")
        message_content = st.text_area("Isi Pesan:")

        if st.button("Kirim Pesan"):
            if sender_name and message_content:
                send_message(sender_name, message_content)
                st.success("Pesan berhasil dikirim!")
            else:
                st.warning("Mohon isi nama pengirim dan isi pesan terlebih dahulu.")

if __name__ == "__main__":
    ADMIN_PASSWORD = decode_password(ADMIN_PASSWORD_ENCODED)
    hash_admin_password = hash_password(ADMIN_PASSWORD)
    main()
