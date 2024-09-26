from keperluan_modul import *
bg()

def check_login(username, password):
    with open('data/data server/data_user.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return row['level']
    return None

def login():
    st.header(":rainbow[BooCar]", divider="rainbow")   
    col1,col2,col3=st.columns([2,1,2])
    with col2:        
        st.title("Login".upper())   

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        level = check_login(username, password)
        if level:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.session_state.level = level
            st.balloons()
            if level == "admin":
                st.success(f"Halo {st.session_state.user}, Anda telah berhasil login.")
            elif level == "user":
                st.success(f"Halo {st.session_state.user}, Anda telah berhasil login.")
        else:
            st.error("Login gagal. Silakan coba lagi.")


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'level' not in st.session_state:
    st.session_state.level = None


if not st.session_state.logged_in:    
    login()
else:
    if st.session_state.level == "admin":
        show_pages([
            Page("page_server/home.py", "🏠 Dashboard"),
            Page("page_server/cek_antrean.py", "👥 Check Queue"),
            Page("page_server/approve_booking.py", "✅ Manage Service Booking"),
            Page("page_server/histori_servis.py", "⏳ Service History"),
            Page("page_server/rating_dan_ulasan.py", "🌟 FeedBacks"),
            Page("about_us.py", "👤 About Us"),
        ])

        st.header(':rainbow[BooCare by BooiCode]', divider='rainbow')
        st.title('CAR SERVICE BOOKING APPLICATION')
        st.write(':grey[Thursday, April 4 2024 at 2:48:11 PM]')
        st.title('')

        data = pd.read_csv('data/data server/data_booking.csv')

        total_data = data.shape[0]
        total_review = data[data['Status'] == 'Review'].shape[0]
        total_approve = data[data['Status'] == 'Approve'].shape[0]
        total_pending = data[data['Status'] == 'Pending'].shape[0]
        total_done = data[data['Status'] == 'Done'].shape[0]

        data['Tanggal Booking'] = pd.to_datetime(data['Tanggal Booking'])
        data['Bulan'] = data['Tanggal Booking'].dt.month_name()

        months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
        data['Bulan'] = pd.Categorical(data['Bulan'], categories=months_order, ordered=True)

        jml_bulanan = data.groupby('Bulan').size().reset_index(name='Jumlah')
        jml_bulanan = jml_bulanan.sort_values('Bulan')

        fig_bulanan = px.line(jml_bulanan, x='Bulan', y='Jumlah', color_discrete_sequence=px.colors.qualitative.Set3)
        fig_bulanan.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            font_color="white"
        )

        st.write(":grey[Total Customers per Month]")
        st.plotly_chart(fig_bulanan, use_container_width=True)

        col1, col2 = st.columns([2, 2])
        with col1:
            persentase_approved = (total_approve / total_data) * 100
            persentase_done = (total_done / total_data) * 100
            donut = pd.DataFrame({
                'Label': ['Approved', 'Done'],
                'Value': [persentase_approved, persentase_done]
            })
            fig_approved = px.pie(donut, values='Value', names='Label', hole=0.5, color_discrete_sequence=px.colors.qualitative.Set3)
            fig_approved.update_traces(textinfo='percent+label')
            fig_approved.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                font_color="white"
            )
            st.plotly_chart(fig_approved, use_container_width=True)

        with col2:
            label_status = ['Review', 'Approve', 'Pending', 'Done']
            jml = [total_review, total_approve, total_pending, total_done]
            
            fig_bar = go.Figure(go.Bar(
                x=jml,
                y=label_status,
                orientation='h',
                marker=dict(color=['#ffee93', '#a0ced9', '#ffc09f', '#adf7b6']),
                width=0.35
            ))

            fig_bar.update_layout(
                xaxis_title="Count",
                yaxis_title="Status",
                margin=dict(l=0, r=0, t=30, b=0),
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                font_color="white"
            )

            st.plotly_chart(fig_bar, use_container_width=True)


    elif st.session_state.level == "user":            
        show_pages([
            Page("page_klien/home.py", "🏠 Home"),              
            Page("page_klien/cek_booking.py", "📅 Check Queue"),
            Page("page_klien/daftar_booking_servis.py", "🚗 Register Service Booking"),                    
            Page("page_klien/rating_dan_ulasan.py", "🌟 FeedBacks"),    
            Page("about_us.py", "👤 About Us"),                                            
        ])

        st.header(':rainbow[BooCare by BoiCode?]', divider='rainbow')
        st.title('CAR SERVICE BOOKING APPLICATION')
        st.write(':grey[Thursday, April 4 2024 at 2:48:11 PM]')
        st.title('')

        st.subheader('WANT TO SERVICE YOUR CAR HERE?')
        st.image(Image.open('img/mobil.jpg'), width=500, caption='Source: https://storyset.com/')
        st.subheader('What is BooCare?')
        st.markdown('''BooCare is a Car Service Booking application. This service provides customers with the convenience of scheduling their 
                    service visits to authorized workshops, thereby shortening the waiting time from long queues. This will certainly make it 
                    easier for customers to manage their service visit schedules to authorized workshops according to their needs. 
                    :rainbow[Come on, try it now here!]''')