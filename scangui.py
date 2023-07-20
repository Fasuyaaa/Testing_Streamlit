import streamlit as st
import nmap

def main():
    st.title("NMAP SCAN NETWORK")
    nmap_version = nmap.__version__
    st.write(nmap_version)

    selected_option = st.selectbox("Select an option", ["Command list", "Scanning port"])
    if st.button("Try"):
        st.write("You selected:", selected_option)
        if selected_option == "Command list":
            function_option1()
        elif selected_option == "Scanning port":
            function_option2()
        else:
            st.write("Invalid option")

def function_option1():
    st.subheader("Command Line")

def function_option2():
    st.subheader("Scanning Port")
    host = st.text_input("Type Target: ")
    start_port = st.number_input("Start Port (e.g: 0)", min_value=0, max_value=65535, value=0)
    end_port = st.number_input("End Port (e.g: 300)", min_value=0, max_value=65535, value=300)

    if st.button("Scan"):
        progress_bar = st.progress(0)  # Menambahkan progress bar
        output_area = st.empty()  # Membuat area kosong untuk output
        port_range = f"{start_port}-{end_port}"
        net = nmap.PortScanner()
        net.scan(host, port_range)
        count = 1
        for host in net.all_hosts():
            hitungan = str(count)
            output_area.subheader("Host %s" % hitungan)
            output_area.write("Host         : %s (%s)" % (host, net[host].hostname()))
            output_area.write("State        : %s" % net[host].state())
            count += 1
            progress_bar.progress(count / len(net.all_hosts()) * 100)  # Mengupdate progress bar

def function_option3():
    st.write("Function for Option 3")

if __name__ == "__main__":
    main()
