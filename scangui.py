import streamlit as st

# Panel admin password
ADMIN_PASSWORD = "120407"

# Function to send a message to the admin panel
def send_message(sender_name, message_content):
    with open("messages.txt", "a") as file:
        file.write(f"{sender_name}: {message_content}\n")

def main():
    st.title("Aplikasi Kirim Pesan dengan Panel Admin")
    
    # Create a sidebar
    st.sidebar.title("Menu")
    menu_selection = st.sidebar.radio("Pilih Halaman:", ("Kirim Pesan", "Panel Admin"))

   if menu_selection == "Panel Admin":
        # Check if the user is the admin
        password_input = st.text_input("Masukkan kata sandi:", type="password")
        if password_input == ADMIN_PASSWORD:
            st.subheader("Panel Admin")
            with open("messages.txt", "r") as file:
                messages = file.read()
            st.text_area("Pesan yang Dikirim", messages, height=200)
        elif password_input:
            st.warning("Kata sandi salah. Panel Admin tidak dapat diakses.")
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
    main()
