from keperluan_modul import *
bg()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def display(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def bubble_sort(self):
        tukar = True
        while tukar:
            tukar = False
            current = self.head
            while current.next:
                if current.data["Tanggal Booking"] > current.next.data["Tanggal Booking"]:
                    current.data, current.next.data = current.next.data, current.data
                    tukar = True
                current = current.next
                
    def bubble_sort_estimate_time(self):
        tukar = True
        while tukar:
            tukar = False
            current = self.head
            while current.next:
                if current.data["Status"] == "Approve" and current.next.data["Status"] == "Approve":
                    if (current.data["Tanggal Booking"] == current.next.data["Tanggal Booking"]):
                        start_time_current = datetime.strptime(str(current.data["Estimasi Waktu Servis"]).split('-')[0], '%H:%M')
                        start_time_next = datetime.strptime(str(current.next.data["Estimasi Waktu Servis"]).split('-')[0], '%H:%M')
                        if start_time_current > start_time_next:
                            current.data, current.next.data = current.next.data, current.data
                            tukar = True
                current = current.next

def load_data():
    return pd.read_csv("data/data server/data_booking.csv")

def simpan_data(df):
    df.to_csv("data/data server/data_booking.csv", index=False)

def display_data_booking(df, status):
    filter_data = df[df["Status"] == status]
    if filter_data.empty:
        st.warning(f"No {status} bookings found.")
    else:
        st.write(f":grey[Antrean {status}]")
        st.dataframe(filter_data[["Kode Servis", "Status"]])

def tampil_detail_servis(df, service_code):
    @st.experimental_dialog("DATA DETAILS")
    def detail(kode_servis, nama, alamat, jk, tlp, no_pol, model_mobil, transmisi, fuel_type, tahun, pkt, tgl_book, keterangan_lain, status, estimasi_waktu_servis, date_created, date_approved):                        

        st.header(" ", divider="rainbow")
        st.header(f":rainbow[BOOKING DETAILS]", divider="rainbow")
        st.subheader("")

        st.subheader(kode_servis, divider="grey")

        a, b = st.columns([2, 2])
        with a:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write(f"Name")
                st.write(f"Address")
            with col2:
                st.write(f": {nama}")
                st.write(f": {alamat}")
        with b:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write(f"Phone")
                st.write(f"Gender")
            with col2:
                st.write(f": 0{tlp}")
                st.write(f": {jk}")

        st.subheader(" ")
        st.subheader("Car Specifications", divider="grey")

        a, b = st.columns([2, 2])
        with a:
            col1, col2 = st.columns([3, 3])
            with col1:
                st.write(f"Number Plate")
                st.write(f"Model")
                st.write(f"Transmission")
                st.write(f"Fuel Type")
            with col2:
                st.write(f": {no_pol}")                
                st.write(f": {model_mobil}")
                st.write(f": {transmisi}")
                st.write(f": {fuel_type}")
        with b:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write(f"Year")
                st.write(f"Date")
                st.write(f"Packages")

            with col2:
                st.write(f": {tahun}")
                st.write(f": {tgl_book}")
                st.write(f": {pkt}")
                
        st.subheader(" ")
        st.subheader("Information", divider="grey")

        a, b = st.columns([2, 2])
        with a:
            col1, col2 = st.columns([3, 3])
            with col1:
                st.write(f"Time")
                st.write(f"Status")                
            with col2:
                if estimasi_waktu_servis == '08:00-08:00':
                   st.write(f": -")
                else:
                    st.write(f": {estimasi_waktu_servis}")                
                st.write(f": {status}")
                
        with b:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write(f"Date Created")
                st.write(f"Date Approved")                

            with col2:
                st.write(f": {date_created}")
                st.write(f": {date_approved}")            

        st.write(f"Other Information:")
        st.write(f"{keterangan_lain}")
        st.header(f"", divider="rainbow")
            
    with st.container(border=True):        
        data = df[df["Kode Servis"] == service_code].iloc[0]
        kode_servis = data["Kode Servis"]
        nama = data["Nama"]
        alamat = data["Alamat"]
        jk = data["Jenis Kelamin"]
        tlp = data["Nomor Telepon"]
        no_pol = data["Nomor Polisi"]
        model_mobil = data["Model"]
        transmisi = data["Transmisi"]
        fuel_type = data["Fuel Type"]
        tahun = data["Tahun"]
        pkt = data["Paket Service"]
        tgl_book = data["Tanggal Booking"]
        keterangan_lain = data["Keterangan Lain"]
        status = data["Status"]
        estimasi_waktu_servis = data["Estimasi Waktu Servis"]
        date_created = data["date_created"]
        date_approved = data["date approved"]
        
        st.subheader(f"SERVICE DETAILS {kode_servis}", divider="grey")        
        a, b = st.columns([2, 2])
        with a:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write(f"Name")
                st.write(f"Service Packages")
            with col2:            
                st.write(f": {nama}")
                st.write(f": {pkt}")
        with b:
            col1, col2 = st.columns([3, 3])
            with col1:
                st.write(f"Phone Number")
                st.write(f"Booking Date")
            with col2:            
                st.write(f": 0{tlp}")
                st.write(f": {tgl_book}")

        st.subheader(" ")                                                                                                                
        if st.button(" + More Details"):
            detail(kode_servis, nama, alamat, jk, tlp, no_pol, model_mobil, transmisi, fuel_type, tahun, pkt, tgl_book, keterangan_lain, status, estimasi_waktu_servis, date_created, date_approved)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    st.header(':rainbow[BooCar]', divider='rainbow')
    st.title("MANAGING BOOKING SERVICE")
    st.subheader(" ")        
    
    df = load_data()    
    st.write("---")
    
    col1, col2 = st.columns([3, 2])
    with col1:        
        tampilkan_status = st.selectbox("Status", ("Review", "Approve", "Pending", "Done"))        
        cari = st.text_input("Search Service Code")
        
    with col2:                
        with st.container(border=False,height=200):
            display_data_booking(df,tampilkan_status)    
            kode_servis = sorted(df["Kode Servis"].tolist())

    st.write("---")
    
    if cari:
        indeks = binary_search(kode_servis, cari)
        if indeks != -1:
            kode_servis_selected = kode_servis[indeks]            
            st.success(f"Service code {kode_servis_selected} found.")            
            tampil_detail_servis(df, kode_servis_selected)                                
            
        else:
            st.error("Service code not found.")            
        
        st.write("")            
        st.subheader("")
        st.subheader("Edit booking service data".upper(), divider="grey")                                               
        
        status = st.radio("Status", ("Review", "Approve", "Pending", "Done"), horizontal=True)                                    
                                            
        if status == "Approve" or status == "Pending":
            if status == "Approve":            
                tgl_booking = df[df["Kode Servis"] == kode_servis_selected]["Tanggal Booking"].iloc[0]            
                detail_servis = df[(df["Tanggal Booking"] == tgl_booking) & (df["Estimasi Waktu Servis"] != "08:00-08:00")][["Kode Servis", "Tanggal Booking", "Estimasi Waktu Servis", "Status"]]                            
                st.write(detail_servis)
                        
            if status == "Pending":                
                tgl_awal = df[df["Kode Servis"] == kode_servis_selected]["Tanggal Booking"].iloc[0]                                                                                    
                new_booking_date = st.date_input("New Booking Date")   
                tgl_booking_new = new_booking_date.strftime("%Y-%m-%d")

                col1,col2=st.columns([4,2])
                with col1:                    
                    detail_servis = df[(df["Tanggal Booking"] == tgl_booking_new) & (df["Estimasi Waktu Servis"] != "08:00-08:00")][["Kode Servis", "Tanggal Booking", "Estimasi Waktu Servis", "Status"]]                            
                    with st.container(height=170,border=False):
                        st.write(detail_servis)                           

                with col2:                
                    with st.container(border=True):
                        st.subheader("Rescheduling".upper(), divider="grey")                                               
                        st.write(f":grey[Previously: {tgl_awal}]")
                        st.write(f":grey[Updated: {new_booking_date}]")
            
            st.subheader("")                        
            durasi = df[df["Kode Servis"] == kode_servis_selected]["Estimasi Waktu Servis"].iloc[0]                            
            waktu_mulai, waktu_akhir = durasi.split('-')
            mulai = datetime.strptime(waktu_mulai, '%H:%M').time()
            selesai = datetime.strptime(waktu_akhir, '%H:%M').time()
            value = (mulai, selesai)                    
            
            appointment = st.slider("Schedule your appointment:", 
                                    value=value,
                                    min_value=time(8, 0),
                                    max_value=time(16, 0))

                                                
        st.write("---")
        
        if st.button("Submit"):
            st.success("Data Updated Successfully")
            df.loc[df["Kode Servis"] == kode_servis_selected, "Status"] = status
            
            if cari:                        
                if status == "Approve" or status == "Pending":
                    appointment_time = f"{appointment[0].strftime('%H:%M')}-{appointment[1].strftime('%H:%M')}"                            
                    df.loc[df["Kode Servis"] == kode_servis_selected, "Estimasi Waktu Servis"] = appointment_time                                                                                

                    if status == "Approve":                            
                        if "date approved" in df.columns:
                            df.loc[df["Kode Servis"] == kode_servis_selected, "date approved"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
                    if status == "Pending":
                        nama_pelanggan = df[df["Kode Servis"] == kode_servis_selected]["Nama"].iloc[0]
                        no_pelanggan = df[df["Kode Servis"] == kode_servis_selected]["Nomor Telepon"].iloc[0]                            
                        df.loc[df["Kode Servis"] == kode_servis_selected, "Tanggal Booking"] = new_booking_date.strftime("%Y-%m-%d")
                                                    
                        with st.container(border=True):
                            st.subheader(f"Schedule updated".upper(), divider="grey")                                               
                            st.write(f"Updated customer car service schedule")
                            st.write(f"Nama : {nama_pelanggan}")
                            st.write(f":grey[Previously: {tgl_awal}]")
                            st.write(f"Updated: {new_booking_date}")
                            st.link_button("Contact Customer", f"https://wa.me/+62{no_pelanggan}")                                                        
                    
            
                new_list = LinkedList()                
                for i in df.to_dict("records"):
                    new_list.append(i)
                    
                new_list.bubble_sort()
                new_list.bubble_sort_estimate_time()
                                
                new_df = pd.DataFrame(new_list.display())                
                simpan_data(new_df)                                

        
if __name__ == "__main__":
    main()   
