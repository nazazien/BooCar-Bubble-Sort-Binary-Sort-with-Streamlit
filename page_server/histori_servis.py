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
    df = pd.read_csv("data/data server/data_booking.csv")    
    linked_list = LinkedList()
    for _, row in df.iterrows():
        linked_list.append(row)
    return linked_list

def binary_search(data, status):
    hasil = []
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid]["Status"] == status:
            hasil.append(data[mid])
            left, right = mid - 1, mid + 1
            while left >= start and data[left]["Status"] == status:
                hasil.append(data[left])
                left -= 1
            while right <= end and data[right]["Status"] == status:
                hasil.append(data[right])
                right += 1
            break
        elif data[mid]["Status"] < status:
            start = mid + 1
        else:
            end = mid - 1
    return hasil

def main():
    st.header(':rainbow[BooCar]', divider='rainbow')
    st.title("VIEW SERVICE HISTORY")
    st.subheader(" ")
    st.subheader(" ")

    linked_list = load_data()
    
    st.subheader('', divider='grey')

    col1, col2, col3 = st.columns([2, 5, 2])
    with col2:
        st.header('SERVICE HISTORY DATA')

    st.subheader('')
    
    status_list = ["Review", "Approve", "Pending", "Done"]
    pilih_status = []
        
    centang = st.columns(len(status_list))
    for i, status in enumerate(status_list):
        if centang[i].checkbox(f"Show {status}"):
            pilih_status.append(status)

    data = list(linked_list.display())
    data.sort(key=lambda x: x["Status"])

    filtered_data = []
    if pilih_status:
        for status in pilih_status:
            filtered_data.extend(binary_search(data, status))
    else:
        filtered_data = data

    df = pd.DataFrame(filtered_data, columns=["Nama", "Model", "Paket Service", "Tanggal Booking", "Status"])
    with st.container(border=True, height=380):
        st.table(df.style.set_table_styles(
            [{'selector': 'th', 
              'props': [('background-color', '#FFDDA1'), 
                        ('color', 'black')]}]))
    
    st.write(f"Total : {len(df)} data")
    st.subheader('', divider='grey')

if __name__ == "__main__":
    main()
