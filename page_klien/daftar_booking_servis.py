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

def bubble_sort(df):
    if df.empty:
        return
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(df) - 1):
            current_date = datetime.strptime(str(df.iloc[i]["Tanggal Booking"]), "%Y-%m-%d")
            next_date = datetime.strptime(str(df.iloc[i + 1]["Tanggal Booking"]), "%Y-%m-%d")
            if current_date > next_date:
                df.iloc[i], df.iloc[i + 1] = df.iloc[i + 1].copy(), df.iloc[i].copy()
                swapped = True

def generate_kode_servis(tanggal_booking, df):    
    tahun = str(tanggal_booking.year)[-2:]        
    
    bulan_romawi = {
        1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
        7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII"
    }
    bulan = bulan_romawi[tanggal_booking.month]
        
    df_filtered = df[df["Kode Servis"].str.contains(f"KDS/{tahun}/{bulan}")]        
    if not df_filtered.empty:
        max_number = df_filtered["Kode Servis"].str.split('/').str[-1].astype(int).max()
    else:
        max_number = 0
        
    new_number = str(max_number + 1).zfill(3)
    new_code = f"KDS/{tahun}/{bulan}/{new_number}"
    
    return new_code

def hubungi_penjual(nama, jadwal):
    no_penjual = 85806871679    
    copy_pesan = f"Halo, perkenalkan nama saya *{nama}.* Saya adalah pengguna Layanan Website BooCare oleh *BooiCode.* Saya ingin mengonfirmasi bahwa saya akan melakukan servis mobil pada tanggal *{jadwal}*. Terimakasih atas waktu Anda!"
    link_wa = f"https://wa.me/+62{no_penjual}?text={copy_pesan}"        
    
    st.subheader("", divider="rainbow")            
    st.link_button("Contact Admin", link_wa)
    st.subheader("",divider="rainbow")

def load_data():
    return pd.read_csv("data/data server/data_booking.csv")

def save_data(df):
    df.to_csv("data/data server/data_booking.csv", index=False)

st.header(':rainbow[BooCar]', divider='rainbow')
st.title('Booking Service Registration Form'.upper())
st.subheader("")    

df = load_data()
x = pd.read_csv("data/toyota.csv")

with st.container(border=True):
    st.subheader('Personal data', divider="grey")        
    st.subheader("")      
    col1,col2=st.columns([2,2])
    with col1:    
        nama = st.text_input("Name")
        alamat = st.text_input("Address")
    with col2:    
        jenis_kelamin = st.radio("Gender", options=["Male", "Female"])
        no_telp = st.text_input("Phone Number")
        
    st.write("")
    st.subheader('Car specification data', divider="grey")        
    st.subheader("")
    col1,col2,col3=st.columns([2,2,2])
    with col1:
        no_pol = st.text_input("Number Plate")
        model_mobil = st.selectbox("Car Model", options=x["model"].unique())        
    with col2:
        transmisi = st.selectbox("Transmission", options=x["transmission"].unique())
        fuel_type = st.selectbox("Fuel Type", options=x["fuelType"].unique())
    with col3:
        tahun = st.number_input("Year", min_value=2000, max_value=datetime.now().year)
        paket_service = st.multiselect("Service Packages", options=["Periodic Service", "Tune Up Service", "Body and Paint Service"])
    
    tanggal_booking = st.date_input("Booking Date")
    keterangan_lain = st.text_area("Other Information")
    st.write("---")        
    submit_button = st.button("Submit")
    
if submit_button:                   
    st.success(f"Successfully booked an service Car!")      
        
    st.header(" ", divider="rainbow")
    st.header(f":rainbow[BOOKING DETAILS]", divider="rainbow")                            
    st.subheader("")

    kode_servis = generate_kode_servis(tanggal_booking, df)
    st.subheader(kode_servis,divider="grey")

    a,b=st.columns([2,2])
    with a:
        col1,col2=st.columns([2,3])
        with col1:
            st.write(f"Name")
            st.write(f"Address")
        with col2:            
            st.write(f": {nama}")
            st.write(f": {alamat}")                        
    with b:
        col1,col2=st.columns([3,3])
        with col1:
            st.write(f"Phone Number")
            st.write(f"Gender")
        with col2:            
            st.write(f": {no_telp}")
            st.write(f": {jenis_kelamin}")           

    st.subheader(" ")                                                                                                                
    st.subheader("Car Specifications",divider="grey")    

    a,b=st.columns([2,2])
    with a:
        col1,col2=st.columns([2,3])
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
        col1,col2=st.columns([2,3])
        with col1:
            st.write(f"Year")        
            st.write(f"Booking Date")
            st.write(f"Service Packages")

        with col2:       
            st.write(f": {tahun}")        
            st.write(f": {tanggal_booking}")
            st.write(f": {', '.join(paket_service)}")
    st.write(f"Other Information:")
    st.write(f"{keterangan_lain}")
            
    hubungi_penjual(nama,tanggal_booking)                     

    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Review"
    estimasi = "08:00-08:00"
            
    new_data = {
        "Kode Servis": kode_servis,
        "Nama": nama,
        "Alamat": alamat,
        "Jenis Kelamin": jenis_kelamin,
        "Nomor Telepon": no_telp,
        "Nomor Polisi": no_pol,
        "Model": model_mobil,
        "Transmisi": transmisi,
        "Fuel Type": fuel_type,
        "Tahun": tahun,
        "Paket Service": ', '.join(paket_service),
        "Tanggal Booking": tanggal_booking,
        "Keterangan Lain": keterangan_lain,
        "Status": status,
        "Estimasi Waktu Servis": estimasi,  
        "date_created": date_created,
        "date approved": ""  
    }

    linked_list = LinkedList()
    linked_list.append(new_data)        
    existing_data = load_data()          

    df = pd.concat([existing_data, pd.DataFrame(linked_list.display())], ignore_index=True)    
    bubble_sort(df)        
    save_data(df)
