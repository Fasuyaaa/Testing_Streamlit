import streamlit as st
import smtplib
from email.message import EmailMessage

def send_email(sender_name, message_content):
    # Replace the following variables with your email account details
    email_address = "your_email@gmail.com"
    email_password = "your_email_password"

    msg = EmailMessage()
    msg["Subject"] = "Pesan dari Aplikasi Streamlit"
    msg["From"] = email_address
    msg["To"] = "dhavinf.a@gmail.com"
    msg.set_content(f"{sender_name} mengirim pesan: \n\n{message_content}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_address, email_password)
            server.send_message(msg)
        st.success("Pesan berhasil dikirim!")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat mengirim email: {str(e)}")

def main():
    st.title("Aplikasi Kirim Pesan")
    st.write("Isi form di bawah ini untuk mengirim pesan.")

    sender_name = st.text_input("Nama Pengirim:")
    message_content = st.text_area("Isi Pesan:")

    if st.button("Kirim Pesan"):
        if sender_name and message_content:
            send_email(sender_name, message_content)
        else:
            st.warning("Mohon isi nama pengirim dan isi pesan terlebih dahulu.")

if __name__ == "__main__":
    main()
