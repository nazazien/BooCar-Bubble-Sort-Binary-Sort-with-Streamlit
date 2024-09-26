from keperluan_modul import *
bg()

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid]['Rating'] == x:
            return mid
        elif arr[mid]['Rating'] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def main():
    st.header(':rainbow[BooCar]', divider='rainbow')
    st.title("SERVICE ASSESSMENT")
    st.subheader(" ")

    try:
        feedback_sebelumnya  = pd.read_csv('data/data server/ulasan.csv')
        feedback_sebelumnya  = feedback_sebelumnya .sort_values(by='Rating').to_dict(orient='records')
        
        st.subheader("Ratings & Feedbacks", divider="grey")

        hitung_rating = pd.Series([feedback['Rating'] for feedback in feedback_sebelumnya ]).value_counts().sort_index()
        pilihan_rating = [f"⭐️" * rating + f" {hitung_rating.get(rating, 0)}" for rating in range(5, 0, -1)]

        pilih_bintang = st.selectbox("Select Rating", options=pilihan_rating)
        rating_selected = 5 - pilihan_rating.index(pilih_bintang)

        index = binary_search(feedback_sebelumnya , rating_selected)
        filter_feedback = []

        if index != -1:
            start = index
            while start >= 0 and feedback_sebelumnya [start]['Rating'] == rating_selected:
                start -= 1
            start += 1
            end = index
            while end < len(feedback_sebelumnya ) and feedback_sebelumnya [end]['Rating'] == rating_selected:
                end += 1
            filter_feedback = feedback_sebelumnya [start:end]

        with st.container(border=True , height=330):
            if filter_feedback:
                for row in filter_feedback:
                    with st.chat_message("user"):
                        col1, col2 = st.columns([15, 1])
                        with col1:
                            stars = "⭐️" * row['Rating']
                            st.write(f"{stars}")
                        with col2:
                            st.write(f"{row['Rating']}/5")
                        st.write(f":grey[{row['Timestamp']}]")
                        st.write("")
                        st.write(row['Ulasan'])
            else:
                st.write("No feedbacks matching the selected star rating.")

    except FileNotFoundError:
        st.write("There are no feedbacks yet.")    

    st.subheader("", divider="rainbow")

if __name__ == "__main__":
    main()
