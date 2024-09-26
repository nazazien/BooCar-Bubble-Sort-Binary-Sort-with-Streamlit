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
            
def load_data():
    df = pd.read_csv("data/data server/data_booking.csv", dtype={'No HP': str})
    df = df[df["Status"] == "Approve"]    
    linked_list = LinkedList()
    for _, row in df.iterrows():
        linked_list.append(row.to_dict())
    return linked_list

def main():
    st.header(':rainbow[BooCar]', divider='rainbow')
    st.title("VIEW SERVICE QUEUE")
    st.subheader(" ")    

    linked_list = load_data()

    pilih_tgl = st.date_input("Select Date")
    col1, col2, col3 = st.columns([3,1,3])
    with col2:
        submit = st.button("Submit")
    st.subheader('', divider='rainbow')

    if submit: 
        if pilih_tgl: 
            col1, col2, col3 = st.columns([2,5,2])                
            with col2:
                st.header(':rainbow[SERVICE QUEUE DATA]')     
                            
            st.write(f':grey[Date {pilih_tgl}]', divider="grey")                        
            st.subheader('')
            
            data_yang_dipilih = [data for data in linked_list.display() if data["Tanggal Booking"] == str(pilih_tgl)]

            if data_yang_dipilih:
                df_pilih_tgl = pd.DataFrame(data_yang_dipilih)
                df_pilih_tgl["Estimasi Waktu Servis"] = df_pilih_tgl["Estimasi Waktu Servis"].apply(lambda x: f"{datetime.strptime(str(x), '%H.%M').strftime('%H.%M')} hours" if isinstance(x, float) else x)
                st.table(df_pilih_tgl.style.set_table_styles([{'selector': 'th',
                                                                'props': [('background-color', '#FFDDA1'), 
                                                                            ('color', 'black')]}]))
            else:
                st.write("No service queue data for the selected date.")

            st.subheader('', divider='rainbow')

if __name__ == "__main__":
    main()
